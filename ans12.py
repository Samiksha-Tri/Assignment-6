c=complex(input("enter a complex number: "))
print(c.real if c.real>c.imag else c.imag)