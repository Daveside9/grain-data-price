from flask import Flask, render_template
import csv
import os

app = Flask(__name__)

# Utility function to read CSV data
def read_csv(file_name):
    data = []
    if os.path.exists(file_name):  # Check if the file exists
        with open(file_name, mode='r', newline='', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                data.append(row)
    else:
        print(f"File {file_name} does not exist.")  # Debugging message
    return data

@app.route('/')
def welcome():
    return "Welcome to the Grain Data Price API in Nigeria!"

@app.route('/grains')
def grains():
    # Load data from CSV files
    grains_data = []
    for grain_file in ['rice_data.csv', 'ginger_data.csv', 'maize_data.csv', 'cocoa_data.csv']:
        grain_type = grain_file.split('_')[0].capitalize()  # Extract grain type (e.g., "Rice")
        grain_rows = read_csv(os.path.join('data', grain_file))
        for row in grain_rows:
            row['Grain Type'] = grain_type  # Add the grain type as a new column
        grains_data.extend(grain_rows)

    # Render data in a table using a template
    return render_template('grains.html', grains=grains_data)

if __name__ == '__main__':
    app.run(debug=True)
