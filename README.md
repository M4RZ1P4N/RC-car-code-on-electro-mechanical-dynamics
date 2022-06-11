# RC-car-code-on-electro-mechanical-dynamics
So you are about to build an RC car, maybe e-skate or some kind of electric vehicle. This code is made for BLDC motors, Li-Po batteries only, but can be changed for what you need. So basically you type in your motor, battery and other car parameters, and the program prints all the characteristics like 0-100kmh, max speed and etc. Code is made by extensive research on physics and engineering in mind. Good luck! P.S (SymPy library is required)
 
 first download and setup SymPy library from https://www.sympy.org/en/index.html
 
 then open given code in your python compiler and run it
 
 the following will appear :
 
 Kv= "type Kv of a BLDC motor"
 I="type in max current of a BLDC"
 U(s)="type in number of cells in Li-Po battery(eg 3s, 4s==3,4)"
 mah="just type random int" - still in development
 mass.e="type in mass of electronic compenents"- motor, bettery, esc and etc
 
 also:
 you can change parameters of a car in the code itself
mc=1   #mass of car's mechanical compenents
r=0.035  # radius of a car's wheel
f0=0.085   ## rolling friction coefficient (you can find table in the web, but this number is probably more precise)
d=0.25   # car width
h=0.08  ##car height
Cd=0.3 # air ressistance coefficient
J=0.09  # moment of inertia of a car's wheel
