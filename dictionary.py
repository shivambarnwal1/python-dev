print("NOTE: This is a dictionary of only four words (dry,set,abandon,machine)")

d1={"dry":"सूखा", "set":"नबंरों का समूह","abandon":"खडंर", "machine":"यत्रं"}

while(True):
	a1=input("enter a word:")
	print(d1.get(a1))
