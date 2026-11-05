#Code A
for number in range(1, 8): 
    if number % 4 == 0:       
        break     
    print(number) 
    #Code B 
    for number in range(1, 8):   
        if number % 4 == 0:       
            continue     
            print(number) 
            #Code C 
            for row in range(1, 4):    
                for column in range(1, 4): 
                    if column == 2:      
                        break       
                    print(row, column) 