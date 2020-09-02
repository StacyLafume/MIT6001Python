# Finger exercise: Write a program that examines three variables—x, y, and z—and prints the largest odd number among them. If none of them are odd, it should print a message to that effect.

x,y,z = 23450,7,90
largest = 0
if x%2:
 largest = x
if y%2:
 if y > largest:
  largest = y
if z%2:
 if z > largest:
  largest = z
if largest:
 print ("largest odd number is", largest)
else:
 print ("there are no odd numbers")

 #this will print out "largest number is 7"

#Find a positive integer that is divisible by both 11 and 12
 x=1
while True:
  if x%11 == 0 and x%12 == 0: break
  x=x+1
print(x, 'is divisible by 11 and 12')