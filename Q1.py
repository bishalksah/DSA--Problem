price = 199 
tax_rate = 0.18 
name = "keyboard" 
in_stock = True 
total = price * (1 + tax_rate) # int * float -> float
print(type(total), total) # <class 'float'> 234.82