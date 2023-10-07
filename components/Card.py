# components/my_component.py
from dash import html

def Card(cardTitle, cardData, dataColor):

    return html.Div([
        # html text, not an h1
        html.P(cardTitle, className=f""" 
        text-gray-500 text-sm font-semibold text-slate-300
"""),
        html.P(cardData, className=f"""
        text-5xl font-bold text-{dataColor}
 """)

        ], className="""
        w-48 h-32 bg-white rounded-xl
        shadow-lg flex flex-col items-center justify-evenly
        
        
        
        """)



