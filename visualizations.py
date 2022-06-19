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
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd

class PlotsModelsOB:
    """
    This class contains methods to plot the apt model and the Roll model.
    It contains two methods one for each model, those only requires the
    intended data and the title of what is being plotted.

    Parameters
    ------------
    Not required to initialize the class.

    Attributes
    ------------
    Not specific in this class.
    """

    @staticmethod
    def plot_apt_model_count(data: pd.DataFrame, price_type: str) -> go.Figure:

        """
        This method plots the calculation of count of the apt model.

        Parameters 
        ----------
        Required on calling:
            data: DataFrame. e.g. 'mid_price' or 'weighted_midprice'.
                 It should contain columns 'e1_count' and 'e2_count'
            price_type: str. The name of data to plot.
        Returns
        ------
        Plot e1 and e2 count: Figure
        """

        fig = go.Figure(data=[
        go.Bar(name='e1 count', x=data['interval'], y=data['e1_count'], marker_color='navy'),
        go.Bar(name='e2 count', x=data['interval'], y=data['e2_count'], marker_color='goldenrod')
        ])

        # Size
        fig.update_layout(
        autosize=False,
        width=900,
        height=800)

        # Title
        fig.update_layout(barmode='stack')
        fig.update_layout(title_text=f"{price_type}: Count of Martingala process",
                          legend=dict(orientation="h"))
        # Axis layout
        fig.update_xaxes(title_text="<b>Minute Bucket</b>")
        fig.update_yaxes(title_text="<b>Count of Martingala Process</b>")

        return fig.show()

    @staticmethod
    def plot_apt_model_percentage(data: pd.DataFrame, price_type: str) -> go.Figure:

        """
        This method plots the calculation of percentage of the apt model.

        Parameters 
        ----------
        Required on calling:
            data: DataFrame. e.g. 'mid_price' or 'weighted_midprice'.
                 It should contain columns 'e1_percentage' and 'e2_percentage'
            price_type: str. The name of data to plot.
        Returns
        ------
        Plot e1 and e2 percentage: Figure
        """

        fig = go.Figure(data=[
        go.Bar(name='e1 count', x=data['interval'], y=data['e1_percentage'], marker_color='cadetblue'),
        go.Bar(name='e2 count', x=data['interval'], y=data['e2_percentage'], marker_color='firebrick')
        ])

        # Size
        fig.update_layout(
        autosize=False,
        width=900,
        height=800)

        # Title
        fig.update_layout(barmode='stack')
        fig.update_layout(title_text=f"{price_type}: Propercentage of Martingala process",
                          legend=dict(orientation="h"))

        # Axis layout
        fig.update_xaxes(title_text="<b>Minute Bucket</b>")
        fig.update_yaxes(title_text="<b>Percentage of Martingala Process</b>")

        return fig.show()

    @staticmethod
    def plot_roll_model(data: pd.DataFrame) -> go.Figure:
        
        """
        This method plots the calculation of bid and ask  with Roll model.

        Parameters 
        ----------
        Required on calling:
            data: DataFrame with columns ['bid_calculated','bid','ask_calculated','ask'].
        Returns
        ------
        Plots of all columns as subplots: Figure
        """

        fig = make_subplots(
            rows=2, cols=2,
            subplot_titles=("Bid with Roll model", "Actual Bid",
                            "Ask with Roll model", "Actual ask"))

        fig.add_trace(go.Scatter(x=data.index, y=data['bid_calculated'],
                   line=dict(color='magenta', width=1), name='bid calculated'),
                    row=1, col=1)

        fig.add_trace(go.Scatter(x=data.index, y=data['bid'], 
                   line=dict(color='royalblue', width=1), name='actual bid'),
                    row=1, col=2)

        fig.add_trace(go.Scatter(x=data.index, y=data['ask_calculated'],
                   line=dict(color='brown', width=1), name='ask calculated'),
                    row=2, col=1)


        fig.add_trace(go.Scatter(x=data.index, y=data['ask'],
                   line=dict(color='red', width=1), name='actual ask'),
                    row=2, col=2)

        # Title
        fig.update_layout(height=800, width=980, title_text=f"Bid-Ask with Roll model",
                          legend=dict(orientation="h"))

        # Axis layout
        fig.update_xaxes(title_text="<b>Time</b>")
        fig.update_yaxes(title_text="<b>$</b>")

        return fig.show()
    
    @staticmethod
    def plot_spread_comparison(data: pd.DataFrame) -> go.Figure:
        """
        This method plots the calculated spread and the actual spread.

        Parameters 
        ----------
        Required on calling:
            data: DataFrame with columns ['spread_calculated',''spread'].
        Returns
        ------
        Plots of comparison b/w spreads: Figure
        """

        fig = go.Figure()

        fig.add_trace(go.Scatter(x=data.index, y=data['spread_calculated'],
                        line=dict(color='blue', width=2), name='spread calculated'))

        fig.add_trace(go.Scatter(x=data.index, y=data['spread'],
                        line=dict(color='red', width=2), name='spread'))                

        # Title
        fig.update_layout(height=800, width=980, title_text=f"Spread Calculated vs Actual Spread",
                        legend=dict(orientation="h"))

        # Axis layout
        fig.update_xaxes(title_text="<b>Time</b>")
        fig.update_yaxes(title_text="<b>$</b>")

        return fig.show()

