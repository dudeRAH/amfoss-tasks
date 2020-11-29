
from math import * # Importing some math libraries to compute sin(x), pi etc
import numpy as np # Importing to have a float range
import sys;

def myfunc(x,b,c): # Defining the function so that it can be called at different values of x
    num=x**2+b*x+c;
    den=sin(x);
    return num/den;


T=input();
if(int(T)==0):
    sys.exit("Number of test cases should be between 1 and 100000");
for i in range(int(T)):
    b=input()
    b=float(b)
    c=input()
    c-float(c)
    nslices=1000; #slicing the graph into smaller units to find effective slope at a point
    deltax=.00000001; #assuming a small value for delta x and finding other attributes and slope via the assumed value
    value=10e22; # very high value in order to swap with the temporary variable to get the smallest value
    tol=.01; #tolerance value below which is considered as zero for slope determination
    for x in np.arange(0.0,pi/2.0,pi/(2.*nslices)):
        x1=x-deltax/2.0
        x2=x+deltax/2.0
        y1=myfunc(x1,b,c);
        y2=myfunc(x2,b,c);
        deltay=y2-y1;
        slope=abs(deltay/deltax);
        if(slope<=tol):
            tmp=myfunc(x,b,c);
            if(tmp<value):
                value=tmp;
    print('The minimum value is',value)

