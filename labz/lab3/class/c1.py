class Str:
    def __init__(self):
        pass

    def get_str(self, stroka):
        self.stroka = stroka

    def print_str(self):
        print(self.stroka.upper()) 

s = Str()
s.get_str(input())
s.print_str()
