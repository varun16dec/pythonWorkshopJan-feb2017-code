x=int(input("Plz en da Num"))

i=2
while i<(x-1):
	if x%i!=0:
		continue
	else:
		print("Not prime")
	i+=1
print("prime")
