def main(): 
    csv_file_path = 'sp500_data.csv'
    data = []
    
    with open(csv_file_path, 'r') as file:
        for index, line in enumerate(file):
            data.append(line.strip())
            
            if index > 100:
                break
    
    if data:
        for row in data:
            print(row)

main()