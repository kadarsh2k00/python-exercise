def div(a,b):
    try:
        c=a/b
    except ZeroDivisionError:
        print('Check your Expression')
    else:
        print(c)
div(5,0)
            
