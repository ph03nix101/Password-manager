import json

new_data = {
    "website": {
        "email": "email",
        "password": "password",
    }
}

try:
    with open("data.json", "r", encoding='utf-8') as data_file:
        data = json.load(data_file)
#
except FileNotFoundError:
    with open("data.json", "w",encoding='utf-8') as data_file:
        json.dump(new_data, data_file, indent=4)
else:
    data.update(new_data)
    with open("data.json", "w",encoding='utf-8') as data_file:
        json.dump(data, data_file, indent=4)

# with open("data.json", "w",encoding='utf-8') as data_file:
#     json.dump(new_data, data_file, indent=4)
#
# with open("data.json", "r", encoding='utf-8') as data_file:
#     data = json.load(data_file)
#     print(data)