
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
import data as dt
from data import DataPreparation
from functions import OrderBookMeasures, PricingModelsOB
from visualizations import PlotsModelsOB

data = DataPreparation()
plot = PlotsModelsOB()
order_book_data = data.order_books_json_transformation("files/orderbooks_05jul21.json")
order_book_measure = OrderBookMeasures(order_book_data)
model = PricingModelsOB(order_book_data)


# Martingala Exploration with mid price method
# print(model.apt_model('mid_price', by='1T'))
# Martingala Exploration with weighted mid price method
# print(model.apt_model('weighted_midprice', by='1T'))

# plot.plot_apt_model_count(model.apt_model('mid_price', by='1T'), 'mid price')
# plot.plot_apt_model_percentage(model.apt_model('mid_price', by='1T'), ' weighted mid price')

print(model.roll_model())


