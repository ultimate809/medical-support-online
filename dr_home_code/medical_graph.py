import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import csv
import numpy as np

def get_ind(s):
	for i in range(12):
		if all_months[i]==s:
			return i
def get_max_month(no_of_diseases):
	ind=0
	k=0
	for i in no_of_diseases:
		if (i)>int(no_of_diseases[ind]):
			ind=k
		k+=1		
	return ind
	
all_months=['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']
no_of_dis=[]
for i in range(12):
	no_of_dis.append(0)
year=[]
dis_name=[]
month=[]
pname=input("Enter the name of the person for analysis : ")
f1=open("data.txt","r")
con=csv.reader(f1,delimiter=":")
flag=0

for line in con:
	if flag==0:
	 	name=line[0]
	 	age=line[1]
	else:
		year.append(line[0])
		month.append(line[1])
		dis_name.append(line[2]) 
	flag=1 

f1.close()

for i in month:
	ind=get_ind(i)
	no_of_dis[ind]+=1
maxi=int(get_max_month(no_of_dis))

f=open(pname+"_suggestion.txt","w")
f.write("You should take a lot of precaution in the month of ")
f.write(all_months[maxi])
f.write("\nHave a good health")
f.close()


data = {'disease_analysis' : pd.Series(no_of_dis, index=all_months) }
df = pd.DataFrame(data)
fig, axes = plt.subplots(nrows=3, ncols=1)

df.plot(kind='bar', figsize=(12, 10),color='g',title='medical record',linewidth=5,align='center')
plt.savefig('%s'%pname, bbox_inches='tight')
