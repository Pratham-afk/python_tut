#code to read number of zeroes in input
q=list(map(int,input().split()))
zeroes=0
for x in q:
  if x==0:
    zeroes+=0
print(zeroes)
