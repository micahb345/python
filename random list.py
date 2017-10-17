from random import randint
def randlist(r,usedlist,done):
	sum = 0
	alpha = [ "A","b","B","c","C","d","G","H","I","J",
				"k","L",]
	usedlist[r] = 1
	c = alpha[r]
	
	for i in range(len(usedlist)):
		sum = sum + usedlist[i]
	#print (c,usedlist,' sum ',sum)
	if sum == 6:
		done = True
	return c,usedlist,done 
	
def main():
	# initial variables
	used = [0,0,0,0,0,0]
	done = False #boolean
	#####################
	while done == False:
		r = randint(0,5)
		c,used,done = randlist(r,used,done)
		c,used,done = randlist(r,used,done)
		print("\033[1;32;40m i did it mr. coleman  \n")
		#print (used)
		print(c,end="")
main()
