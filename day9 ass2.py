def isArmstrong(x): 
      
    n = order(x) 
    temp = x 
    sum1 = 0
    while n<x:
        while (temp != 0): 
           r = temp % 10
           sum1 = sum1 + power(r, n) 
           temp = temp // 10
  
       if(sum1 == x) :
         print("Armstrong")
print("\nUsing for in loop") 
for i in fib(1000):  
    print(i) 

