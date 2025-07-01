from dash import Dash, html, dcc, Input, Output, State, ctx
import pandas as pd
import dash
import os

app = Dash()
stock_tickers = ['AAPL', 'GOOGL', 'MSFT', 'AMZN', 'TSLA', 'NVDA', 'META', 'JPM', 'V', 'DIS']

def generate_table_rows(num_rows=10):
    rows = []
    for i in range(num_rows):
        row = html.Tr([
            html.Td(
                dcc.Dropdown(
                    id={'type': 'ticker-dropdown', 'index': i},
                    options=[{'label': t, 'value': t} for t in stock_tickers],
                    placeholder='Select Ticker'
                )
            ),
            html.Td(
                dcc.Input(
                    id={'type': 'amount-input', 'index': i},
                    type='number',
                    placeholder='Amount in $'
                )
            )
        ])
        rows.append(row)
    return rows

app.layout = html.Div(children=[
    html.H1(children='Optimize your Portfolio',
             style={
                 'textAlign': 'center',
                 'color': "#0A0541"
             }),

    html.Div(children='''
        Make sure to input all your stocks and the quantity of it.
    '''),

    html.Table([
        html.Thead(
            html.Tr([
                html.Th('Stock Ticker'),
                html.Th('Amount ($)')
            ])
        ),
        html.Tbody(
            generate_table_rows(10)
        )
    ], style={'margin': 'auto', 'width': '50%', 'marginTop': 30}),
    html.Br(),
    html.Button("That is my portfolio", id="download-btn"),
    dcc.Download(id="download-dataframe-csv")
])

@app.callback(
    Output("download-dataframe-csv", "data"),
    Input("download-btn", "n_clicks"),
    [State({'type': 'ticker-dropdown', 'index': dash.ALL}, 'value'),
     State({'type': 'amount-input', 'index': dash.ALL}, 'value')],
    prevent_initial_call=True
)
def download_portfolio(n_clicks, tickers, amounts):
    # Filter out empty rows
    data = [
        {"Ticker": t, "Amount": a}
        for t, a in zip(tickers, amounts)
        if t and a is not None
    ]
    if not data:
        return dash.no_update
    df = pd.DataFrame(data)
    # Save a copy on the server in a specific folder
    save_path = os.path.join(os.path.dirname(__file__), "exports", "portfolio.csv")
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    df.to_csv("/Users/eloibernier/Documents/Portfolio_Optimization_Sturturing/InvestmentPortfolioAI/notebooks/DescriptiveAnalysisPortfoli.ipynb_checkpoints/exports/portfolio.csv", index=False)
    # Send file to user for download
    return dcc.send_data_frame(df.to_csv, "portfolio.csv", index=False)

if __name__ == '__main__':
    app.run(debug=True)
