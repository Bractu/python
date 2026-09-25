#Sam's house has an apple tree and an orange tree that yield an abundance of fruit. Using the information given below, 
# determine the number of apples and oranges that land on Sam's house.

def countApplesAndOranges(s, t, a, b, apples, oranges):
    contApples = 0
    contOranges = 0
    
    for i in range(len(apples)):
        posicion = a + apples[i]
        if posicion >= s and posicion <= t:
            contApples += 1
    for j in range(len(oranges)):
        posicion2 = b + oranges[j]
        if posicion2 >= s and posicion2 <= t:
            contOranges += 1
    print(contApples)
    print(contOranges)
