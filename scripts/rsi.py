# importação das bibliotecas

import pandas as pd
import numpy as np
from finta import TA
import MetaTrader5
import pytz
from datetime import datetime , date

#  inserir seus dados
user = 'seu usuário'
pwd = 'sua senha'
server = 'o servidor da sua corretora(a mesma deve te informar)'

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
ativo = pd.read_csv('E:\Projects\Bot_MetaTrader5-MT5\data\ativos.txt')

# dia, mês e ano referente ao dia corrente
ano = datetime.today().year
mes = datetime.today().month
dia = datetime.today().day

# definimos o fuso horário
timezone = pytz.timezone("Brazil/DeNoronha")
utc_from = datetime(2021, 4, 30, tzinfo=timezone)
rates = mt5.copy_rates_from(ativo , mt5.TIMEFRAME_D1 , utc_from, 82)

rf = pd.DataFrame(rates)
rf['RSI']= TA.RSI(rf)

rf['RSI'] = rf['close'].apply(RSI)