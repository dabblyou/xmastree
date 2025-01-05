logo = r"""
              *

            T H E

          XMAS TREE

        * GENERATOR *

      ** by dabblyou **
"""

print(logo + "\n")

create_tree = True

while create_tree:
    char = "*"

    while True:
        try:
            size = int(input("Choose the size of your Christmas tree (between 5 and 100): "))
            if 5 <= size <= 100:
                break
            else:
                print("Please choose a number between 5 and 100.")
        except ValueError:
            print("Invalid input. Please enter a number between 5 and 100.")

    density = int(input('Do you want a dense (1) or a less dense (2) Christmas tree? Type "1" or "2". '))
    if density != 1 and density != 2:
        density = input('Invalid input. Please choose "1" (dense) or "2" (less dense). ')
    choose_char = input(
        'Would you like to choose the character that will be used to create your Christmas tree (default: *). Type "y" or "n". ').lower()

    if choose_char == "y":
        char = input("Please enter your desired character: ")

    increase_char = 1
    print("\n")

    if density == 1:
        spaces -= 1

        for _ in range(size):
            print(" " * spaces + char * increase_char)
            increase_char += 2
            spaces -= 1

    elif density == 2:
        if size % 2 == 0:
            size -= 1

        spaces = size - 1

        for _ in range(size - round(size / 2)):
            print(" " * spaces + char * increase_char + "\n")
            increase_char += 4
            spaces -= 2

    print(
        "\n⚠️ Tip: If you copy the result to use it in another program, please make sure to select a monospaced font.")

    again = input('\nDo you want to create another Christmas tree? Type "y" or "n". ')

    if again != "y":
        create_tree = False
