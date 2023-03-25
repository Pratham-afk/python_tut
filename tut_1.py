//code to read number of zeroes in input
q=list(map(int,input().split()))
sum=0
for x in q:
  if x==0:
    sum+=0
print(sum)
