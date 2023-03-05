# Multiples of 3 or 5
# Problem 1
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

a = 0
b = 0

for b in range(0, 1000, 1):
  if b % 3 == 0 or b % 5 == 0:
    a += b
    
print(a)
# answr is 233168
