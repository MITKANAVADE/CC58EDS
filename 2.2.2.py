heights = list(map(int,(input()).split()))


max=0
for i in heights :
	if max<i:
		max = i
print(max)