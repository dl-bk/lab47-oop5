# Створіть клас Passport (паспорт), який міститиме
# паспортну інформацію про громадянина заданої країни.
# За допомогою механізму успадкування реалізуйте
# клас ForeignPassport (закордонний паспорт), похідний
# від Passport.
# Нагадаємо, що закордонний паспорт містить, крім
# паспортних даних, дані про візи і номер закордонного
# паспорта.
# Кожен із класів має містити необхідні методи.

class Passport:
    def __init__(self, name, country, id) -> None:
        self._name = name
        self._country = country
        self._id = id
    
    def __str__(self):
        return f"Passport Information:\nName: {self._name}\nID: {self._id}\nCountry: {self._country}"

    def get_name(self):
        return self._name
    def set_name(self, name):
        self._name = name
    
    def get_country(self):
        return self._country

    
    def get_id(self):
        return self._id
    

class ForeignPassport(Passport):
    def __init__(self, name, country, id, pass_num) -> None:
        super().__init__(name, country, id)
        self._passnum = pass_num
        self._visas = []

    def add_visa(self, visa):
        self._visas.append(visa)
    
    def display_info(self):
        super().__str__()
        print(f"Foreign Passport Information:\nPassport Number: {self._passnum}")
        if self._visas:
            for visa in self._visas:
                print(visa)

passport = Passport("John Doe", "123456789", "USA")
print(passport)

foreign_passport = ForeignPassport("Jane Doe", "987654321", "USA", "ABC123456")
foreign_passport.add_visa("Tourist Visa - Country A")
foreign_passport.add_visa("Business Visa - Country B")
foreign_passport.display_info()