import fetch_data
import process_data
import analyze_data
import visualize_data

def main():
    # Step 1: Fetch data
    fetch_data.fetch_ginger_data()
    fetch_data.fetch_maize_data()
    fetch_data.fetch_rice_data()
    fetch_data.fetch_cocoa_data()

    # Step 2: Process the data
    process_data.process_ginger_data()
    process_data.process_maize_data()
    process_data.process_rice_data()
    process_data.process_cocoa_data()

    # Step 3: Analyze the data
    analyze_data.analyze_price_trends()

    # Step 4: Visualize the data
    visualize_data.plot_price_trends()

if __name__ == "__main__":
    main()
