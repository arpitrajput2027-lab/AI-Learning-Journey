color = input("Enter the Color :")

match color:
    case "green":
        print("Go")
    case "red":
        print("Stop")
    case "yellow":
        print("Wait")
    case _:
        print("Invalid Color ")