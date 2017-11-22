for i in range(50):
    if (i>1) and (not(i%3) or not(i%5)):
        s = "" + "fizz" if  not(i%3) else ""
        s += "buzz" if not(i%5) else ""
        print(s)
    else :
        print(i)