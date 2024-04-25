# What is the problem?

We have a large apartment building in which Santa is trying to deliver presents in each "_house_".

But the directions given to him ( _probably by the elves_ ) are very confusing.

We have an elevator system in which Santa can either go **up** or **down**; he will **never** reach the top or the bottom of the building complex $\Rightarrow$ meaning that there is an unlimited $\infty$ **floors**.

- Going **up** in the elevator is represented by `(`
- Going **down** in the elevator is represented by `)`

# PART 1

## What do we have to find?

Given an input that ressembles something like this

<p align="center">Text File</p>

```console
))(()))(()....
```

**What floor will he be in after the input**?

## Thinking: Part 1

We just need to have a counter; then increment that counter if we find the symbol `(` else if we find the symbol `)`. We have to decrement the same counter.
At the end, we need to output that counter which is basically the **floor** number that he will be on.

### Solution: Part 1

```python
# open the text file, for read, using context manager
with open("input.txt", 'r') as file:

    # reading the file
    read_file = file.read()

    # DECLARE count: INTEGER
    count = 0

    # exception handling
    try:

        # iterate and check each character in file
        for character in read_file:
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

    # if file has not been found; raise exception with exception handling
    except FileExistsError:

        # ouput appropriate message
        print()
        print("File has NOT been Found!")
        print()

# output the value of `count`
print(f"He is on Floor {count}")
print()

# check if file has been closed
print(f"Is File 'input.txt' closed? {file.closed}")
print()
```
| Answer |
| ------ |
|   74   |

# PART 2

## What's the problem now?

Using the same instruction given in the `input.txt` file; find the position of the first character that will cause him to enter the basement, again basement = Floor number `-1`.

### Example

`)` $\Rightarrow$ Means that it will enter basement at character position 1
`()())` $\Rightarrow$ Means that it will enter basement at character position 5

## Thinking: Part 2

So we have floors; we have a lot of them! Now we are trying to find the "_place_" where we are going to enter the basement which is obviously at floor `-1`. Meaning if we have:

- `()())` $\Rightarrow$ this means that at character position 5, we are going to hit the basement ( "Floor _-1_" )

### Solution: Part 2

```python
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

    # if file has not been found; raise exception with exception handling
    except FileExistsError:

        # ouput appropriate message
        print()
        print("File has NOT been Found!")
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
```

| Answer |
| ------ |
|  1795  |
