# Function to count and print  
# currency notes 
def countCurrency(amount): 
      
    notes = [2000, 500, 200, 100, 
               50, 20, 10, 5, 1] 
                 
    noteCounter = [0, 0, 0, 0, 0, 
                     0, 0, 0, 0] 
       
      
    for i, j in zip(notes, noteCounter): 
        if amount >= i: 
            j = amount // i 
            amount = amount - j * i 
            print (i ," : ", j) 
            
amount = int(input("Enter the amount:"))
countCurrency(amount)
