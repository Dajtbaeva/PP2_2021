import os

while True:
    command = input()
    if command == 'cd':
        kuda = input()
        if os.path.isdir(kuda) and os.path.exists(kuda):
            os.chdir(kuda)
            print('Done')
        else:
            print('Net takogo')
    elif command == 'dir':
        print(os.listdir(os.getcwd()), sep = '\n')
    elif command == 'gde':
        print(f'The current directory is: {os.getcwd()}')
    elif command == 'create dir':
        name = input()
        if os.path.exists(name):
            print("Uzhe est'")
        else:
            f = open(name, 'w')
            s = input("Chto napisat'?\n")
            f.write(s)
            f.close()
            print(f'Created{name}')
    elif command == 'del':
        chto = input()
        if os.path.exists(chto):
            os.remove(chto)
            print('Done')
    elif command == 'exit':
        break