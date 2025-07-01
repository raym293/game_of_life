import time, os, random

size = 0

def alive(i:int,j:int):
    if i == 0 or i == size or j == 0 or j == size:
        return False
    return arr[i][j]

def play():
    for i in range(size):
        for j in range(size):
            count = 0
            count += alive(i-1,j-1)
            count += alive(i,j-1)
            count += alive(i+1,j-1)
            count += alive(i+1,j)
            count += alive(i+1,j+1)
            count += alive(i,j+1)
            count += alive(i-1,j+1)
            count += alive(i-1,j)
            if count <= 1 or count >=4:
                arr[i][j] = 0
            if count == 3:
                arr[i][j] = 1
if __name__ == '__main__':
    # Setup
    size = int(input("Size of board:\n"))
    arr = [[int((lambda y: (y>0.7))(random.random())) for x in range(size)] for x in range(size)]

    # TODO 
    # check if the game is over

    # Simulate
    while True:
        os.system('clear')
        #print(time.time())
        play()
        for i in arr:
            for j in i:
                print("\033[35m█\033" if j==1 else " ", end="")
            print()
        time.sleep(0.1)
