class User:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def __str__(self) -> str:
        return f"Меня зовут {self.name}, мне {self.age} года"


a = User(name="Соня", age=23)
b = User(name="Денис", age=23)

print(b)