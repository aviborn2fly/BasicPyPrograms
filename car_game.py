
command = ""
car_status = False
while 1:
    command = input('>').lower()
    if command == 'quit':
        break
    elif command == 'start':
        if not car_status:
            print("Car started...Ready to go!")
            car_status = True
        else:
            print("Car is already started!")
    elif command == 'stop':
        if car_status:
            print("Car stopped.")
            car_status = False
        else:
            print("Car already stopped!")
    elif command == 'help':
        print('''
start - to start the car
stop - to stop the car
quit - to exit
        ''')
    else:
        print("I don't understand that!")
