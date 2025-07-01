############################# W E B S I T E   A S S E T S   D A T A #############################


# Set global variables for the portfolio analysis
import pandas as pd

# Ensure the file exists and print a message if not
import os
csv_path = "/Users/eloibernier/Documents/Portfolio_Optimization_Sturturing/InvestmentPortfolioAI/notebooks/DescriptiveAnalysisPortfoli.ipynb_checkpoints/exports/portfolio.csv"

currentportfolio = pd.read_csv(csv_path)
print(currentportfolio)

# Extract the columns
keys = currentportfolio['Ticker']
values = currentportfolio['Amount']

# Create the dictionary
Asset_Amounts = dict(zip(keys, values))

print(Asset_Amounts)


############################# M A I N   Y F   V A R I A B L E S #############################

start = "2012-01-01"
end = "2024-12-31"
frequency = "1d"

day_bought = "2019-12-02"
Analysis_from = '2019-12-02'

#############################

# Define the amount invested in each asset
#Asset_Amounts = {
#    "AAPL": 30000,
#    "GOOGL": 3000,
#    "AMZN": 4000,
#    "MSFT": 3500,
#    "NFLX": 2000,
#    "PLTR": 2000,
#    "DOL": 4500,
#   "V": 3000,
#   "QQQ": 0,
#   "SPY": 0,
 #   "AIR": 0
#}


#Define the amount invested in each asset
OptimizedPortfolio = {
    "AAPL": 1500,
    "GOOGL": 3000,
    "AMZN": 4000,
    "MSFT": 3500,
    "NFLX": 2000,
    "PLTR": 20000,
    "DOL": 4500,
    "V": 50000,
    "QQQ": 0,
    "SPY": 5000,
    "AIR":0
}


