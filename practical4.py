print("***********Traffic Signal Simulation System***********")


signal = input("Enter a signal color: ").lower().strip()


if signal == "red":
    print("Signal is red")
    print("Action: Stop")

elif signal == "yellow":
    print("Signal is yellow")
    print("Action: Get ready")

elif signal == "green":
    print("Signal is green")
    print("Action: Go")

else:
    
    print(f"Invalid color: '{signal}'")
    print("Please enter red, yellow, or green.")