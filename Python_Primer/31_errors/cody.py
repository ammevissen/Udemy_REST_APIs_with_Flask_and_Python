from typing import final


def divide(dividend, divisor):
    if divisor==0:
        # print("Divisor cannont be 0.")
        # return
        raise ZeroDivisionError("Divisor cannot be 0.") #creating an exception class
    return(dividend/divisor)

#divide(15, 0)

grades=[78, 99, 85, 100]
grades=[]
print("Welcome to the average grade program.")

try:
    average=divide(sum(grades), len(grades))
except ZeroDivisionError as e:
    #print(e)
    print("There are no grades yet in your list.")
else: #if try successful run else....
    print(f"The average grade is {average}.")
finally:
    print("This always runs")



#errors are often used for flow control.  now get traceback
#other errors: TypeError, ValueError, RuntimeError, can also make custom errors
