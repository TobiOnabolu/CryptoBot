#from strategy import Strategy
#from exchange.binance import Binance
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

password = os.getenv('PASS')
print(password)

#connecting to an exhange
#exchange = Binance(key='', secret='')

#set currency, asset, strategy

#exchange will gather data from exchange

#stategy will have excchange variable to have access to that date


#starts the program
#runner = Strategy(exchange)

#runner will have to call ._run to begin our strategy

#our strategy will have to call exhchanges methods to get data and place orders