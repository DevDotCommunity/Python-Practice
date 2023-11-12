def decToBinary(n): 
  
    # Size of an integer is 
    # assumed to be 32 bits 
    for i in range(16, -1, -1): 
        k = n >> i 
        if (k & 1): 
            print("1", end="") 
        else: 
            print("0", end="") 
  
  
# Driver Code 
n = int(input("Enter a number: "))
decToBinary(n) 