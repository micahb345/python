from random import randint
def randlist(r,usedlist,done):
	sum = 0
	alpha = [ "A","B","C","D","E","F","G","H","I",
				"J","K","L","M","N","O","P","Q","R","S",
				"T","U","V","W","X","Y","and","Z","#",
				"={}","{","|","*","!","","","","","","","","",""
				"","","","","","","","","","","","","","","^","_","`","a","b","c","d","e" "F"
	         "g","h",'i','j','k','l','m','n','o','p',
	         'q','r','s','t','u','v','w','x','y','z',
	         '{','|','}','~','-','&','$','@','>','(','+','?']
	usedlist[r] = 1
	c = alpha[r]
	print (len(usedlist))
	
	for i in range(len(usedlist)):
		sum = sum + usedlist[i]
	#print (c,usedlist," sum ",sum)
	if sum == 6:
		done = True
	return c,usedlist,done 
	
def main():
	# initial variables
	used = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,]
	done = False #boolean
	#####################
	while done == False:
		r = randint(0,94)
		c,used,done = randlist(r,used,done)
		print (used,r,c,done)
		#print(c,end="")
main()

