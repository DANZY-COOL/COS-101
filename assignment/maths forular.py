import math


def main():
    print("Welcome to the Geometry Calculator!")
    print("You can ask about the following shapes:")
    print("1. Triangle")
    print("2. Trapezium (Trapezoid)")
    print("3. Rectangle")
    print("4. Square")
    print("5. Circle")

    shape = input("Please choose a shape (1-5): ")

    if shape == '1':
        triangle_question()
    elif shape == '2':
        trapezium_question()
    elif shape == '3':
        rectangle_question()
    elif shape == '4':
        square_question()
    elif shape == '5':
        circle_question()
    else:
        print("Invalid choice. Please choose a number between 1 and 5.")


def triangle_question():
    print("You chose Triangle. What do you want to calculate?")
    print("1. Area (base, height)")
    print("2. Perimeter (all sides)")
    question = input("Please choose an option (1-2): ")

    if question == '1':
        base = float(input("Enter the base: "))
        height = float(input("Enter the height: "))
        area = 0.5 * base * height
        print(f"The area of the triangle is {area:.2f}")
    elif question == '2':
        a = float(input("Enter side a: "))
        b = float(input("Enter side b: "))
        c = float(input("Enter side c: "))
        perimeter = a + b + c
        print(f"The perimeter of the triangle is {perimeter:.2f}")
    else:
        print("Invalid option.")


def trapezium_question():
    print("You chose Trapezium (Trapezoid). What do you want to calculate?")
    print("1. Area (base1, base2, height)")
    print("2. Perimeter (all sides)")
    question = input("Please choose an option (1-2): ")

    if question == '1':
        base1 = float(input("Enter base 1: "))
        base2 = float(input("Enter base 2: "))
        height = float(input("Enter height: "))
        area = ((base1 + base2) / 2) * height
        print(f"The area of the trapezium is {area:.2f}")
    elif question == '2':
        a = float(input("Enter side a: "))
        b = float(input("Enter side b: "))
        c = float(input("Enter side c: "))
        d = float(input("Enter side d: "))
        perimeter = a + b + c + d
        print(f"The perimeter of the trapezium is {perimeter:.2f}")
    else:
        print("Invalid option.")


def rectangle_question():
    print("You chose Rectangle. What do you want to calculate?")
    print("1. Area (length, width)")
    print("2. Perimeter (length, width)")
    question = input("Please choose an option (1-2): ")

    if question == '1':
        length = float(input("Enter the length: "))
        width = float(input("Enter the width: "))
        area = length * width
        print(f"The area of the rectangle is {area:.2f}")
    elif question == '2':
        length = float(input("Enter the length: "))
        width = float(input("Enter the width: "))
        perimeter = 2 * (length + width)
        print(f"The perimeter of the rectangle is {perimeter:.2f}")
    else:
        print("Invalid option.")


def square_question():
    print("You chose Square. What do you want to calculate?")
    print("1. Area (side)")
    print("2. Perimeter (side)")
    question = input("Please choose an option (1-2): ")

    if question == '1':
        side = float(input("Enter the side length: "))
        area = side ** 2
        print(f"The area of the square is {area:.2f}")
    elif question == '2':
        side = float(input("Enter the side length: "))
        perimeter = 4 * side
        print(f"The perimeter of the square is {perimeter:.2f}")
    else:
        print("Invalid option.")


def circle_question():
    print("You chose Circle. What do you want to calculate?")
    print("1. Area (radius)")
    print("2. Circumference (radius)")
    question = input("Please choose an option (1-2): ")

    if question == '1':
        radius = float(input("Enter the radius: "))
        area = math.pi * (radius ** 2)
        print(f"The area of the circle is {area:.2f}")
    elif question == '2':
        radius = float(input("Enter the radius: "))
        circumference = 2 * math.pi * radius
        print(f"The circumference of the circle is {circumference:.2f}")
    else:
        print("Invalid option.")


if __name__ == "__main__":
    main()