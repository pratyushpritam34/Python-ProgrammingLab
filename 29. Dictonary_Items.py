def dictionary_items(dictionary):
    for key, value in dictionary.items():
        print(f"{key}: {value}")

my_dict = {"name": "Mohan", "age": 90, "city": "Panchanpur", "Work": "Rest", "Salary": 50000}
print("Dictionary items are:")
dictionary_items(my_dict)
