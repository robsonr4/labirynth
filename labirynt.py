wall = "#"
road = " "
we = "*"

labirynth = [
    [wall, wall, road, wall, wall, wall, wall],
    [wall, road, road, wall, wall, wall, wall],
    [wall, road, wall, road, road, road, wall],
    [wall, road, road, road, wall, road, wall],
    [wall, wall, wall, wall, road, road, wall],
    [wall, wall, wall, wall, we, wall, wall]
]

start = [5, 4]
position = start
end = [0, 2]

for i in range(6):
    for j in range(7):
        print(labirynth[i][j], end="")
    print()

while position != end:
    where = input("Where should i go? (up, down, left, right):  ")

    if where == "right" and labirynth[position[0]][position[1] + 1] != wall:
        labirynth[position[0]][position[1]] = road
        position[1] += 1
        labirynth[position[0]][position[1]] = we
    elif where == "left" and labirynth[position[0]][position[1] - 1] != wall:
        labirynth[position[0]][position[1]] = road
        position[1] -= 1
        labirynth[position[0]][position[1]] = we
    elif where == "up" and labirynth[position[0] - 1][position[1]] != wall:
        labirynth[position[0]][position[1]] = road
        position[0] -= 1
        labirynth[position[0]][position[1]] = we
    elif where == "down" and labirynth[position[0] + 1][position[1]] != wall:
        labirynth[position[0]][position[1]] = road
        position[0] += 1
        labirynth[position[0]][position[1]] = we
    else:
        print("You can't go there, it's a wall.", end="\n\n\n")
        for i in range(6):
            for j in range(7):
                print(labirynth[i][j], end="")
            print()
        continue

    for i in range(6):
        for j in range(7):
            print(labirynth[i][j], end="")
        print()

print("Finisher!!!!!!!!!!")
