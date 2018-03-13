import string
import random
from random import randint

s="abcdefgh"
l=['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']

f=open("data.txt","w")

f.write("person")
f.write(":")
f.write("20")
f.write("\n")
for i in range(50):
	f.write(str(randint(2007, 2017)))
	f.write(":")
	f.write(random.choice(l))
	f.write(":")
	f.write(random.choice(s))
	f.write("\n")
f.close()
