import fetch_data
import process_data
import report_results

input_file = "/Users/consultadd/Desktop/python_training/file_handling/assign1/students.csv"
output_file = "/Users/consultadd/Desktop/python_training/file_handling/assign1/output.csv"


data = fetch_data.read_csv(input_file)

processed_data = process_data.calculate_total_marks(data)

report_results.save_to_csv(processed_data, output_file)

print("Processing complete! Check output.csv")