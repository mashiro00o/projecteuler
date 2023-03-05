# Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

b1 = 1
b2 = 0
a = 0

while b1 < 4000000:
  bnew = b1 + b2
  if bnew % 2 == 0:
    a += bnew
  b2 = b1
  b1 = bnew
print(a)
# answer is 4613732
