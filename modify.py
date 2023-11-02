x=10 #global variable
def modify_global():
    global x # non-local scope variable, by using global keyword
    x=20
    
modify_global()
print(x)