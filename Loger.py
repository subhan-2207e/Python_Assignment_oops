class Logger:
    def __init__(self):
        print("Logger object created !")

    def __del__(self):
        print("Logger object destroyed !")

l1 = Logger()

del l1
print(l1)