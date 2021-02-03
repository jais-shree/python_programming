'''
typecasting : mechanism to convert one type of daa to another type, without changing  initial reference.

syntax :
         new_ref_data = class_constructor(ref_data)
'''

# int-float  compatible
#float-int   compatible

#a=100
a=100.56
print("a =",a)
print("Type of a :",type(a))

#b=float(a)
b=int(a)
print("b =",b)
print("Type of b :",type(b))