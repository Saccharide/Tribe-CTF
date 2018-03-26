# s = "596f75206c6f766520796f757220686f6d6520616e642077616e7420697420746f2062652062656175746966756c2e"
# output = ""
# ubuntu = "7562756e7475"
# for i in range(len(s)//2):
# 	output += "0x"+s[i]+s[i+1] + ", "
# 
# 
# 
# print output

pad = "ubuntu"
def ttt(s):
	ret = []
	for i in range(len(s)):
		tmp = ord(s[i])^ord(pad[i%len(pad)])
		ret.append(chr(tmp))
	return "".join(ret)
 
