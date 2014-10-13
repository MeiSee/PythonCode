lines = 100000
if lines < 1000:
	print("small")
elif lines < 10000:
	print("medium")
else:
	print("large")

x = int(input("Please insert your number:"))
if x > 10:
	print("big")
elif x < 5:
	print("medium")
else:
	print("small")
	
for country in ["malysia","india","england","taiwan"]:
	print(country)	
	
for x in range(1,10):
    for y in range(1,10):
        print (x,'*',y,'=',x*y)
	
	
	
	
