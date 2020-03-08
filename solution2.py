a = 1
b = 1
c = 0
Final = 0

while c < 4000000:
   c = (a+b)         
   if c%2 == 0:
       Final = Final + c

   a = b
   b = c

print Final
