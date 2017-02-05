x=int(input("enter number"))
flag=0;
for i in range(2,x):
	if(x%i==0):
		
 		flag=1
 		break
if(flag==1):
	print("number is not  prime")
else:
	print(" prime")

