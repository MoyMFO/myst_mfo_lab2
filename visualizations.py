
"""
# -- --------------------------------------------------------------------------------------------------- -- #
# -- project: A SHORT DESCRIPTION OF THE PROJECT                                                         -- #
# -- script: visualizations.py : python script with data visualization functions                         -- #
# -- author: YOUR GITHUB USER NAME                                                                       -- #
# -- license: THE LICENSE TYPE AS STATED IN THE REPOSITORY                                               -- #
# -- repository: YOUR REPOSITORY URL                                                                     -- #
# -- --------------------------------------------------------------------------------------------------- -- #
"""
import plotly.graph_objects as go
import pandas as pd

class PlotsModelsOB:
    """
    This class contains methods to plot the apt model.
    OrderBookMeasure class inherits methods to this class to leverage from prices calculation
    like midprice or weighted midprice.

    Parameters
    ------------
    data_ob: dict (default: None)
        Orderbook data, it should be a dictionary following next structures:
        'timestamp': timestamp object, e.g. pd.to_datetime()
        'bid_size': bid levels volumes
        'ask_size': ask levels volumes
        'bid': bid levels prices
        'ask': ask levels prices

    Attributes
    ------------
    Both are attributes comming from OrderBookMeasures class.

    ob_ts: list of orderbooks keys.
    l_ts: list of timestamps of orderbooks.
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
        go.Bar(name='e1 count', x=data['interval'], y=data['e1_count']),
        go.Bar(name='e2 count', x=data['interval'], y=data['e2_count'])
        ])

        # Size
        fig.update_layout(
        autosize=False,
        width=1000,
        height=800)

        # Title
        fig.update_layout(barmode='stack')
        fig.update_layout(height=600, width=600, title_text=f"{price_type}: Count of Martingala proces")
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
        go.Bar(name='e1 count', x=data['interval'], y=data['e1_percentage']),
        go.Bar(name='e2 count', x=data['interval'], y=data['e2_percentage'])
        ])

        # Size
        fig.update_layout(
        autosize=False,
        width=1000,
        height=800)

        # Title
        fig.update_layout(barmode='stack')
        fig.update_layout(height=600, width=600, title_text=f"{price_type}: Propercentage of Martingala proces")

        # Axis layout
        fig.update_xaxes(title_text="<b>Minute Bucket</b>")
        fig.update_yaxes(title_text="<b>Propercentage of Martingala Process</b>")
        return fig.show()