# Створіть клас Human, який міститиме інформацію
# про людину.
# За допомогою механізму успадкування реалізуйте
# клас Builder (містить інформацію про будівельника),
# клас Sailor (містить інформацію про моряка), клас Pilot
# (містить інформацію про льотчика).
# Кожен із класів має містити необхідні для роботи
# методи.

class Human:
    def __init__(self, name: str, age: int, sex: str) -> None:
        self._name = name
        self._age = age
        self._sex = sex
    
    def get_name(self):
        return self._name
    def set_name(self, name):
        self._name = name

    def get_age(self):
        return self._age
    def set_age(self, age):
        self._age = age
    
    def get_sex(self):
        return self._sex
    def set_sex(self, sex):
        self._sex = sex

    def __str__(self) -> str:
        return f"Name: {self._name}, Age: {self._age}, Sex: {self._sex}"


class Builder(Human):
    def __init__(self, name: str, age: int, sex: str, profession: str) -> None:
        super().__init__(name, age, sex)
        self._rank = profession
    
    def get_profession(self) -> str:
        return self._rank
    def set_profession(self, profession) -> None:
        self._rank = profession
    
    def __str__(self) -> str:
        human_info = super().__str__()
        return f"{human_info}, Profession: {self._rank}"

class Sailor(Human):
    def __init__(self, name: str, age: int, sex: str, rank: str) -> None:
        super().__init__(name, age, sex)
        self._rank = rank
    
    def get_rank(self) -> str:
        return self._rank
    def set_rank(self, rank) -> None:
        self._rank = rank
    
    def __str__(self) -> str:
        human_info = super().__str__()
        return f"{human_info}, Rank: {self._rank}"

builder = Builder(name="John", age=30, sex="Male", profession="Engineer")
print(builder)

sailor = Sailor(name="Alice", age=25, sex="Female", rank="Captain")
print(sailor)
