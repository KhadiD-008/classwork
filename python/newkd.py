

# Множества
# l = list((1, 2, 2, 3, 3, 4))
# s = set(l)
# print(s)

# li = list(s)
# print(li)

#---------

# a = {1, 2, 3, 4}
# a.remove (4)  # удалить
# a.discard (5) # удалить, если есть
# a.add (6) # добавить

#---------

# a = {1, 2, 3}
# b = {3, 4, 5}
# print (a | b) # a.union(b) - объединение
# print (a & b) # a.intersection(b) - пересечение
# print (a - b) # a.difference(b) - разница
# print (a ^ b) # a.symmetric_difference(b) - симметричная разница

#---------

# a = {1, 2, 3} #subset - подмножество
# b = {1, 2, 3, 4} #superset - надмножество

# a <= b # или a.issubset(b)
# b >= a # или b.issuperset(a)
# a == b # равно ли

#---------

# first_event = ['Lara', 'Karan', 'Josh', 'Nora', 'Rani'] 
# second_event = ['Sara', 'Elsa', 'Josh', 'Rani', 'Nick']

# new_first_event = set(first_event)
# new_second_event = set(second_event)

# print (new_first_event & new_second_event) # посетили оба мероприятия
# print (new_first_event - new_second_event) # посетили только первое мероприятие
# print (new_second_event - new_first_event) # посетили только второе мероприятие 

#---------

# first_text = input('write your first text: ') 
# second_text = input('write your second text: ')

# new_first_text = set(first_text.split(' '))
# new_second_text = set(second_text.split(' '))


# print (new_first_text & new_second_text) # посетили оба мероприятия
# print (new_first_text - new_second_text) # посетили только первое мероприятие
# print (new_second_text - new_first_text) # посетили только второе мероприятие 

#---------

# stream = open('user.txt', mode = 'r', encoding = None) 
# txtFromFile = stream.readlines()
# print(txtFromFile)

# from os import strerror
# try:
#     cnt = lcnt = ccnt = 0
#     s = open('user.txt', 'rt')
#     ch = s.read(1)
#     l = s.readline()
#     while ch != '':
#         print(ch, end= '')
#         cnt += 1
#         ch = s.read(1)
#     while l != '':
#         lcnt +=1
#         for cl in l:
#             print(cl, end= '')
#             ccnt += 1
#         l = s.readline()
#     s.close()
#     print(ccnt)
#     print(lcnt)
#     print(cnt)
#     # print('\n\nCharacters in file:', cnt)
# except IOError as e:
#     print('I/O error occurred: ', strerror(e.errno))

#---------

#1 Коешелек, который можно пополнить или снять средства с него, с возможностью отображения баланса
#2 Меню с пунктами: -Пополнить -Посмотреть -Вывести -Товары(бананы 50, яблоки 30, гранаты 80, ананасы 100)

# def walletBalance(amount):
#     wallet = open('wallet.txt', 'wt')
#     wallet.write('Баланс' + amount)
#     wallet.close()

# while(True):
#     menu = input(
#         '1. Пополнить \n'
#         '2. Посмотреть \n'
#         '3. Вывести \n'
#         '4. Товары \n'
#     )
#     if menu == '1':
#        value = input('Введите сумму: ')
#        walletBalance(value)




#---------

# def get_balance():
#     try:
#         with open('wallet.txt', 'r') as f:
#             return float(f.read().strip() or 0)
#     except FileNotFoundError:
#         return 0
    
# def update_balance(amount):
#     balance = get_balance() + amount
#     with open('wallet.txt', 'w') as f:
#         f.write(str(balance))
#     return balance

# def show_goods():
#     goods = {
#     '1': ('Бананы', 50),
#     '2': ('Яблоки', 30),
#     '3': ('Гранаты', 80),
#     '4': ('Ананасы', 100),
#     }

#     while True:
#         print('\n=== МЕНЮ ТОВАРОВ ===')
#         choice = input(
#             '1. Бананы - 50 руб\n'
#             '2. Яблоки - 30 руб\n'
#             '3. Гранаты - 80 руб\n'
#             '4. Ананасы - 100 руб\n'
#             '5. Назад\n'
#         )
        
#         choices = choice.split()
#         if not choices:
#             continue

#         main_choice = choices[0]

#         if main_choice == '5':
#             return
        
#         if main_choice in goods:
#             item_name, item_price = goods[main_choice]
#             balance = get_balance()

#             if balance >= item_price:
#                 quantity = 1
#                 if len(choices) > 1 and choices[1].isdigit():
#                     quantity = int(choices[1])

#                 total_cost = item_price * quantity

#                 if balance >= total_cost:
#                     update_balance(-total_cost)
#                     print(f'Куплено {quantity} {item_name} за {total_cost} руб!')
#                     print(f'Остаток на балансе: {get_balance()} руб')
#                 else:
#                     print('\nНедостаточно средств для покупки такого количества')
#             else:
#                 print('\nНедостаточно средств!')
#         else:
#             print('\nНекорректный выбор. Попробуйте снова')

# while True:
#     print(f'\nТекущий баланс: {get_balance()} руб')
#     choice = input(
#         '\n1. Пополнить баланс\n'
#         '2. Посмотреть баланс\n'
#         '3. Снять деньги\n'
#         '4. Показать товары\n'
#         '5. Выйти\n'
#         '>'
#     )
#     if choice == '1':
#         amount = float(input('Сколько внести? '))
#         update_balance(amount)
#         print(f'Баланс пополнен на {amount} руб!')
#     elif choice == '2':
#         print(f'\nТекущий баланс: {get_balance()} руб')
#     elif choice == '3':
#         amount = float(input('Сколько снять? '))
#         if get_balance() >= amount:
#            update_balance(-amount)
#            print(f'Снято {amount} руб!')
#         else:
#             print('Недостаточно средств!')
#     elif choice == '4':
#         show_goods()
        
#     elif choice == '5':
#         print('Выход из программы')
#         break

#---------

# 1. С помощью инпута получить значения: Имя пользователя, возраст, увлечения
# 2. Создать класс, из которого можно создавать объект на основе введенных данных
# 3. Реализовать метод класса, который будет выводить строку с описанием увлечения пользователя

# userName = input("name: ")
# userAge = input("age: ")
# userHobby = input("hobby: ")
# class UserData:
#     def __init__(self, name, age, hobby):
#         self.userName = name
#         self.userAge = age
#         self.userHobby = hobby
#     def print_hobby(self):
#         hobbies = self.userHobby.split(',')
#         hobbies = [h.strip() for h in hobbies]

#         if len(hobbies) == 1:
#             print(f"{self.userName} увлекается: {hobbies[0]}")
#         else:
#             formatted_hobbies = ", ".join(hobbies[0:-1]) + " и " + hobbies[-1]
#             print(f"{self.userName} увлекается: {formatted_hobbies}")

# user = UserData(userName, userAge, userHobby)
# user.print_hobby()

#---------

# 1. Создать класс Book
# Атрибуты: title, author, is_borrowed
# is_borrowed имеет значение по умолчанию False (книга не взята)
# Методы: borrow() - взять книгу (если она доступна)
# return_book() - вернуть книгу

# 2. Создать класс Library
# Атрибуты: 
#    -- name (название библиотеки)
#    -- books (список книг)
# Методы:
#    -- add_book(book) - добваить книгу в бибилиотеку
#    -- borrow_book(book) - взять книгу по названию
#    -- return_book(book) - вернуть книгу
#    -- list_books() - вывести список книг


class Book:
    def __init__(self, title, author, is_borrowed = False):
        self.title = title
        self.author = author
        self.is_borrowed = is_borrowed

    def borrow(self):
        if self.is_borrowed:
            return False
        self.is_borrowed = True
        return True
    
    def return_book(self):
        if not self.is_borrowed:
            return False
        self.is_borrowed = False
        return True
    
class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def borrow_book(self, title):
        for book in self.books:
            if book.title == title:
                return True
            return False
        return False
    
    def return_book(self):
        for book in self.books:
            if book.title == title:
                if book.return_book():
                    return True
                return False
        return False
    
    def list_books(self):
        print(f'Books in {self.name}:')
        for book in self.books:
            status = 'borrowed' if book.is_borrowed else 'Available'
            print(f"- '{book.title}' by {book.author} ({status})")

book1 = Book('1984', 'George Orwell')
book2 = Book('The Hobbit', 'J.R.R. Tolkien')
library = Library('Central Library')

library.add_book(book1)
library.add_book(book2)

library.borrow_book('1984')
library.borrow_book('1984')

library.return_book('1984')
library.return_book('1984')

library.list_books()

#---------