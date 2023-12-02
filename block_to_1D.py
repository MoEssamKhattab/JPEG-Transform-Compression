import numpy as np

def block_to_1d(block):
    currmode = 0
    n,n = block.shape
    vecimage = np.array([])
    for i in range(n):
        if currmode == 0:
            for j in range(i+1):
                vecimage = np.append(vecimage,block[i-j][j])
        else:
            for j in range(i+1):
                vecimage = np.append(vecimage,block[j][i-j])
        currmode = 1 - currmode
    currmode = 1
    block = np.rot90(block)
    block = np.rot90(block)
    for i in reversed(range(n-1)):
        if currmode == 0:
            for j in range(i+1):
                vecimage = np.append(vecimage,block[i-j][j])
        else:
            for j in range(i+1):
                vecimage = np.append(vecimage,block[j][i-j])
        currmode = 1 - currmode
    return vecimage

print(block_to_1d(np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])))