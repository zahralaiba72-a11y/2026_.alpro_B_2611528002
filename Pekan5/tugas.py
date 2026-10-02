#program for the top left output 
height = int(input("Enter the height of the triangle: "))
for i in range(1, height + 1):
    #print spaces
    for j in range(height - i):
        print(" ", end="")
    #print stars
    for k in range( i):
        print("*", end="")
    print()
    
    #program for the bottom left  output
    height2 = int(input("Enter the height of the triangle: "))
    for i in range(height2, 0, -1):
        #print spaces
        for j in range(height2 - i):
            print(" ", end="")
        #print stars
        for k in range(i):
            print("*", end="")
        print()
        
        #program for the right triangle output
        height3 = int(input("Enter the height of the triangle: "))
        for i in range(1, height3 + 1):
            #print spaces
            for j in range(height3 - i):
                print(" ", end="")
            #print stars (2* i -1 gives the number of stars in each row)
            for k in range(2 * i - 1):
                print("*", end="")
            print()