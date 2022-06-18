"""
# -- --------------------------------------------------------------------------------------------------- -- #
# project: This project has been created to show the operation of two price explanatory models 
# in the microstructure. On the one hand, the APT model that analyzes prices as a martingale
# stochastic process. On the other hand, the Roll model that aims to calculate the theoretical spread
# from transaction price data. Through considering the order book as an object that contains the data 
# on which the model is based,the pertinent classes were made to calculate and plot the models.          -- #
# -- script: data.py : python script for data collection                                                 -- #
# -- author: MoyMFO                                                                                      -- #
# -- license: GNU General Public License v3.0                                                            -- #
# -- repository: https://github.com/MoyMFO/myst_mfo_lab2                                                 -- #
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


# APT model exploration with mid price method
print(model.apt_model('mid_price', by='1T'))
# APT model exploration with weighted mid price method
print(model.apt_model('weighted_midprice', by='1T'))
# APT plots
plot.plot_apt_model_count(model.apt_model('mid_price', by='1T'), 'mid price')
plot.plot_apt_model_percentage(model.apt_model('mid_price', by='1T'), ' weighted mid price')
# Roll model exploration
print(model.roll_model())
# Roll model plots
plot.plot_roll_model(model.roll_model())


