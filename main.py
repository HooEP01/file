import pandas as pd
import matplotlib.pyplot as plt

data = []

def store(): 
    csv_file_path = 'sp500_data.csv'
    
    with open(csv_file_path, 'r') as file:
        for index, line in enumerate(file):
            data.append(line.strip())
            
            if index > 100:
                break
    
    if data:
        for row in data:
            print(row)

def main():
    csv_file_path = 'sp500_data.csv'
    df = pd.read_csv(csv_file_path)

    df['Date'] = pd.to_datetime(df['Date'])

    # Plotting
    plt.figure(figsize=(12.5, 4.5))
    plt.plot(df['Date'], df['Open'], label='Open')
    plt.plot(df['Date'], df['High'], label='High')
    plt.plot(df['Date'], df['Low'], label='Low')
    plt.plot(df['Date'], df['Close'], label='Close')
    plt.plot(df['Date'], df['Adj Close'], label='Adj Close')
    plt.plot(df['Date'], df['Volume'], label='Volume')

    # Add legend
    plt.legend()

    # Add title and labels
    plt.title('S&P 500 Data Overview')
    plt.xlabel('Date')
    plt.ylabel('Value')

    # Show plot
    plt.show()

main()