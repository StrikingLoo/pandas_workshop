import pandas as pd
import random

names = ["Albert","John","Richard","Henry","William"]
surnames = ["Goodman","Black","White","Green","Joneson"]
salaries = [500*random.randint(10,30) for _ in range(10)]

def generate_random_person(names, surnames, salaries):
    return {"name":random.sample(names,1)[0],
            "surname":random.sample(surnames,1)[0],
            "salary":random.sample(salaries,1)[0]}
def generate_people(k):
    return [generate_random_person(names, surnames, salaries) for _ in range(k)]

df = pd.DataFrame(generate_people(50),columns=["name","surname","salary"])
df.to_csv("random_people.csv")

