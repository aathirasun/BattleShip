board=[]
# changed this here
for i in range (5):
    board.append([])
    for j in range (5):
        board[i].append('F')
print("-"*20)
for i in range (5):
    for j in range (5):
        print("| "+board[i][j],end=' ')
    print("|"+"\n"+"-"*20)