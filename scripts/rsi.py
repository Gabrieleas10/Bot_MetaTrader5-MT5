# importação das bibliotecas

import pandas as pd
import numpy as np
from finta import TA
import MetaTrader5 as mt5
import pytz
from datetime import datetime , date

#  inserir seus dados
user = 1000063862
pwd = 'G@briel10'
server = 'ClearInvestimentos-PRD'

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

# numero de periodos do indicador
n_period = 14
# quantidade de pregões desde o dia inicial
range_time = 60 # em dias pois estou usando timeframe diário

print('Executando o programa...')
for ativo in ativos:
    try:
        # coletando as informações do MT5
        rates = mt5.copy_rates_from(ativo , mt5.TIMEFRAME_D1 , utc_from, range_time)
        # transformando para dataframe
        rf = pd.DataFrame(rates)
        # criando coluna com o indicador
        rf['RSI']= TA.RSI(rf, n_period)
        if (rf['RSI'][range_time -1] < 25):
            new_row = {'Data': rf['time'][range_time-1], 'Ativo': ativo , 'Price': rf['close'][range_time-1] ,'Ação':'Compra'}
            resposta = resposta.append(new_row, ignore_index=True)
        if (rf['RSI'][range_time -1] > 75):
            new_row = {'Data': rf['time'][range_time-1], 'Ativo': ativo , 'Price': rf['close'][range_time-1] ,'Ação':'Venda'}
            resposta = resposta.append(new_row, ignore_index=True)
    except:
        pass

# gera o excel de resposta ao final do pregão com os ativos que tiveram os requisitos estabelecidos acionados
resposta.to_excel('E:\\Projects\\Bot_MetaTrader5-MT5\\output\\output_file.xlsx')