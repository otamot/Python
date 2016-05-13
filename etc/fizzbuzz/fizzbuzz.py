for i in range(1,101):
    a=(i%3==0)*2+(i%5==0)
    if(a%2):print"Fizz",
    if(a/2):print"Buzz",
    if(not(a)):print i,
    print
