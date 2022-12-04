# -*- coding: utf-8 -*-


from faker import Faker
from itertools import chain
import random
from random import sample
import json
fake = Faker()

genders = ["M","F"]
nb_persons_generated = 100
nb_artists = 40

female_names = [(fake.first_name_female(), fake.last_name()) for _ in range(nb_artists//2)]
male_names = [(fake.first_name_male(), fake.last_name()) for _ in range(nb_artists//2)]

data = {
        "persons": [{
                "name": f"{fake.first_name()} {fake.last_name()}",
                "adress": fake.address(),
                "phone": fake.ssn(),
                "email": fake.email(),
                "age": random.randint(18, 90),
                "gender": sample(genders, 1)
        } for _ in range(nb_persons_generated)],
        
        "artists": [{
                "firstname" : fn,
                "lastname" : ln,
        } for fn, ln in chain(female_names, male_names)]
     
}


with open('data.json', 'w') as f:
        f.write(json.dumps(data) + '\n')
        