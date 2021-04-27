# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())         
d ={}                     
for i in range(n):        
    text = input().split()     
    d[text[0]] = text[1]       
while 1:
    
    try:
        name = input()
        if name in d :
            print(str(name), "=" ,str(d[name]),sep="")
        else:
            print("Not found")
    except:
        break
