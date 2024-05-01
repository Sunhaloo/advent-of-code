# PART 1
def part1():

    visited = set()
    visited.add((0, 0))
    pos = (0, 0)

    # open the file for read
    with open("input.txt", 'r') as file:

        read = file.read().strip()

        # output the contents of file
        for ch in read:

            if ch == "^":
                pos = (pos[0], pos[1] + 1)
            elif ch == ">":
                pos = (pos[0] + 1, pos[1])
            elif ch == "v":
                pos = (pos[0], pos[1] - 1)
            elif ch == "<":
                pos = (pos[0] - 1, pos[1])
            visited.add(pos)
        print(len(visited))

def part2():

    visited = set()
    visited.add((0, 0))
    santa = (0, 0)
    robo = (0, 0)

    def update(pos, ch):
        if ch == "^":
            return (pos[0], pos[1] + 1)
        elif ch == ">":
            return (pos[0] + 1, pos[1])
        elif ch == "v":
            return (pos[0], pos[1] - 1)
        elif ch == "<":
            return (pos[0] - 1, pos[1])


    # open the file for read
    with open("input.txt", 'r') as file:

        read = file.read().strip()

        # output the contents of file
        for line, ch in enumerate(read):
            if line % 2 == 0:
                robo = update(robo, ch)
                visited.add(robo)
            else:
                santa = update(santa, ch)
                visited.add(santa)
        print(visited)
        print(len(visited))

# calling functions
part2()