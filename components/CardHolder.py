# components/my_component.py
from dash import html
from components.Card import Card

def CardHolder():

    return html.Div([
            Card("Total Cases", 1000, "sky-500"),
            Card("Total Deaths", 1000, "fuchsia-500"),
            Card("Total Recovered", 1000, "green-500"),
            Card("Total Active", 1000, "amber-500"),


        ], className="""w-full flex justify-between items-center
        gap-4
        """)
