from data.data import User
from faker import Faker

faker_en = Faker('en_US')
Faker.seed()


def generated_user():
    yield User(
        full_name=faker_en.first_name() + " " +faker_en.last_name(),
        email=faker_en.email(),
        current_address=faker_en.address()
    )
