n= int(input("Enter Number:"))
temp= n***(1/2)
i=2
j=0
while i<=temp:
	temp2=temp/i
	if temp2==0:
		j+=1
	i+=1
if j>2:
	print("Not Prime")
else:
	print("Prime")
