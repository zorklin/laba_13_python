
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


# Функція читання файлу csv та перезапису його у json з додаванням даних - Плутенко Олексій
def convert_csv_to_json_Plutenko(csv_file, json_file):
    try:
        with open(csv_file, mode = 'r', encoding='utf-8') as file:
            output_data = csv.DictReader(file)
            rows = {row["Name"]: {"Age": row["Age"], "City": row["City"]} for row in output_data}
    except IOError as e:
        print(f"Помилка при обробці {csv_file}: {e}")
    except Exception as e:
        print(f"Помилка при обробці {csv_file}: {e}")

    while True:
        temp = input("Додати користувачів?\n1 - Так\n0 - Ні\n")
        if temp == '1':
            Name = input("Введіть ім'я особи: ")
            Age = input("Введіть вік особи: ")
            City = input("Введіть місто, в якому проживає особа: ")
            rows[Name] = {"Age": Age, "City": City}
        elif temp == '0':
            break
        else:
            print("Невірний вибір, спробуйте ще раз.")

    try:
        with open(json_file, mode = 'w', encoding='utf-8') as file:
            json.dump(rows, file, ensure_ascii=False, indent=4)
    except IOError as e:
        print(f"Помилка при обробці {json_file}: {e}")
    except Exception as e:
        print(f"Помилка при обробці {json_file}: {e}")

# Функція читає .json файл та конвертує вміст у .csv файл - Попов Максим
def convert_json_csv_Popov(jname, cname):
    try:
        with open(jname, "r") as jfile:
            jdata = json.load(jfile)
            jlist = []
            for name in jdata.keys():
                jdata[name]["Name"] = name
                jlist.append(jdata[name])
            print(jlist)

    except:
        print("Файл {} не вдалося відкрити".format(jname))
    try:
        with open(cname, "w") as cfile:
            cdata = csv.DictWriter(cfile, fieldnames=jlist[0].keys())
            cdata.writeheader()
            cdata.writerows(jlist)
            print("Дані переписані")
    except IOError:
        print("Файл {} не вдалося відкрити".format(cname))

# Функція читання файлу csv та перезапису його у json з додаванням даних. Гончарова Дарина
def convert_csv_to_json_Honcharova(csv_file, json_file):
    try:
        with open(csv_file, mode = 'r', encoding='utf-8') as file:
            output_data = csv.DictReader(file)
            rows = {row["Name"]: {"Age": row["Age"], "City": row["City"]} for row in output_data}
    except IOError as e:
        print(f"Помилка при обробці {csv_file}: {e}")
    except Exception as e:
        print(f"Помилка при обробці {csv_file}: {e}")

    while True:
        temp = input("Додати користувачів?\n1 - Так\n0 - Ні\n")
        if temp == '1':
            Name = input("Введіть ім'я особи: ")
            Age = input("Введіть вік особи: ")
            City = input("Введіть місто, в якому проживає особа: ")
            rows[Name] = {"Age": Age, "City": City}
        elif temp == '0':
            break
        else:
            print("Невірний вибір, спробуйте ще раз.")

    try:
        with open(json_file, mode = 'w', encoding='utf-8') as file:
            json.dump(rows, file, ensure_ascii=False, indent=4)
    except IOError as e:
        print(f"Помилка при обробці {json_file}: {e}")
    except Exception as e:
        print(f"Помилка при обробці {json_file}: {e}")


dictionary_data = [
    {"Name": "Ivan", "Age": 19, "City": "Sumy"},
    {"Name": "Dima", "Age": 18, "City": "Lutsk"},
    {"Name": "Mark", "Age": 21, "City": "Lviv"}
]

csv_name = 'data.csv'
json_name = 'data.json'

commands = "1. Записати заготовлені дані до .csv файлу\n\
2. Переписати вміст .csv файлу в .json файл\n\
3. Переписати вміст .json файлу в .csv файл з додаванням даних\n\
4. Переписати вміст .csv файлу в .json файл з додаванням даних\n\
5. Переписати вміст .json файлу в .csv файл\n\
6. Переписати вміст .csv файлу в .json файл з додаванням нових даних."

print("Доступні такі команди: \n" + commands)
while True:
    set = int(input("Введіть індекс необхідної команди: "))
    if set == 1:
        write_to_csv(dictionary_data, csv_name)
    elif set == 2:
        convert_csv_to_json(csv_name, json_name)
    elif set == 3:
        convert_json_csv(dictionary_data ,json_name,csv_name)
    elif set == 4:
        convert_csv_to_json_Plutenko(csv_name, json_name)
    elif set == 5:
        convert_json_csv_Popov(json_name, csv_name)
    elif set == 6:
        convert_csv_to_json_Honcharova(csv_name, json_name)
    elif set == 0:
        print("Завершення...")
        break
    else:
        print("Невідома операція!")
