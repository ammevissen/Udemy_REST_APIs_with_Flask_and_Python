def divide(dividend, divisor):
    if divisor !=0:
        print(dividend/divisor)
    else:
        print("You fool!")

#positional arguments must come before the keyword arguments
divide(dividend=15, divisor=0)
divide(5, divisor=15) 
#cannot do:
#divide(5, dividend=15) #2 dividend arguments, no divisor arguments
#divide(dividend=15, 5) #keyword argument before positional argument