customer = {
    "name": 'John Smith',
    "age": 30,
    "is_verified": True
}

customer["name"] = "Will Smith"
# normal print
print(customer["name"])

# using the get method for keys
# print(customer.get("name"))

# keys that do are not in the dictionary
# print(customer.get("birthdate", "January 1, 2020"))
