import math
i = int(input("Enter a no - "))
j=2
k=0
while j<=math.sqrt(i) :
	if (i%j==0):
		k=1
	j+=1

if(k==0):
	print("Prime")
else:
	print("Not Prime")

