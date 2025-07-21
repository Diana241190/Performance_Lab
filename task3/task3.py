import json
import io
import os
import sys


with open(sys.argv[1], 'r') as file:
    tests_data = json.load(file)

with open(sys.argv[2], 'r') as file:
    values_data = json.load(file)


test_dict = tests_data["tests"]
values_dict_lst = values_data["values"]
value_dict_final = {item["id"]: item["value"] for item in values_dict_lst}

def fill_tests_values(test_dict, value_dict):
    for element in test_dict:
        element_id = element.get("id")
        if element_id in value_dict:
            element["value"] = value_dict[element_id]
        if "values" in element:
            fill_tests_values(element["values"], value_dict)
    return test_dict

data = fill_tests_values(test_dict, value_dict_final)
with open(sys.argv[3], 'w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)




