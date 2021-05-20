from mymodule import divide
import sys
#import mymodule #to get all

print(sys.path)
print(divide(10, 2))
print(__name__)  #only the main file is main, others are different.

#may need to create an __init__.py when importing files