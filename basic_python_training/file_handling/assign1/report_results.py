import csv

def save_to_csv(data, output_file):
    """Writes processed data with total marks into a new CSV file."""
    fieldnames = data[0].keys()
    
    with open(output_file, mode="w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)
