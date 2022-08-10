# Keyword Variable length argument is an argument that can accept any number of values in key-value pair.
# This argument is written with ** symbol. It stores all the values in "Dictionary" in form of key-value pair.

def details(**detail):
    first_name = detail['first_name']
    last_name = detail['last_name']
    age = detail['age']
    phone = detail['phone']

    print(f"First_name is: {first_name}, Last_name is:{last_name}, Age is: {age}, Phone is:{phone}")


details(first_name="john", last_name="Doe", age=32, phone=1234567890)
details(first_name="john", last_name="Doe", age=32, phone=1234567890, country="USA")


def details2(**kwargs):
    for k, v in kwargs.items():
        print("%s=%s" % (k, v))


details2(name="abhishek", firstclass=23)

names = ['Bangalore', 'Abhishek', 'India']
print(names[-1][-2])
