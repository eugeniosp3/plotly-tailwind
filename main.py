from dash import Dash, html
from components.CardHolder import CardHolder
from components.MainBox import MainBox

import pandas as pd

# using this to bring in the tailwind css via their cdn 
# a CDN is a content delivery network - it's a way to bring in external resources
# without having to download them to your local machine, and then reference them,
# which is what we did with the local css file
# you can do the external_stylesheets, but it will not work with the latest (3.3) version of tailwind
external_scripts = [
    {'src': 'https://cdn.tailwindcss.com'}
]
app = Dash(__name__, 
           external_scripts=external_scripts
           )

df = pd.read_csv("data.csv")
print(df.shape)

app.layout = html.Div(
    [
        CardHolder(),
        MainBox(),
    ],
    className="""w-full h-screen bg-slate-100 p-10 gap-4
    flex flex-col justify-center items-center
    
    """
)

if __name__ == "__main__":
    app.run_server(debug=True)
