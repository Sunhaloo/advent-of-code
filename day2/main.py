file_name = "input.txt"

# PART 1
def part1():

    print()
    print('-'*40)
    print("Part 1")
    print('-'*40)
    print()

    # initialise a variable for total amount of wrapping paper needed
    total_wrapping_paper = 0

    # open the text file
    with open(file_name, 'r') as file:
        # remove all the 'new line characters' from each line in file
        lines = file.read().split("\n")

        # iterate through that list ---> `lines`
        for values in lines:
            # remove all 'x' from that list
            distance = values.split("x")
            # multiple assignment, convert the length, width and height to integers
            l, w, h = int(distance[0]), int(distance[1]), int(distance[2])

            # calculate the total surface area of presents
            tsa = 2*l*w + 2*l*h + 2*w*h

            # calculate the smallest area
            # calculate each face's area
            area1 = l*w
            area2 = l*h
            area3 = w*h

            # finding the face with the smallest area
            # consider area1 smallest
            if area1 <= area2 and area1 <= area3:
                smallest_area = area1
            # consider area2 smallest
            elif area2 <= area1 and area2 <= area3:
                smallest_area = area2
            # consider area3 smallest
            elif area3 <= area1 and area3 <= area2:
                smallest_area = area3

            '''
            OR we can simply do:
            smallest_area = min([area1, area2, area3])
            '''

            # total amount of wrapping paper needed
            total_wrapping_paper += tsa + smallest_area

    # output the total amount of wrapping paper needed
    print(f"Total Amount of Wrapping Paper Needed to Buy = {total_wrapping_paper}")
    print()
    
    # check if file has been closed
    print(f"Is '{file.name}' Closed? {file.closed}")
    print()

# PART 2
def part2():

    print()
    print('-'*40)
    print("Part 2")
    print('-'*40)
    print()

    # initialise a variable for total amount of ribbon needed
    total_ribbon = 0

    # open the text file
    with open(file_name, 'r') as file:
        # remove all the 'new line characters' from each line in file
        lines = file.read().split("\n")

        # iterate through that list ---> `lines`
        for values in lines:
            # remove all 'x' from that list
            distance = values.split("x")
            # multiple assignment, convert the length, width and height to integers
            l, w, h = int(distance[0]), int(distance[1]), int(distance[2])

            # calculate the volume of present
            volume = l * w * h

            # calculate the smallest perimeter
            # calulating perimeter for each face
            perimeter1 = 2 * l + 2 * w
            perimeter2 = 2 * l + 2 * h
            perimeter3 = 2 * w + 2 * h

            # finding the face with the smallest perimeter
            # consider perimeter1 smallest
            if perimeter1 <= perimeter2 and perimeter1 <= perimeter3:
                smallest_perimeter = perimeter1
            # consider perimeter2 smallest
            elif perimeter2 <= perimeter1 and perimeter2 <= perimeter3:
                smallest_perimeter = perimeter2
            # consider perimeter3 smallest
            elif perimeter3 <= perimeter1 and perimeter3 <= perimeter2:
                smallest_perimeter = perimeter3

            '''
            OR we can simply do:
            smallest_area = min([perimeter1, perimeter2, perimeter3])
            '''

            # total amount or ribbon
            total_ribbon += volume + smallest_perimeter

    # output the total amount of ribbon needed
    print(f"Total Amount of Ribbon Needed to Buy = {total_ribbon}")
    print()

    # check if file has been closed
    print(f"Is '{file.name}' Closed? {file.closed}")
    print()

# calling functions
part1()
part2()