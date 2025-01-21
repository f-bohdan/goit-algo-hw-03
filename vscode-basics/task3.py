import re

numbers = ["    +38(050)123-32-34",
           "     0503451234",
           "(050)8889900",
           "38050-111-22-22",
           "38050 111 22 11   ",
]

def normalize_phone(phone_number):
    phone_number = re.findall("\d+", phone_number)
    return phone_number


new_number = []
for number in numbers:
    new_number.append(normalize_phone(normalize_phone))
