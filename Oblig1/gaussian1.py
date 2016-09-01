# This is a Python program for evaluating the Gaussian function

from math import sqrt, pi, exp

m = 0.0 ; s = 2.0 ; x = 1.0        # m & s are parameters, while x the function variable 

gaussfunc = 1/(sqrt(2*pi)*s) * exp((-1/2.0)*((x-m)/s)**2)

print gaussfunc     # The output from the print is the same as my calculations



# OUTPUT FROM RUNNING THE PROGRAM
"""  

chsten@laptop:~/git/INF1100/Oblig1$ python gaussian1.py 
0.176032663382

"""

