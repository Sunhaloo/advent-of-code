# open the text file, for read, using context manager
with open("input.txt", 'r') as file:

    # reading the file
    read_file = file.read()

    # DECLARE count: INTEGER
    count = 0

    # exception handling
    try:

        # iterate and check each character in file
        for position, character in enumerate(read_file):
            if count == -1:
                break
            # if elevator is going UP
            if character == "(":
                # counter `count` increases
                count += 1
            # if elevator is going DOWN
            elif character == ")":
                # counter `count` decreases
                count -= 1

    # if file has not been found; raise exception with exception handling
    except FileNotFoundError:

        # ouput appropriate message
        print()
        print("File has NOT been Found!")
        print()

    # if file does not exists; raise exception with exception handling
    except FileExistsError:

        # output appropriate message
        print()
        print("File does NOT Exists!")
        print()

# output the character "position" `position`
print()
print(f"Position that causes Santa to first enter the basement: {position}")
print()

# output the value of `count`
print(f"He is on Floor {count}")
print()

# check if file has been closed
print(f"Is File 'input.txt' closed? {file.closed}")
print()
