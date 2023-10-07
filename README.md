[Visit the YouTube Channel](https://www.youtube.com/channel/UCwAsnLbyt87_TeGAKOkbm2w)
<br>[Holler at me on LinkedIn](https://linkedin.com/in/datagarage)
<br>[Join the Discord for fun](https://discord.gg/N84v7RAweS)



# Project Title: Dash-TailwindCSS Integration
**TLDR**
<br>This project demonstrates a powerful integration between Plotly's Dash—a Python web framework for building dashboards—and Tailwind CSS, a utility-first CSS framework, to create visually stunning and interactive data visualization web applications.
<br><br>**Here is how you bring tailwind to the party.**</br>
```python
external_scripts = [
    {'src': 'https://cdn.tailwindcss.com'}
]

app = Dash(__name__, 
           external_scripts=external_scripts
           )
```


**Main Features**
Efficient Styling with Tailwind CSS: Utilizing Tailwind CSS via its CDN to style Dash applications without the need to download or locally reference CSS files.

**Modular Design**
Employing a modular component structure similar to React or Next.js, ensuring a clean and maintainable codebase.

**Interactive Visualization**
Offering interactive visualizations with the ability to build upon more data-driven functionalities using Plotly and Dash.

**Code Structure**
Main Application Layout (main.py)
This script initializes the Dash application, brings in the Tailwind CSS using their CDN, reads a data file (data.csv), and sets up the main layout consisting of various components.
```
from dash import Dash, html
from components.CardHolder import CardHolder
from components.MainBox import MainBox
import pandas as pd

# External scripts for Tailwind CSS CDN
external_scripts = [{'src': 'https://cdn.tailwindcss.com'}]

app = Dash(__name__, external_scripts=external_scripts)
df = pd.read_csv("data.csv")

# Main Layout
app.layout = html.Div(
    [CardHolder(), MainBox()],
    className="w-full h-screen bg-slate-100 p-10 gap-4 flex flex-col justify-center items-center"
)

if __name__ == "__main__":
    app.run_server(debug=True)

```

**Components**
The project adheres to a component-based architecture, ensuring better code manageability and reusability.

**Card Component** Displays a card with a title and data with configurable color.
```
from dash import html

def Card(cardTitle, cardData, dataColor):
    return html.Div([
            html.P(cardTitle, className="text-gray-500 text-sm font-semibold text-slate-300"),
            html.P(cardData, className=f"text-5xl font-bold text-{dataColor}")
        ], 
        className="w-48 h-32 bg-white rounded-xl shadow-lg flex flex-col items-center justify-evenly"
    )
```

**CardHolder Component** Responsible for rendering multiple Card components.
```
from dash import html
from components.Card import Card

def CardHolder():
    return html.Div([
            Card("Total Cases", 1000, "sky-500"),
            Card("Total Deaths", 1000, "fuchsia-500"),
            Card("Total Recovered", 1000, "green-500"),
            Card("Total Active", 1000, "amber-500"),
        ], 
        className="w-full flex justify-between items-center gap-4"
    )
```



# Getting this all to run...
**Setup: Ensure you have Python, Dash, and Pandas installed.**

```
pip install dash pandas
```

**Run: Navigate to the project directory and execute the main.py.**
```
python main.py
```

Access the app at http://127.0.0.1:8050/ in your web browser.

Acknowledgements
Special thanks to:
1. Tailwind CSS for providing a dynamic and efficient styling framework.
2. Plotly's Dash for enabling robust data visualization capabilities in Python.
