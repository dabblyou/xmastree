logo = r"""
              *

            T H E

          XMAS TREE

        * GENERATOR *

      **** by  wmd ****
"""
print(logo + "\n")

create_tree = True

while create_tree:
    char = "*"

    while True:
        try:
            size = int(input("Choose the size of your Christmas tree (between 3 and 100): "))
            if 3 <= size <= 100:
                break
            else:
                print("Please choose a number between 3 and 100.")
        except ValueError:
            print("Invalid input. Please enter a number between 3 and 100.")

    # else:
    density = int(input('Do you want a dense (1) or a less dense (2) Christmas tree? Type "1" or "2". '))
    if density != 1 and density != 2:
        density = input('Invalid input. Please choose "1" (dense) or "2" (less dense). ')
    choose_char = input('Would you like to choose the character that will be used to create your Christmas tree (default: *). Type "y" or "n". ').lower()

    if choose_char == "y":
        char = input("Please enter your desired character: ")

    if density == 1:

        if size % 2 == 0:
            size += 1

        score = 1
        spaces = int((size + 1 - score))
        print("\n")

        for _ in range(size + 1):
            print(" " * spaces + char * score)
            score += 2
            spaces = spaces - 1

    elif density == 2:
        if size % 2 != 0:
            size += 1

        line = 1
        spaces = int((size + 1 - line))
        print("\n")

        for _ in range(int(size/2) + 1):
            print(" " * spaces + char * line + "\n")
            line += 4
            spaces = spaces - 2

    print("\nTip: If you copy the result and use it in another program, please make sure to select a monospaced font.")
    again = input('\nDo you want to create another Christmas tree? Type "y" or "n". ')
    if again != "y":
        create_tree = False
        
