def out():
    output = ""
    print("---------")
    for i in range(3):
        output = "| "
        for j in range(3):
            output += matrix[i][j] + " "
        output += "|"
        print(output)
    print("---------")
matrix = [[' ' for j in range(0, 3)] for i in range(0, 3)]
counter = 0
out()
while True:
    x, y = input("Enter the coordinates: ").split()
    if not (len(x) == 1 and len(y) == 1 and x.startswith(('1', '2', '3', '4', '5', '6', '7', '8', '9', '0')) and y.startswith(('1', '2', '3', '4', '5', '6', '7', '8', '9', '0'))):
        print("You should enter numbers!")
    elif not (1 <= int(x) <= 3 and 1 <= int(y) <= 3):
        print("Coordinates should be from 1 to 3!")
    elif matrix[3-int(y)][int(x)-1] != ' ':
        print("This cell is occupied! Choose another one!")
    else:
        if not counter % 2:
            state = 'X'
        else:
            state = 'O'
        matrix[3-int(y)][int(x)-1] = state
        out()
        strikes = [set(matrix[0]), set(matrix[1]), set(matrix[2]), set([matrix[0][0], matrix[1][0], matrix[2][0]]), set([matrix[0][1], matrix[1][1], matrix[2][1]]), set([matrix[0][2], matrix[1][2], matrix[2][2]]), set([matrix[0][0], matrix[1][1], matrix[2][2]]), set([matrix[0][2], matrix[1][1], matrix[2][0]])]
        str_strikes = [''.join(i) for i in strikes]
        cells = ''.join(matrix[0]) + ''.join(matrix[1]) + ''.join(matrix[2])
        wxs, wos = 0, 0
        if counter >= 5:
            for i in str_strikes:
                if len(i) == 1:
                    if i == "X":
                        wxs += 1
                    elif i == "O":
                        wos += 1
            if wxs == 0 and wos == 0 and (" " not in cells):
                print("Draw")
                break
            elif wxs == 1 and wos == 0:
                print("X wins")
                break
            elif wxs == 0 and wos == 1:
                print("O wins")
                break
        counter += 1
