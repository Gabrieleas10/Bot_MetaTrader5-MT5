# importação das bibliotecas

import pandas as pd
import numpy as np
from finta import TA
import MetaTrader5 as mt5
import pytz
from datetime import datetime , date

#  inserir seus dados
user = 'seu usuário'
pwd = 'sua senha'
server = 'o servidor da sua corretora'

print('Conectando ao MetaTrader...')
# conecte-se ao MetaTrader 5
mt5.initialize()

authorized = mt5.login(login = user , password = pwd , server = server)
if authorized:
    # exibimos os dados sobre a conta de negociação como estão
    print('mt5.account_info()')
else:
    print("failed to connect at account #{}, error code: {}".format(user, mt5.last_error()))
    mt5.shutdown()


# impotação base com os ativos a ser analisados
ativos = pd.read_csv('E:\\Projects\\Bot_MetaTrader5-MT5\\data\\ativos.txt')
ativos = list(ativos['ativo'])

# criação de dataframe em branco
resposta = pd.DataFrame(columns = ['Data','Ativo','Price','Método'])

# dia, mês e ano referente ao dia corrente
ano = datetime.today().year
mes = datetime.today().month
dia = datetime.today().day

# definimos o fuso horário
timezone = pytz.timezone("Brazil/DeNoronha")
utc_from = datetime(ano, mes, dia, tzinfo=timezone)

# quantidade de pregões desde o dia inicial
range_time = 60 # em dias pois estou usando timeframe diário

print('Executando o programa...')
for ativo in ativos:
    try:
        # coletando as informações do MT5
        rates = mt5.copy_rates_from(ativo , mt5.TIMEFRAME_D1 , utc_from, range_time)
        # transformando para dataframe
        rf = pd.DataFrame(rates)
        # transformando a coluna da data no formato datetime
        rf['time'] = pd.to_datetime(rf['time'], unit='s')
        # cálculo das médias móveis
        rf['MM4'] = rf['close'].rolling(4).mean()
        rf['MM17'] = rf['close'].rolling(17).mean()
        rf['MM55'] = rf['close'].rolling(55).mean()
           
        if (rf['MM4'][range_time-1] < rf['MM17'][range_time-2]) and (rf['MM4'][range_time-1] >= rf['MM17'][range_time-1]) and (rf['MM17'][range_time-1] >= rf['MM55'][range_time-1]):
            new_row = {'Data': rf['time'][range_time], 'Ativo': ativo , 'Price': rf['close'][range_time] ,'Ação':'Compra'}
            resposta = resposta.append(new_row, ignore_index=True)
        else:
            pass
    except:
        pass

# gera o excel de resposta ao final do pregão com os ativos que tiveram os requisitos estabelecidos acionados
resposta.to_excel('E:\Projects\Bot_MetaTrader5-MT5\output\\output_file2.xlsx')