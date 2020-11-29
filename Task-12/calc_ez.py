
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
    tmpstr=input()
    res=tmpstr.split(',');
    b=float(res[0]);
    
    c=float(res[1]);
    
    nslices=1000;
    deltax=.00000001;
    check=10e22;
    tol=.01;
    for x in np.arange(0.0,pi/2.0,pi/(2.*nslices)):
        x1=x-deltax/2.0
        x2=x+deltax/2.0
        y1=myfunc(x1,b,c);
        y2=myfunc(x2,b,c);
        deltay=y2-y1;
        slope=abs(deltay/deltax);
        #print(slope)
        if(slope<=tol):
            tmp=myfunc(x,b,c);
            if(tmp<check):
                check=tmp;
    print('The minimum value is',check)

