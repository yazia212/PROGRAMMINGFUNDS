# Class for Customer
class Customer:
    def __init__(self, name, email, phone, credit_card):
        self.__name = name
        self.__email = email
        self.__phone = phone
        self.__credit_card = credit_card

    # Getters
    def get_name(self):
        return self.__name

    def get_email(self):
        return self.__email

    def get_phone(self):
        return self.__phone

    def get_credit_card(self):
        return self.__credit_card

    # Setters
    def set_name(self, name):
        self.__name = name

    def set_email(self, email):
        if "@" in email:  # basic validation
            self.__email = email
        else:
            print(f"Invalid email format for {self.__name}. Please re-enter a valid email.")

    def set_phone(self, phone):
        self.__phone = phone

    def set_credit_card(self, credit_card):
        self.__credit_card = credit_card


# Class for Room
class Room:
    def __init__(self, room_number, room_type, price, availability):
        self.__room_number = room_number
        self.__room_type = room_type
        self.__price = price
        self.__availability = availability

    # Getters
    def get_room_number(self):
        return self.__room_number

    def get_room_type(self):
        return self.__room_type

    def get_price(self):
        return self.__price

    def is_available(self):
        return self.__availability

    # Setters
    def set_room_number(self, room_number):
        self.__room_number = room_number

    def set_room_type(self, room_type):
        self.__room_type = room_type

    def set_price(self, price):
        self.__price = price

    def set_availability(self, availability):
        self.__availability = availability


# Class for Reservation
class Reservation:
    def __init__(self, dates, room_type, confirmation_number, price):
        self.__dates = dates
        self.__room_type = room_type
        self.__confirmation_number = confirmation_number
        self.__price = price

    # Getters
    def get_dates(self):
        return self.__dates

    def get_room_type(self):
        return self.__room_type

    def get_confirmation_number(self):
        return self.__confirmation_number

    def get_price(self):
        return self.__price

    # Setters
    def set_dates(self, dates):
        self.__dates = dates

    def set_room_type(self, room_type):
        self.__room_type = room_type

    def set_confirmation_number(self, confirmation_number):
        self.__confirmation_number = confirmation_number

    def set_price(self, price):
        self.__price = price


# Class for Payment
class Payment:
    def __init__(self, method, total_amount, status):
        self.__method = method
        self.__total_amount = total_amount
        self.__status = status

    # Getters
    def get_method(self):
        return self.__method

    def get_total_amount(self):
        return self.__total_amount

    def get_status(self):
        return self.__status

    # Setters
    def set_method(self, method):
        self.__method = method

    def set_total_amount(self, total_amount):
        self.__total_amount = total_amount

    def set_status(self, status):
        self.__status = status

    # Method to process payment
    def process_payment(self):
        if self.__status == "pending":
            self.__status = "completed"
            print("Payment successful.")
        else:
            print("Payment already processed.")


# Testing the classes with updated customer names and invalid cases

# Valid Customer (Good case)
customer1 = Customer("Sara Ahmed", "sara@gmail.com", "1234567890", "1111-2222-3333-4444")
customer2 = Customer("Ali Mohamed", "ali@yahoo.com", "0987654321", "5555-6666-7777-8888")
customer3 = Customer("Alyia Saif", "alyia@icloud.com", "9876543210", "9999-0000-1111-2222")

# Test for invalid email (Bad case)
customer1.set_email("saragmail.com")  # Invalid email

# Print valid outputs
print(f"Customer Name: {customer1.get_name()}, Email: {customer1.get_email()}")
print(f"Customer Name: {customer2.get_name()}, Email: {customer2.get_email()}")
print(f"Customer Name: {customer3.get_name()}, Email: {customer3.get_email()}")

# Valid Room (Good case)
room1 = Room(101, "Single", 100.0, True)
print(f"Room Number: {room1.get_room_number()}, Type: {room1.get_room_type()}, Price: {room1.get_price()}")

# Reservation (Good case)
reservation1 = Reservation("2023-09-30", "Single", 12345, 100.0)
print(f"Reservation Confirmation Number: {reservation1.get_confirmation_number()}, Total Price: {reservation1.get_price()}")

# Payment (Good and Bad case)
payment1 = Payment("Credit Card", 100.0, "pending")
payment1.process_payment()  # Should succeed
payment1.process_payment()  # Already processed (Bad case)
