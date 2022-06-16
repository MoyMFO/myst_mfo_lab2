
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
from functions import PricingModelsOB
from data import DataPreparation
import pandas as pd

class PlotsModelsOB:

    @staticmethod
    def plot_apt_model_count(data: pd.DataFrame, price_type: str) -> go.Figure:

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
    def plot_apt_model_portion(data: pd.DataFrame, price_type: str) -> go.Figure:

        fig = go.Figure(data=[
        go.Bar(name='e1 count', x=data['interval'], y=data['e1_portion']),
        go.Bar(name='e2 count', x=data['interval'], y=data['e2_portion'])
        ])

        # Size
        fig.update_layout(
        autosize=False,
        width=1000,
        height=800)

        # Title
        fig.update_layout(barmode='stack')
        fig.update_layout(height=600, width=600, title_text=f"{price_type}: Proportion of Martingala proces")

        # Axis layout
        fig.update_xaxes(title_text="<b>Minute Bucket</b>")
        fig.update_yaxes(title_text="<b>Proportion of Martingala Process</b>")
        return fig.show()