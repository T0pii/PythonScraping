import random as rand

def initGrid(size):
  return ([[rand.randint(0,1) for i in range(size)] for j in range(size)])

def displayGrid():
  for row in range(size):
    for col in range(size):
      if(grid[row][col] == 0):
        print(".",end="")
      else:
        print("0",end="")
      print(" ",end="")
    print("")

"""
def checkNeighbours(grid,row,col):
  neighbours=0
  for i in range(-1,1):
    for j in range(-1,1):
      if(grid[row+i][col+j] == 1):
        neighbours+=1
  return neighbours
"""

size=10
grid=initGrid(size)
displayGrid()
print(checkNeighbours(grid,1,1))