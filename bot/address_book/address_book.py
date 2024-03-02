from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, field):
        super().__init__(field)

class Phone(Field):
    def __init__(self, field):
        super().__init__(field)

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        if (len(phone) == 10 and phone.isnumeric()):
            self.phones.append(Phone(phone))
        else:
            raise ValueError(f"Phone number: {phone} is wrong")

    def remove_phone(self, phone):
        self.phones.remove[phone]
    
    def edit_phone(self, phone, new_phone):
        for i, item in enumerate(self.phones):
            if item.value == phone:
                self.phones[i] = Phone(new_phone)

    def find_phone(self, phone):
        for item in self.phones:
            if item.value == phone:
                return item.value
        return None


    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    
    def add_record(self, record: Record):
        self.data[record.name.value] = record

    def find(self, name) -> Record:
        return self.data[name]
    
    def delete(self, name):
        self.data.pop(name)



def main():
      # Створення нової адресної книги
    book = AddressBook()

    # Створення запису для John

    john_record = Record("John")
    add_phone(john_record, "123456890")
    add_phone(john_record, "5555555555")

    # Додавання запису John до адресної книги
    book.add_record(john_record)

    # Створення та додавання нового запису для Jane
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    # Виведення всіх записів у книзі
    for _, record in book.data.items():
        print(record)

    # Знаходження та редагування телефону для John
    john = book.find("John")
    john.edit_phone("1234567890", "1112223333")

    print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

    # Пошук конкретного телефону у записі John
    found_phone = john.find_phone("5555555555")
    print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

    # Видалення запису Jane
    book.delete("Jane")

def add_phone(record: Record, phone: str):
    try:
        record.add_phone(phone)
    except ValueError as error:
        print(error)

if __name__ == "__main__":
    main()


