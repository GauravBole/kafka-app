import re
from faker import Faker

fake = Faker()

def get_random_data():
    return {
        "name": fake.name(),
        "address": fake.address()
    }

if __name__ == "__main__":
    print(get_random_data)
