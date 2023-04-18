my_dict = {"name": "abhishek", "age": 33, "occupation": "IT"}


def search(dict, value):
    for key in dict:
        if dict[key] == value:
            print(key, ":", value)
    print("Key-Value Pair Doesn't Exists")


search(my_dict, "abhishek")
