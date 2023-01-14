#Collatz Conjecture - Start with a number n > 1. Find the number of steps it takes to reach one using the following process: 
# f n is even, divide it by 2. If n is odd, multiply it by 3 and add 1.



def cc (n):
    steps = 0
    
    
    while n != 1:
        
        steps += 1
        print (f'The number of steps taken: {steps} \n The number is: {n}')
        
        if n % 2 == 0:
            n = n/2
            
        else:
            n *= 3 
            n += 1
            
    return n
n = int(input ('Input a number:'))

cc(n)


