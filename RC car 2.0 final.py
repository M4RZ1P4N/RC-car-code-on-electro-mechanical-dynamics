from sympy import*
Kv=(int(input("Kv="))*2*3.14)/60          #########SI
I=int(input("I="))
U=4.2*int(input("U(s)="))                 ##LIPO
Ah=int(input("mah="))/1000
me=float(input("mass.e="))
g=9.8
mc=1   ##
r=0.035
f0=0.085   ##
A=0.00065
ro=1.3
d=0.25
h=0.08  ##
S=0.8*d*h
Cd=0.3
mu=0.8
J=0.09

m=mc+me
N=m*g
k=(f0*N*A+Cd*ro*S/2)
t=symbols('t')
T=symbols('T',cls=Function)
n=symbols('n')
v=symbols('v',cls=Function)(t)
w=symbols('w')
w=n*v/r
T=(I/Kv)*(1-w/(Kv*U))          #T(w)
print(T)
###################################################################################
v_eqq=Eq(n*T/r-f0*N-k*(v**2),0)
print("v_eqq  ",v_eqq)
VV=solveset(v_eqq,v).args[1]            #V(n)
print(VV)

n_eqq=Eq(diff(VV,n),0)         #V'(n)=0
n_id=solveset(n_eqq,n).args[0]   #  n_ideal
print("n_id=",n_id)
for i in range(len(n_id)):
    if n_id.args[i]>0 and n_id.args[i]<15:
        n_ideal=n_id.args[i]

print("n=",n_ideal)

V_max=VV.subs(n,n_ideal)
print("V_max=",V_max)
###########################################################################

aa=-k
bb=-(n_ideal**2*I)/(U*(Kv*r)**2)
cc=(I*n_ideal)/(Kv*r)-f0*N
print(aa,bb,cc)

V_integ=(atan((2*aa*v+bb)/(2*sqrt(aa)*sqrt(cc-(bb**2)/(4*aa)))))/(sqrt(aa)*sqrt(cc-(bb**2)/(4*aa)))
t=m*(V_integ-V_integ.subs(v,0))                               ####  t(v)
print(v_eqq.subs(n,n_ideal))

print("0-100: ",t.subs(v,27.778))
print("0-max: ",t.subs(v,V_max*0.945))
t1=symbols('t1')
steineq=Eq(t1,m*(V_integ-V_integ.subs(v,0)))
print(steineq)
v=solveset(steineq,v).args[0]                    #####    v(t1)
print(v)
t2=symbols('t2')
S=integrate(v,(t1,0,t2))                        #####   S(t2)
print(S)
print(S.subs(t2,0))
for i in range(0,30):
    if S.subs(t2,i)>390 and S.subs(t2,i)<410:
        print("t_1/4mile",i)
        print("s=",S.subs(t2,i))
########################################################################17.09.2021
print()
print()
print()
print("V_max=",3.6*V_max//1,"km/h")
print("n_ideal==",n_ideal)
print()
while 1<2:
    t5=float(input("t=="))
    print("S(t)=",S.subs(t2,t5),"m")
    print("v(t)=",v.subs(t1,t5)*3.6,"km/h")
    print()

