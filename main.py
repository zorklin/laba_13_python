import csv
import json

def write_to_csv(data, file_name):
    try:
        with open(file_name, mode = 'w', newline = '') as file:
            input_data = csv.DictWriter(file, fieldnames = data[0].keys())
            input_data.writeheader()
            input_data.writerows(data)
    except IOError as err:
        print(f"err with file: {err}")
    except Exception as err:
        print(f"err: {err}")

def convert_csv_to_json(csv_file, json_file):
    try:
        with open(csv_file, mode = 'r') as file:
            output_data = csv.DictReader(file)
            rows = [row for row in output_data]

        with open(json_file, mode = 'w') as file:
            json.dump(rows, file, indent = 4)
    except IOError as err:
        print(f"err with file: {err}")
    except Exception as err:
        print(f"err: {err}")

# Функція читання файлу json та перезапису його у csv з додаванням строки - Павло Меша
def convert_json_csv(data, f_json, f_csv):
    jsonData = json.dumps(dictionary_data)
    try:
        with open(f_json, "rt") as file:
            data = json.loads(jsonData)
    except IOError as err:
        print(f"err with file: {err}")
    except Exception as err:
        print(f"err: {err}")
    write_to_csv(data, f_csv)
    print("Add ")
    Name = input("Name:")
    Age = input("Age:")
    City = input("City:")
    try:
        with open(f_csv,"a") as csvfile:
            writer = csv.writer(csvfile, delimiter = ",")
            writer.writerow((Name, Age, City))
            csvfile.close
    except IOError as err:
        print(f"err with file: {err}")
    except Exception as err:
        print(f"err: {err}")


dictionary_data = [
    {"Name": "Ivan", "Age": 19, "City": "Sumy"},
    {"Name": "Dima", "Age": 18, "City": "Lutsk"},
    {"Name": "Mark", "Age": 21, "City": "Lviv"}
]

csv_name = 'data.csv'
json_name = 'data.json'

write_to_csv(dictionary_data, csv_name)
convert_csv_to_json(csv_name, json_name)
convert_json_csv(dictionary_data ,json_name,csv_name)
