from nameko.rpc import rpc
from faker import Faker


class PeopleListService:
    name = 'peoplelist'

    @rpc
    def populate(self, number=20):
        names = []
        fake = Faker()
        for _ in range(number):
            names.append(fake.name())
        return names
