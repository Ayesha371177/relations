class Printer:
    def print_message(self):
        print("Printing Document")

class Computer:
    def use_printer(self):
        p = Printer()      
        p.print_message()

c = Computer()

c.use_printer()