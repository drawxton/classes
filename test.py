emptydb = []
class User:
    def __init__(self, name: str, age: int, gender: str, country: str):
        self.name = name.title().strip()
        self.age = age
        self.gender = gender.title().strip()
        self.country = country.title().strip()
    
    

emptydb.append(User(name="      Roxton    ", age=23, gender="M   ", country="India"))

print(emptydb[0])