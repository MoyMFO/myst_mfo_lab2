
"""
# -- --------------------------------------------------------------------------------------------------- -- #
# -- project: A SHORT DESCRIPTION OF THE PROJECT                                                         -- #
# -- script: main.py : python script with the main functionality                                         -- #
# -- author: YOUR GITHUB USER NAME                                                                       -- #
# -- license: THE LICENSE TYPE AS STATED IN THE REPOSITORY                                               -- #
# -- repository: YOUR REPOSITORY URL                                                                     -- #
# -- --------------------------------------------------------------------------------------------------- -- #
"""

import numpy as np
import pandas as pd
from sklearn import metrics
import data as dt
from data import DataPreparation
from functions import OrderBookMeasures

data = DataPreparation()

order_book_data = data.order_books_json_transformation("files/orderbooks_05jul21.json")
order_book_measure = OrderBookMeasures(order_book_data)


# -- Calcular el midprice

mid_price = order_book_measure.mid_price()
mid_price.index = [pd.to_datetime(i) for i in list(order_book_data.keys())]

ob_ts = list(order_book_data.keys())[9:]
l_ts = [pd.to_datetime(i_ts) for i_ts in ob_ts]
# print(order_book_data)

# -- Contabilizar ocurrencias de escenarios (Utilizando todos los datos)
# Para contabilizar los e1 de acuerdo a esta formulación --> P_t = E[P_t+1]

# e1 = midprice_t == midprice_t+1
total = len(mid_price) -1
e1 = [mid_price.iloc[i_midprice] == mid_price.iloc[i_midprice + 1] for i_midprice in range(0, len(mid_price) - 1)]
e2 = total - sum(e1)

exp_1 = {'e1': {'cantidad': e1, 'proporcion': np.round(sum(e1)/total, 2)}, 
            'e2': {'cantidad': e2, 'proporcion': np.round(e2/total, 2)}, 
            'total': len(mid_price)-1}

# Imprimir los resultados
exp_1['e1']['proporcion']
exp_1['e2']['proporcion']


# e2 = midprice_t != midprice_t+1, e2 = total_datos - 1

# Imprimir el resultado en una tabla 

# -- Repetir lo anterior para otros (Experimentos)
# Experimentos: 00:06:00 - 00:06:00 ... 00:06:59 - 00:05:59 

minutes = list(np.arange(0, 60))

exp_2 = pd.DataFrame({'intervalo': list(np.arange(0, 60)), 'total': [2391]*len(minutes),
                      'e1_conteo': [1757]*len(minutes), 'e1_proporcion': [.73]*len(minutes),
                      'e2_conteo': [634]*len(minutes), 'e2_proporcion': [.27]*len(minutes)}, index=list(np.arange(0, 60)))

#list(np.arange(1, 60)) ==  list(set([i_ts.minute for i_ts in l_ts]))

# Y todo lo anterior también para Weighted-MidPrice

# Hacer 1 gráfica barplot
# Analisis simple, exploratorio y descriptivo
