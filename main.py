class Node:
    def __init__(self, phone_num: int, name: str, address: str, surname: str):
        self.phone_num = phone_num
        self.name = name
        self.address = address
        self.surname = surname
        self.next = None


class CircularList:
    def __init__(self):
        self.head = None

    def push(self, phone_num: int, full_name: str, address: str, surname: str):
        node = Node(phone_num, full_name, address, surname)
        temp = self.head
        node.next = self.head
        if self.head is not None:
            while temp.next != self.head:
                temp = temp.next
            temp.next = node
        else:
            node.next = node
        self.head = node

    def pop_back(self):
        if self.head.next == self.head:
            self.head.next = None
            self.head = None
            return
        last_node = self.head
        previous = last_node.next
        while previous.next != last_node:
            previous = previous.next

        previous.next = last_node.next
        self.head = previous
        last_node.next = None

    def print_list(self):
        temp = self.head
        print(f"|| Phone number: {temp.phone_num}\n"
              f"|| Name: {temp.name}\n"
              f"|| Surname: {temp.surname}\n"
              f"|| Address: {temp.address}\n"
              f"==============================================")
        temp = temp.next
        while temp != self.head:
            print(f"|| Phone number: {temp.phone_num}\n"
                  f"|| Name: {temp.name}\n"
                  f"|| Surname: {temp.surname}\n"
                  f"|| Address: {temp.address}\n"
                  f"==============================================")
            temp = temp.next

    def add_by_phone_number_rise(self, node):
        current = self.head

        if current is None:
            node.next = node
            self.head = node

        elif current.phone_num >= node.phone_num:
            while current.next != self.head:
                current = current.next
            current.next = node
            node.next = self.head
            self.head = node

        else:
            while current.next != self.head and current.next.phone_num < node.phone_num:
                current = current.next
            node.next = current.next
            current.next = node

    def find_by_surname(self, searched_surname: str):
        current = self.head
        while True:
            if current.surname == searched_surname:
                print(f"|| Phone number: {current.phone_num}\n"
                      f"|| Name: {current.name}\n"
                      f"|| Surname: {current.surname}\n"
                      f"|| Address: {current.address}\n"
                      f"==============================================")
            current = current.next
            if current == self.head:
                break


customers_list = CircularList()

Subscriber1 = Node(999, "Nine", "somewhere in Ukraine", "Ninetier")
Subscriber2 = Node(1, "One and Only", "always in place First", "Uno")
Subscriber3 = Node(34814, "IUTVUK", "somewhere in Randomland", "Random")
customers_list.add_by_phone_number_rise(Subscriber1)
customers_list.add_by_phone_number_rise(Subscriber2)
customers_list.add_by_phone_number_rise(Subscriber3)
print("\n-- List of customers: ")
customers_list.print_list()
customers_list.push(908, "THE NAME", "THE LOCATION", "THE SURNAME")
print("\n-- List of customers: ")
customers_list.print_list()
print("\n-- List of customers: ")
customers_list.pop_back()
customers_list.print_list()
print("\n-- Searching for Uno: ")
customers_list.find_by_surname("Uno")
