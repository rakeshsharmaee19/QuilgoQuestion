# returns a tuple of two integers that add up to the target number.
listInput = input().split(' ')
targetNumber = int(input())
def getTuple(listInput, targetNumber):
    for i in range(0,len(listInput)-1):
        base = i+1
        while base<len(listInput):
            if int(listInput[i])+int(listInput[base]) == targetNumber:
                
                return (int(listInput[i]),int(listInput[base]))
            else:
                base+=1
    return 'Not Found'
getTuple(listInput,targetNumber )