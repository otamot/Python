for i in range(1,100):
    if((i%3==0&i%5==0)==False):print(str(i))
    else:
        if(i%3==0):print ("Fizz",end="")
        if(i%5==0):print ("Buzz",end="")
        print ("")
