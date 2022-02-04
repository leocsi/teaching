tablazat = [["_","_","_","_","_"],  # TODO generate procedurally
            ["_","_","_","_","_"],
            ["_","_","_","_","_"],
            ["_","_","_","_","_"],
            ["_","_","_","_","_"]]


def check_win(x, y, turn, vert, hor):
    if x < 0 or x > len(tablazat)-1 or y < 0 or y > len(tablazat)-1:
        return 0
    elif tablazat[x][y] != turn:
        return 0
    else:
        return check_win(x+hor, y+vert, turn, vert, hor) + 1


def start_check(x, y, turn):
    sums = []
    dirs = (0, 1, -1)
    for v in dirs:
        for h in dirs:
            if v == 0 and h == 0:
                continue
            else:
                sums.append(check_win(x, y, turn, v, h))

    for c in range(4):
        if sums[c] + sums[c+4] - 1 >= 4:
            print("You Won!!!")
            return True
    return False


for sor in tablazat:  # TODO do a function for displaying
    string = ""
    for elem in sor:
        string += "|" + elem + "|"
    print(string)

for i in range(25):

    user_input1 = int(input("Dobd ide a sor számát tesa: "))
    user_input2 = int(input("Ide meg az oszlopét: "))  # TODO transform coordinates to human readable eg.: (1,1) -> bottom left of the grid
    if i % 2 == 0:
        player = "X"
    else:
        player = "0"
    tablazat[user_input1-1][user_input2-1] = player

    if start_check(user_input1-1, user_input2-1, player):
        break
    for sor in tablazat:
        string = ""
        for elem in sor:
            string += "|" + elem + "|"
        print(string)
    # except:  TODO do checks for input: (no try, except clause) repetitions, numbers?, out of bounds
    #     print("Érvénytelen input, próbáld újra.")
    #     user_input1 = int(input("Dobd ide a sor számát tesa: "))
    #     user_input2 = int(input("Ide meg az oszlopét: "))

  # TODO break down into methods