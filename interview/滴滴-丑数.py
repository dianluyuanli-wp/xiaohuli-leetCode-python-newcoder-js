
def GetUglyNumber_Solution(index):
	if (index <= 0):
		return 0
	uglyList = [1]
	indexTwo = 0
	indexThree = 0
	indexFive = 0
	for i in range(index-1):
		newUgly = min(uglyList[indexTwo]*2, uglyList[indexThree]*3, uglyList[indexFive]*5)
		uglyList.append(newUgly)
		if (newUgly % 2 == 0):
			indexTwo += 1
		if (newUgly % 3 == 0):
			indexThree += 1
		if (newUgly % 5 == 0):
			indexFive += 1
	return uglyList[-1]
        
while True:
	try:
		a=raw_input()
		if not a:
			break
		a=int(a)
		print GetUglyNumber_Solution(a)
	except:
		break
