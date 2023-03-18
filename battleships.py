
import socket
import errno
import time

GAME_PORT = 6005
# participating clients must use this port for game communication


############## GAME LOGIC ##############

board1=[]
board2=[]
global finish
finish=True

def print_board(board):
    print("-"*20)
    for i in range (5):
        for j in range (5):
            print("| "+board[i][j],end=' ')
        print("|"+"\n"+"-"*20)

def make_board():
    board=[]
    for i in range (5):
        board.append([])
        for j in range (5):
            board[i].append(' ')
    return board

#get users move & update game
def attack(board,count,loc):
  
    while(True):
        try:
            #loc_atk = [int(item) for item in input("Enter the location for attack : ").split()]
            loc_atk=int(loc[0]),int(loc[2])
            atk=board[loc_atk[0]][loc_atk[1]]
            print(atk)
            print(count)
            if (atk[0]=="O" ):
                board[loc_atk[0]][loc_atk[1]]='X'
                
                count+=1 
                break
            elif (atk[0]=='X'):
                print("ship already hit!")
                
                break
            else :
                print("missed!")
                board[loc_atk[0]][loc_atk[1]]='M' 
                
                break                  
        except Exception as e:
            print(e)
    return count

def placing_ships(board):
    i=0
    while(True):
        try:
            x=''
            while i<4:
                loc = [int(item) for item in input("Enter the location of ship : ").split()]
                
                if board[loc[0]][loc[1]]!='O':
                    board[loc[0]][loc[1]]='O'
                    print_board(board)
                    x+=str(loc)
                    x+='\n'
                    i+=1
                else:
                    print("Ship already placed!")
            break
        except:
            print('invalid input')
            
    return (x)
  
#has game ended
def game_over(count):
      if (count==4):
          print('Game over')
          return True
      else:
         return False
def get_users_move(board,count,move):
    print('user is attacking...')
    c=attack(board,count,move)
    return c

      


def print_opponent_board(board):
      print("-"*20)
      for i in range (5):
        for j in range (5):
            if( board[i][j]=='O'):
             print("|   ",end=' ')
            else:
             print("| "+board[i][j],end=' ')
        print("|"+"\n"+"-"*20)



    
   
############## EXPORTED FUNCTIONS ##############

def game_server(after_connect):
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as accepter_socket:
      accepter_socket.bind(('', GAME_PORT))
      accepter_socket.listen(1)

      # non-blocking to allow keyboard interupts (^c)
      accepter_socket.setblocking(False)
      while True:
        try:
          game_socket, addr = accepter_socket.accept()
        except socket.error as e:
          if e.errno == errno.EAGAIN or e.errno == errno.EWOULDBLOCK:
            time.sleep(0.1)
            continue
        break

      game_socket.setblocking(True)
      with game_socket:
        after_connect()
        print('Game Started')
        #user1=input('username-')
        count1=0#no of ships attacked
        count2=0
        board1=make_board()
        print_board(board1)#create another function called print opponent board to omit printing ships
        
        print('place your ships...')
        x=placing_ships(board1)
        game_socket.send(x.encode())
        opp_ships= game_socket.recv(1024).decode()
        opp_ships=opp_ships.split('\n')
        opp_board=make_board()
        for i in opp_ships[:-1]:
          opp_board[int(i[1])][int(i[4])]="O"
              
            
        print("OPPONENT'S BOARD")
        print_board(opp_board)

       

        while True:

          print("waiting for opp's move")
          opp_move = game_socket.recv(1024).decode()
          if not opp_move:
            break

          count2=get_users_move(board1,count2,opp_move)
          print_board(board1)
          if game_over(count2):
            break

          move=input("Enter the location for attack : ")
          print(move)
          game_socket.send(move.encode())
          count1=get_users_move(opp_board,count1,move)
          print_board(opp_board)          
          if game_over(count1):
            break

      print('Game ended')

def game_client(opponent):
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as game_socket:
      game_socket.connect((opponent, GAME_PORT))
      print('Game Started')
      #user2=input('username-')
      count2=0
      count1=0
      board2=make_board()
      print_board(board2)
      print('place your ships...')
      x=placing_ships(board2)
      game_socket.send(x.encode())
      opp_ships= game_socket.recv(1024).decode()
      opp_ships=opp_ships.split('\n')
      opp_board=make_board()
      

      for i in opp_ships[:-1]:
        opp_board[int(i[1])][int(i[4])]="O"
      print("OPPONENT'S BOARD")
      print_opponent_board(opp_board)
      
      while True:
        move=input("Enter the location for attack : ")
        print(move)
        game_socket.send(move.encode())
        if game_over(count2):
          break
        count2=get_users_move(opp_board,count2,move)
        print_opponent_board(opp_board)

        print("waiting for opp's move")
        opp_move = game_socket.recv(1024).decode()
        if not opp_move:
          break
        count1=get_users_move(board2,count1,opp_move)    
        print_board(board2)
        
         #send a coordinate
        
        #update_game_state('opp', opp_move)
        if game_over(count1):
          break


  
  print('Game ended')

