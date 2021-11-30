# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 15:03:25 2021

@author: Ujjal Chettri
"""


print("NOTE: The program considers the equation of the form ax\u00b2+bx+c")

c1 = float(input("Enter the coefficient x\u00b2: "))
c2 = float(input("Enter the coefficient x: "))
c3 = float(input("Enter the constant c : "))

d = c2**2 - 4*c1*c3

print("The discriminant for your equation is ",d)

if d >= 0:
    def real_roots(a = 0,b = 0,c = 0):
        d1 = d**(1/2)
        r1 = (-b + d1)/(2*a)
        r2 = (-b - d1)/(2*a)
     
        return r1,r2
    print("The roots are ",real_roots(a = c1,b = c2,c = c3))

elif d < 0:
    def img_roots(a = 0,b = 0,c = 0):
        abs_d = abs(d)
        d1 = abs_d**(1/2)
        real = (-b)/(2*a)
        img = (d1)/(2*a)
        
        return real,img
    
    real,img = img_roots(a = c1,b = c2,c = c3)
    r = real
    i = img
    print("The roots of the given equation are { (",r,") +i (",i,") & (",r,") -i (",i,") }")


