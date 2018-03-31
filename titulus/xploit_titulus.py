##################################################################################################
'''
// @Project      ManTech CTF 2018 Challenge 2
// @Author       Saccharide
'''
##################################################################################################

# Generates the key to challenge 2
def generate_key():

	# the buffer size of checking the key is 32, and it then compares with "~"
	# our solution is to fill up the buffer with any character and adds "~"
	# Useage of the solution: ./titulus password.txt flag.txt enter_key_generated
	
	print "A"*32+"~"

generate_key()


