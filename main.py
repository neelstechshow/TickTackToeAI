import random
import pickle

class TreeNode:
  def __init__(self, board, turn):
    self.children = []
    self.board = board
    self.turn = turn

  def add_child(self, child):
    self.children.append(child)
    
  def show_board(self):
    printed = ''
    for row in self.board:
      for x in row:
        printed += x + ' '
      printed += '\n'
    print(printed)
    
  def turn(self):
    return self.turn
    
  def terminalWin(self):
    
    gameOver = True
    
    if self.board[0][0] == self.board[1][1] == self.board[2][2] != '-':
      return (True, self.board[0][0])
      
    if self.board[2][0] == self.board[1][1] == self.board[0][2] != '-':
      return (True, self.board[2][0])
      
    if self.board[0][0] == self.board[1][0] == self.board[2][0] != '-':
      return (True, self.board[0][0])
      
    if self.board[0][1] == self.board[1][1] == self.board[2][1] != '-':
      return (True, self.board[0][1])

    if self.board[0][2] == self.board[1][2] == self.board[2][2] != '-':
      return (True, self.board[0][2])      
      
    if self.board[0][0] == self.board[0][1] == self.board[0][2] != '-':
      return (True, self.board[0][0])
      
    if self.board[1][0] == self.board[1][1] == self.board[1][2] != '-':
      return (True, self.board[1][0])
      
    if self.board[2][0] == self.board[2][1] == self.board[2][2] != '-':
      return (True, self.board[2][0])
      
    for row in self.board:
      for x in row:
        if x == '-':
          gameOver = False
          
    if gameOver == True:
      return (True, 'DRAW')
      
    else: 
      return (False, 'NONE')
      
class Tree:
  def __init__(self):
    self.root = TreeNode([['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']], 'X')
    self.build_tree(self.root)
    print('Done')
    
  def copyBoard(self, board):
    b = []
    for row in board:
      r = []
      for i in row:
        r.append(i)
      
      b.append(r)
      
    return b
        
	
  def build_tree(self, currentNode):

    a = currentNode.terminalWin()
    if a[0] == True:
      return
    for row in range(len(currentNode.board)):
      for col in range(len(currentNode.board[row])):
        b = self.copyBoard(currentNode.board)
        
        if currentNode.board[row][col] == '-':
          if currentNode.turn == 'X':
            t = 'O'
          else:
            t = 'X'
          b[row][col] = currentNode.turn
          pos = TreeNode(b, t)
          currentNode.add_child(pos)
          self.build_tree(pos)

  def save_tree(self):

    # FINISH
    print('a')
    # BFS METHOD      
    #for i in currentNode.children:
    #  self.build_tree(i)
    
  def play_game(self):
    currentGameBoard = self.root
    
    input("Welcome to the Tic Tac Toe Ai Game, where you can play Tick Tac Toe random AI. You will be player 'X' and the computer will be player 'O'. Press enter to start. \n")
    
    while True:
      while True:
        currentGameBoard.show_board()
        row, col = input('It is now your turn \n Which row would you like to place your X? \n Which column would you like to place your X? ').split(',')
        IRow = int(row)
        ICol = int(col)
        if IRow <= 2 and ICol <= 2 and ICol >= 0 and IRow >= 0:
          break
        else:
          print('PLEASE ENTER A VALID OPTION')


      for x in currentGameBoard.children:
        if x.board[IRow][ICol] == 'X':
          currentGameBoard = x
          currentGameBoard.show_board()
      w = currentGameBoard.terminalWin()
      if w[0] == True and w[1] != 'DRAW':
        print(f'GAME OVER! {w[1]} Has Won!')
        return
      
      elif w[0] == True and w[2] == 'DRAW':
        print('GAME OVER! It ended in a draw.')
        return 
      
      
      r = random.randint(0, len(currentGameBoard.children)-1)
      currentGameBoard = currentGameBoard.children[r]
      print('The AI has played')
      currentGameBoard.show_board()
      w = currentGameBoard.terminalWin()
      if w[0] == True and w[1] != 'DRAW':
        print(f'GAME OVER! {w[1]} Has Won!')
        return
      
      elif w[0] == True and w[1] == 'DRAW':
        print('GAME OVER! It ended in a draw.')
        return 



#g = Tree()
#g.play_game()
f = open('cn.dat', 'r')
pickle.load(f)
