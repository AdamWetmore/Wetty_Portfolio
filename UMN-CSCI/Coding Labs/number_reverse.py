'''
def num_reverse(x):
    d = x//10**3
    x = x%10**3
    c = x//10**2
    x = x%10**2
    b = x//10
    a = x%10
    print(str(a)+str(b)+str(c)+str(d))
'''

def num_reverse(x):
    count = 0
    while(x>0):
        newNum =  x%10
        count = count*10+newNum
        x = x // 10
    print(count)
  
        
