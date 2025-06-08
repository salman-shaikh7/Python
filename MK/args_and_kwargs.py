def sum1(a,b,c=0):
    return a+b

"""
1.  Positional Arguments are 'a' and 'b' with position 1 and 2
2.  Here c is Default Argument
"""


def sum2(*args):
    result=0
    for i in args:
        result=result + i
    return result
"""
Here in the above code sum fuction will take as many values it wants 10,20
That is why it is called arbitary argument.
"""

def sum3(*args,**kwargs):
    print(kwargs['Error'])
    print(args)
    return None

sum3(1,2,Error='e1')

##output 
# e1
#(1, 2)

"""
Keyword Argument
Key Value pair input unlimited

"""