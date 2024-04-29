---
Alias: 2015 Day 2
Tag:
  - AOC
  - python
Author: S.Sunhaloo
URL: https://www.adventofcode.com/2015/day/2
Date: 
Status:
---

### My Links

- [[AOC 2015 Day 2#Socials | Links to Socials]]

---

# What is the Problem?

Basically, the elves are running low on **wrapping paper**; hence they are going to order some more.

They order in exact amounts, this is because they **know** every size of the presents and, in addition, the presents are all rectangular prisms ( *which makes our lives much easier* ).

# Part 1

## What do we have to find?

Given the that input of the file looks like this:

<p align="center">Text File</p>

```
6x5x26
19x12x20
6x24x25
11x20x7
4x8x5
2x13x11
...
...
```

- We need to calculate the amount / total surface area of each presents + the area of the smallest side.

The answer to that calculation will give us the total amount of wrapping paper needed to wrap a single present.

### Thinking Part 1

They gave us this formula to use:

$$(2 \times l \times w) + (2 \times l \times h) + (2 \times w \times h)$$

I was thinking; this is too fucking long. Like normally, if you are going to find the TSA ( *total surface area* ) of a cuboid you just do $(2 (l \times w) + 4(l \times h) )$

### Ahh!

Because we do **not** have "regular" sizes of boxes / presents; we **cannot** use my formula. We have to use the formula given, because each length, width and height will be different.

### Solution Part 1

```python

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

```

| Answer |
| ------ |
| 1588178 |

---

# Part 2

## What's the problem now?

Now, that we have found the exact amount of wrapping paper needed. They are telling us that they are running low on ribbon, *again*, they are going to buy exact amount of ribbons to make bows.

### Thinking Part 1

The calculation that we are going to make are given as follows:

Find the smallest perimeter of any one face

To find the perimeter we need to simply do:

$$perimeter = (2*l + 2*w) \ or  \ (2*l + 2*h) \ or \ (2*w + 2*h)$$

- Additionally, find the volume of the box; they use that amount to make the bow out of the ribbons

Volume of a fucking box is simply:

$$Volume = l * w * h$$

### Solution Part 2

```python

file_name = "input.txt"

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
            smallest_area = min([area1, area2, area3])
            '''

            # total amount or ribbon
            total_ribbon += volume + smallest_perimeter

    # output the total amount of ribbon needed
    print(f"Total Amount of Ribbon Needed to Buy = {total_ribbon}")
    print()

    # check if file has been closed
    print(f"Is '{file.name}' Closed? {file.closed}")
    print()

```

| Answer |
| ------ |
| 3783758 |

## Reddit Solution

Link to reddit post: https://www.reddit.com/r/adventofcode/comments/3v3w2f/day_2_solutions/

This is the best version of day 2 that I have seen!

```python

def day2_1():
    total = 0
    for line in open('day2input.txt'):
        l, w, h = line.split('x')
        l, w, h = int(l), int(w), int(h)
        area = 2*l*w + 2*w*h + 2*h*l
        slack = min(l*w, w*h, h*l)
        total += area + slack
    print total

def day2_2():
    total = 0
    for line in open('day2input.txt'):
        l, w, h = line.split('x')
        l, w, h = int(l), int(w), int(h)
        ribbon = 2 * min(l+w, w+h, h+l)
        bow = l*w*h
        total += ribbon + bow
    print total

if __name__ == '__main__':
    day2_1()
    day2_2()

```

>And with that; we have solved Day 2 of 2015!

---

# Socials

- [**Instagram**](https://www.instagram.com/s.sunhaloo/)
- [**YouTube**](https://www.youtube.com/channel/UCMkQZsuW6eHMhdUObLPSpwg)
- [**GitHub**](https://www.github.com/Sunhaloo/advent-of-code)

---

S.Sunhaloo
Thank You!