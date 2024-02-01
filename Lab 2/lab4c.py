import math

def circle_area(radius):
    """
    Calculate the area of a circle given its radius.

    :param radius: The radius of the circle.
    :type radius: int
    :return: The area of the circle.
    :rtype: float
    """
    return math.pi * (radius ** 2)

if __name__ == "__main__":
    print("Enter integers between 0 and 1999 (Press Enter to stop):")

    while True:
        user_input = input("Enter an integer: ")

        if user_input == "":
            print("Program was cancelled.")
            break

        try:
            radius = int(user_input)

            if 0 <= radius <= 1999:
                area = circle_area(radius)
                print(f"Radius: {radius}, Area: {area:.2f}")
            else:
                print("Error: Input out of bounds (0-1999)")

        except ValueError:
            print("Error: Not a valid integer")
