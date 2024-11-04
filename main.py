import csv
import json

def write_to_csv(data, file_name):
    try:
        with open(file_name, mode = 'w', newline = '') as file:
            input_data = csv.DictWriter(file, fieldnames = data[0].keys())
            input_data.writeheader()
            input_data.writerows(data)
    except IOError as err:
        print(f"error with file: {err}")
    except Exception as err:
        print(f"error: {err}")

def convert_csv_to_json(csv_file, json_file):
    try:
        with open(csv_file, mode = 'r') as file:
            output_data = csv.DictReader(file)
            rows = {row["Name"]: {"Age": row["Age"], "City": row["City"]} for row in output_data}

        with open(json_file, mode = 'w') as file:
            json.dump(rows, file, indent = 4)
    except IOError as err:
        print(f"Error with file: {err}")
    except Exception as err:
        print(f"Error: {err}")

dictionary_data = [
    {"Name": "Ivan", "Age": 19, "City": "Sumy"},
    {"Name": "Dima", "Age": 18, "City": "Lutsk"},
    {"Name": "Mark", "Age": 21, "City": "Lviv"}
]

csv_name = 'data.csv'
json_name = 'data.json'

write_to_csv(dictionary_data, csv_name)
convert_csv_to_json(csv_name, json_name)
