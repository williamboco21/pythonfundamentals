command = ""
started = False
stopped = False
while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("The car has already been started. Please stop the car.")
        else:
            print("Car started...Ready to go!")
            started = True
    elif command == "stop":
        if stopped:
            print("The car has already been stopped. Please stop the car.")
        else:
            print("Car stopped.")
            stopped = True
            started = False
    elif command == "help":
        print(f"start - to start the car\n"
              f"stop - to stop the car\n"
              f"quit - to exit")
    elif command == "quit":
        break
    else:
        print("I don't understand that")

