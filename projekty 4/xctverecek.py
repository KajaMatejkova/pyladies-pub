v=10
for i in range(v):
	for l in range(v):
		if i >0 and i < v-1 and l > 0 and l < v-1 :
			print(" ", end = " ")
		else:
			print( "X" , end = " ")
	print()
