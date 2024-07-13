

while True:
    side_1 = int(input("Enter first side: "))
    side_2 = int(input("Enter second side: "))
    side_3 = int(input("Enter third side: "))

    if side_1**2 + side_2**2 == side_3**2:
        print("Yes, it is a Pythagorean Triple!")
    elif side_1**2 + side_3**2 == side_2**2:
        print("Yes, it is a Pythagorean Triple!")
    elif side_2**2 + side_3**2 == side_1**2:
        print("Yes, it is a Pythagorean Triple!")
    else:
        print("No, it is not a Pythagorean Triple.")