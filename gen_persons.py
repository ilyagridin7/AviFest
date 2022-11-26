# -*- coding: utf-8 -*-


from faker import Faker
import random
from random import sample
import json
fake = Faker()

list1 = ["M","F"]

a = [{
        "name": fake.name(),
        "adress": fake.address(),
        "phone": fake.ssn(),
        "email": fake.email(),
        "age": random.randint(18, 90),
        "sexe": sample(list1, 1)
} for _ in range(100)]

with open('persons.json', 'w') as f:
        f.write(json.dumps(a) + '\n')
        