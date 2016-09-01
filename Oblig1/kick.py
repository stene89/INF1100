# This is a Python program for computing the drag force on a football. (Exercise 1.11)
from math import pi                    
                    
                                    # UNITS BELOW
drag_C = 0.4                        # [Unitless]
rho = 1.2                           # [kg]/[m]^3
a = 0.11                            # [m]
m = 0.43                            # [kg]
g = 9.81                            # [m]

unit_converter = 1/3.6              # ([h]/[s]) * ([m]/[km]) =>>> Unitless
V_hard = 120*unit_converter         # [m]/[s] 
V_soft = 30*unit_converter          # [m]/[s]

A = pi*a**2                         # [m]^2
force_of_G = m*g                    # [kg][m]/[s]^2
F_d = 0.5*drag_C*rho*A*V_hard**2    # [kg][m]/[s]^2
ratio = F_d/force_of_G              # [Unitless]

print """
For a hard kick with velocity 
of %.1f m/s the drag force
on the ball is %.1f N.
The ratio of the drag force 
and the force of gravity is %.1f. 
""" % (V_hard,F_d, ratio)


F_d = 0.5*drag_C*rho*A*V_soft**2    # [kg][m]/[s]^2
ratio = F_d/force_of_G              # [Unitless]

print """
For a hard kick with velocity 
of %.1f m/s the drag force
on the ball is %.1f N.
The ratio of the drag force 
and the force of gravity is %.1f. 
""" % (V_soft,F_d, ratio)

# OUPUT OF RUNNING THE PROGRAM

"""
chsten@laptop:~/git/INF1100/Oblig1$ python kick.py 

For a hard kick with velocity 
of 33.3 m/s the drag force
on the ball is 10.1 N.
The ratio of the drag force 
and the force of gravity is 2.4. 


For a hard kick with velocity 
of 8.3 m/s the drag force
on the ball is 0.6 N.
The ratio of the drag force 
and the force of gravity is 0.2. 
"""

