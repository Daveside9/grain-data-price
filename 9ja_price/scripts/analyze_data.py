import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
filename = "commodity_prices_20250115120000.csv"  # Replace with your CSV filename
df = pd.read_csv(filename)

# Convert date to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Plot price trends
def plot_trends(data):
    plt.figure(figsize=(10, 6))
    for commodity in data['Commodity'].unique():
        subset = data[data['Commodity'] == commodity]
        plt.plot(subset['Date'], subset['Price'], label=commodity)

    plt.title('Price Trends of Commodities')
    plt.xlabel('Date')
    plt.ylabel('Price (NGN)')
    plt.legend()
    plt.grid(True)
    plt.show()

# Run the analysis
if __name__ == '__main__':
    plot_trends(df)
