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

        # Title and make the bar plot in stack mode
        fig.update_layout(barmode='stack')
        fig.update_layout(title_text=f"{price_type}: Count of Martingala process",
                          legend=dict(orientation="h"))
        
        # xticks
        fig.update_layout(
            xaxis = dict(
            tickmode = 'linear',
            tick0 = 1,
            dtick = 1))

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

         # xticks
        fig.update_layout(
            xaxis = dict(
            tickmode = 'linear',
            tick0 = 1,
            dtick = 1))

        # Axis layout
        fig.update_xaxes(title_text="<b>Minute Bucket</b>")
        fig.update_yaxes(title_text="<b>Percentage of Martingala Process</b>")

        return fig.show()

    @staticmethod
    def plot_roll_model(data: pd.DataFrame, serie_type: str='calculated') -> go.Figure:
        
        """
        This method plots the calculation of bid and ask  with Roll model. In case 
        a comparison against the actuals, it is possible to plot them.

        Parameters 
        ----------
        Required on calling:
            data: DataFrame with columns ['bid_calculated','bid','ask_calculated','ask'].
            type: str 'calculated' or 'actual'. Default 'calculated'.
        Returns
        ------
        Plots of all columns as subplots: Figure
        """
        options = {
            'calculated': ['bid_calculated', 'ask_calculated', 'Bid-Ask with Roll model'],
            'actual':     ['bid', 'ask', 'Bid-Ask Observed']
        }
        # Crafting of subplots to show the price which varies a little bit
        fig = go.Figure()

        fig.add_trace(go.Scatter(x=data.index, y=data[options[serie_type][0]],
                   line=dict(color='blue', width=0.7), name=options[serie_type][0]))

        fig.add_trace(go.Scatter(x=data.index, y=data[options[serie_type][1]], 
                   line=dict(color='firebrick', width=0.7), name=options[serie_type][1]))

        fig.add_trace(go.Scatter(x=data.index, y=data['mid_price'],
                   line=dict(color='green', width=0.7), name='mid_price'),)


        # Title and make the bar plot in stack mode
        fig.update_layout(height=800, width=980, title_text=options[serie_type][2],
                          legend=dict(orientation="h"))

        # Axis layout
        fig.update_xaxes(title_text="<b>Time</b>")
        fig.update_yaxes(title_text="<b>$</b>")

        return fig.show()
    
    @staticmethod
    def plot_spread_comparison_series(data: pd.DataFrame) -> go.Figure:
        """
        This method plots the calculated spread and the actual spread.

        Parameters 
        ----------
        Required on calling:
            data: DataFrame with columns ['spread_calculated',''spread'].
        Returns
        ------
        Plots of comparison b/w spreads as series: Figure
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

    @staticmethod
    def plot_spread_comparison_bars(data: pd.DataFrame, by: str='2T') -> go.Figure:
        """
        This method plots the calculated spread and the actual spread.

        Parameters 
        ----------
        Required on calling:
            data: DataFrame with columns ['spread_calculated',''spread'].
        Returns
        ------
        Plots of comparison b/w spreads in bars: Figure
        """
        data = data.resample(by).sum()

        fig = go.Figure()

        fig.add_trace(go.Bar(x=data.index, y=data['spread_calculated'],
                    marker_color='blue', name='spread calculated'))

        fig.add_trace(go.Bar(x=data.index, y=data['spread'], 
                    marker_color='firebrick', name='spread'))                

        # Title
        fig.update_layout(height=800, width=980, title_text=f"Spread Calculated vs Actual Spread",
                        legend=dict(orientation="h"))

        # Axis layout
        fig.update_xaxes(title_text="<b>Time</b>")
        fig.update_yaxes(title_text="<b>$</b>")

        return fig.show()
