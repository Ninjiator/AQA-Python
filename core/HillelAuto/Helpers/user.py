from faker import Faker

class TestUser:

    def __init__(self):
        self.faker = Faker()
        self.name = self.faker.first_name()
        self.last_name = self.faker.last_name()
        self.mail = self.name + self.last_name + "@gmail.com"
        self.password = self.faker.password()