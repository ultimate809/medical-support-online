import MySQLdb
import mysql.connector
import csv

def ignore_extra(line):
	temp=""
	for i in line:
		if(i=='|' or i=='.'):
			break;
		temp+=i
	return temp
	

def insert(sno,line):
	db=MySQLdb.connect("localhost","root","Shaurya@123","sdl")
	cursor=db.cursor()
	disease_name=ignore_extra(line[0])
	defination=ignore_extra(line[1])
	symptom=ignore_extra(line[2])
	slimmap=ignore_extra(line[3])
	
	#print (disease_name,defination,symptom,slimmap)


	sql="INSERT INTO diseases VALUES (%d,'%s','%s','%s','%s')"%(sno,disease_name,defination,symptom,slimmap)

	#print ("INSERT INTO test VALUES ('%s','%s','%s')"%(name,place,animal))

	try:
		#execute the sql commqnd
		cursor.execute(sql)
		#commit your changes in the database
		db.commit()
	except:
		#rollback in case there is any error
		print ("Error", sno)
		db.rollback()

	db.close()

with open("medical_database.txt","r") as f1 :
	data=csv.reader(f1,delimiter=";")
	sno=1
	for line in data:
		insert(sno,line)
		sno=sno+1
