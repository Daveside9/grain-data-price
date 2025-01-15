import matplotlib.pyplot as plt
import seaborn as sns

def plot_price_trends():
    ginger_avg, maize_avg, rice_avg, cocoa_avg = analyze_data.analyze_price_trends()

    # Set up the plot style
    sns.set(style="darkgrid")

    # Create subplots
    fig, ax = plt.subplots(figsize=(10, 6))

    # Plot the data
    ax.plot(ginger_avg.index, ginger_avg.values, label='Ginger', color='green')
    ax.plot(maize_avg.index, maize_avg.values, label='Maize', color='yellow')
    ax.plot(rice_avg.index, rice_avg.values, label='Rice', color='brown')
    ax.plot(cocoa_avg.index, cocoa_avg.values, label='Cocoa', color='purple')

    # Add labels and title
    ax.set_xlabel('Month')
    ax.set_ylabel('Average Price (NGN)')
    ax.set_title('Price Trends of Crops in Nigeria')
    ax.legend()

    # Save and show the plot
    plt.savefig('outputs/price_trends.png')
    plt.show()
    print("Price trends visualized.")
