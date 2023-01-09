class Rocket:
    def __init__(self, mark, destination, engines):
        self.mark = mark
        self.destination = destination
        self.engines = [engines]

    def launch(self):
        return f'Rocket {self.mark} has been launched to the Mars.'

    def getAbsolutePower(self):
        return sum([i.getPower() for i in self.engines])

    def addEngine(self, newEngine):
        self.engines.append(newEngine)


class Engine:
    def __init__(self, weight, e_class):
        self.weight = weight
        self.e_class = e_class

    def getPower(self):
        return int(self.weight * 9.81)
        
    def getClass(self):
        return self.e_class

def main():
    n = int(input())
    quazar_13 = Engine(12500, 'Quazar')
    R1 = Rocket('Falcon-1', 'Mars', quazar_13)
    for i in range(n):
        command = input()
        if command == 'Launch':
            print(R1.launch())
        elif command == 'getAbsolutePower':
            print(R1.getAbsolutePower())
        elif command == 'addEngine':
            quazar_14 = Engine(25000, 'QuazarL')
            R1.addEngine(quazar_14)
        elif command == 'showEngineClasses':
            print(f'Engines of {R1.mark} are:')
            for i in R1.engines:
                print(i.getClass())

if __name__ == '__main__':
    main()