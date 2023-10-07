# components/my_component.py
from dash import html, dcc

def MainBox():

    return html.Div([
        html.Div([
            dcc.Slider(
                min=0,
                max=100,
                step=1,
                value=50,
                marks={
                    0: {'label': '0'},
                    25: {'label': '25'},
                    50: {'label': '50'},
                    75: {'label': '75'},
                    100: {'label': '100'},
                },
                className="w-full"
            ),
            dcc.Slider(
                min=0,
                max=100,
                step=1,
                value=50,
                marks={
                    0: {'label': '0'},
                    25: {'label': '25'},
                    50: {'label': '50'},
                    75: {'label': '75'},
                    100: {'label': '100'},
                },
                className="w-full"
            ),
            dcc.Slider(
                min=0,
                max=100,
                step=1,
                value=50,
                marks={
                    0: {'label': '0'},
                    25: {'label': '25'},
                    50: {'label': '50'},
                    75: {'label': '75'},
                    100: {'label': '100'},
                },
                className="w-full"
            ),
            dcc.Slider(
                min=0,
                max=100,
                step=1,
                value=50,
                marks={
                    0: {'label': '0'},
                    25: {'label': '25'},
                    50: {'label': '50'},
                    75: {'label': '75'},
                    100: {'label': '100'},
                },
                className="w-full"
            ),
            dcc.Slider(
                min=0,
                max=100,
                step=1,
                value=50,
                marks={
                    0: {'label': '0'},
                    25: {'label': '25'},
                    50: {'label': '50'},
                    75: {'label': '75'},
                    100: {'label': '100'},
                },
                className="w-full"
            ),
            dcc.Slider(
                min=0,
                max=100,
                step=1,
                value=50,
                marks={
                    0: {'label': '0'},
                    25: {'label': '25'},
                    50: {'label': '50'},
                    75: {'label': '75'},
                    100: {'label': '100'},
                },
                className="w-full"
            ),
            dcc.Slider(
                min=0,
                max=100,
                step=1,
                value=50,
                marks={
                    0: {'label': '0'},
                    25: {'label': '25'},
                    50: {'label': '50'},
                    75: {'label': '75'},
                    100: {'label': '100'},
                },
                className="w-full"
            ),
            dcc.Slider(
                min=0,
                max=100,
                step=1,
                value=50,
                marks={
                    0: {'label': '0'},
                    25: {'label': '25'},
                    50: {'label': '50'},
                    75: {'label': '75'},
                    100: {'label': '100'},
                },
                className="w-full"
            ),
            dcc.Slider(
                min=0,
                max=100,
                step=1,
                value=50,
                marks={
                    0: {'label': '0'},
                    25: {'label': '25'},
                    50: {'label': '50'},
                    75: {'label': '75'},
                    100: {'label': '100'},
                },
                className="w-full"
            ),
            dcc.Slider(
                min=0,
                max=100,
                step=1,
                value=50,
                marks={
                    0: {'label': '0'},
                    25: {'label': '25'},
                    50: {'label': '50'},
                    75: {'label': '75'},
                    100: {'label': '100'},
                },
                className="w-full"
            ),
            dcc.Slider(
                min=0,
                max=100,
                step=1,
                value=50,
                marks={
                    0: {'label': '0'},
                    25: {'label': '25'},
                    50: {'label': '50'},
                    75: {'label': '75'},
                    100: {'label': '100'},
                },
                className="w-full"
            ),
            dcc.Slider(
                min=0,
                max=100,
                step=1,
                value=50,
                marks={
                    0: {'label': '0'},
                    25: {'label': '25'},
                    50: {'label': '50'},
                    75: {'label': '75'},
                    100: {'label': '100'},
                },
                className="w-full"
            ),
            
            
        ],
        className="""
        w-1/4 h-full flex flex-col justify-evenly items-center

        """),
        # end of sliders

        # div holding 4 stacked scatter plots each with made up data
        html.Div([html.Div([
            dcc.Graph(
                figure={
                    'data': [
                        {'x': [1, 2, 3, 4, 5], 'y': [1, 2, 3, 4, 5], 'type': 'scatter', 'name': 'SF'},
                        {'x': [1, 2, 3, 4, 5], 'y': [5, 4, 3, 2, 1], 'type': 'scatter', 'name': u'Montréal'},
                    ],
                    'layout': {
                        'title': 'Dash Data Visualization',
                        'font': {
                            'size': 8
                        },
                         # legend underneath
                        'legend': {
                            'orientation': 'h',
                            'yanchor': 'bottom',
                            'y': 1.02,
                            'xanchor': 'right',
                            'x': .75,
                        }
                           
                    }
                },
                className="w-1/2 h-full"
            ),
            dcc.Graph(
                figure={
                    'data': [
                        {'x': [1, 2, 3, 4, 5], 'y': [1, 2, 3, 4, 5], 'type': 'scatter', 'name': 'SF'},
                        {'x': [1, 2, 3, 4, 5], 'y': [5, 4, 3, 2, 1], 'type': 'scatter', 'name': u'Montréal'},
                    ],
                    'layout': {
                        'title': 'Dash Data Visualization',
                        'font': {
                            'size': 8
                        },
                        # legend underneath
                        'legend': {
                            'orientation': 'h',
                            'yanchor': 'bottom',
                            'y': 1.02,
                            'xanchor': 'right',
                            'x': .75,
                        }
                    }
                },
                className="w-1/2 h-full"
            ),
            
            
            

        ], className="""w-3/4 h-1/2 flex"""),
        # end of scatter plots

        # div holding one tall bar chart with many horizontal bars
        html.Div([
            dcc.Graph(
    figure={
        'data': [
            {'x': [1, 2, 3, 4, 5], 'y': [1, 2, 3, 4, 5], 'type': 'bar', 'name': 'SF', 'orientation': 'v'},
            {'x': [1, 2, 3, 4, 5], 'y': [5, 4, 3, 2, 1], 'type': 'bar', 'name': 'Montréal', 'orientation': 'v'},
            {'x': [1, 2, 3, 4, 5], 'y': [2, 3, 3, 5, 4], 'type': 'bar', 'name': 'New York', 'orientation': 'v'},
        ],
        'layout': {
            'title': 'Dash Data Visualization',
            'font': {
                'size': 8,
                # make title size small
                'title': 4
            },
            'legend': {
                'orientation': 'h',
                'yanchor': 'bottom',
                'y': 1,
                'xanchor': 'center',
                'x': .5,
            },
        }
    }, className="w-full h-full"

)

        ], className="w-3/4 h-1/2 flex justify-evenly items-center"),]
        # end of bar chart div
        
        # wraps the charts only
        , className="w-3/4 h-full flex flex-col justify-evenly items-center")
        
        # wraps everything
        ], className="w-full h-3/4 shadow-lg rounded-xl bg-white flex")
