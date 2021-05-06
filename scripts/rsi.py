# importação das bibliotecas

import pandas as pd
import numpy as np
from finta import TA
import MetaTrader5
import pytz
from datetime import datetime , date

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