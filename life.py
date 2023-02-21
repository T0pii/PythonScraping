import random as rand
import time

GRIDSIZE=30

def initGrid(size):
  return ([[rand.randint(0,1) for i in range(size)] for j in range(size)])

def displayGrid(grid):
  for row in range(GRIDSIZE):
    for col in range(GRIDSIZE):
      if(grid[row][col] == 0):
        print(".",end="")
      else:
        print("O",end="")
      print(" ",end="")
    print("")

def countNeighbors(grid,row,col):
  neighborCount=0
  for i in range(-1,2):
    for j in range(-1,2):
      if i == 0 and j == 0:
        continue
      if row + i >= 0 and row + i < GRIDSIZE and col + j >= 0 and col + j < GRIDSIZE:
        if grid[row+i][col+j] == 1:
          neighborCount+=1
  return neighborCount

def nextGeneration(grid):
  nextGenGrid=[]
  for row in range(GRIDSIZE):
    nextGenRow = []
    for col in range(GRIDSIZE):
      cellNeighbors=countNeighbors(grid,row,col)
      if grid[row][col] == 1:
        if cellNeighbors < 2 or cellNeighbors > 3:
          nextGenRow.append(0)
        else:
          nextGenRow.append(1)
      else:
        if cellNeighbors == 3:
          nextGenRow.append(1)
        else:
          nextGenRow.append(0)
    nextGenGrid.append(nextGenRow)
  return nextGenGrid

def main():
  grid = initGrid(GRIDSIZE)
  displayGrid(grid)
  while True:
    time.sleep(0.4)
    grid=nextGeneration(grid)
    displayGrid(grid)
    
main()