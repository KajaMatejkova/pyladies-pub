v=10
for i in range(v):
	for k in range(v):
		if i >0 and i < v-1 and k > 0 and k < v-1 :
			print(" ", end = " ")
		else:
			print( "X" , end = " ")
	print()
