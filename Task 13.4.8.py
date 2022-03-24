try:
    e = int(input("Input a whole number:"))
except ValueError as error:
    print("Incorrect number")
else:
    print("You input",e)
finally:
    print("Exit the application")

