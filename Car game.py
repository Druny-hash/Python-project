command = ""
while command != "quite":
    command = input("> ") .lower()
    if command == "start":
        print("The car is started.")
    elif command == "stop":
        print("The car is stopped.")
    elif command == "help":
        print("""
              
             1. start - To start the car
              
             2. stop - To stop the car
              
             3. quit - To quit 

               """)
    elif command == "quit":
        break

    else:
        print("Invalid command. Type 'help' for a list of commands.")
