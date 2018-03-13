import MySQLdb
import mysql.connector
import csv
import sys

f=open("result.json","w")
f.write("[")

def ignore_extra(line):
	temp=""
	for i in line:
		if(i=='|' or i=='.'):
			break;
		temp+=i
	#temp+='\0'
	#print (temp)
	return temp
'''def insert(sno,line):
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

def view():
	db=MySQLdb.connect("localhost","root","Shaurya@123","sdl")
	cursor=db.cursor()
	#prepare SQL to insert to Insert a record into the database.
	sql="SELECT *FROM diseases;"
	try:
		#execute the Sql command
		cursor.execute(sql)
		#fetch all the rows in al list of lists.
		results=cursor.fetchall()
		for row in results:
			sno=int(row[0])
			dname=row[1]
			defination=row[2]
			symptom=row[3]
			slimmap=row[4]
			ps=row[6];
			
			
			#now print fetched result
			print ("%d%2s%2s%2s%2s" %(sno,dname,defination,symptom,slimmap))
	except:
		print("Error : Unable to fetch data")
	#disconnect from server
	db.close()



def update():
	db=MySQLdb.connect("localhost","root","Shaurya@123","sdl")
	cursor=db.cursor()

	#prepare SQL query to update rerquird records
	m=input("Enter roll no to update")
	roll=input("Enter rollno: ")
	name=raw_input("Enter name: ")
	marks=input("Enter marks: ")
	gend=raw_input("enter gender")
	sql="UPDATE seit SET marks=%f ,gend='%s', name='%s' WHERE roll=%d"%(marks,gend,name,m)
	try:
		cursor.execute(sql)
		db.commit()
	except:
		db.rollback()
	

	db.close()
	
def delete():
	db=MySQLdb.connect("localhost","root","Shaurya@123","college")
	cursor=db.cursor()

	roll=input("Enter roll no to delete: ")
	#prepare sql query to DELETE required records
	sql="DELETE FROM seit WHERE roll=%d"%roll
	try:
		#Execute the SQL command
		cursor.execute(sql)
		#commit your changes in the databse
		db.commit()
		print("Deleted succesfully")
	except:
		db.rollback()
	db.close()

def menu():
	while 1:	
		print("1.INSERT")
		print("2.VIEW")
		print("3.UPDATE")
		print("4.DELETE")
		print("5.EXIT")
		ch=input("Enter your choice(1-5): ")
		#if ch==1:
			#insert()
		if ch==2:
			view()
		elif ch==3:
			update()
		elif ch==4:
			delete()
		elif ch==5:
			exit()
		else:
			print ("enter a valid choice")

def top(x):
	db=MySQLdb.connect("localhost","root","Shaurya@123","sdl")
	cursor=db.cursor()
	#prepare SQL to insert to Insert a record into the database.
	sql="SELECT * FROM diseases limit %d"%x
	try:
		#execute the Sql command
		cursor.execute(sql)
		#fetch all the rows in al list of lists.
		results=cursor.fetchall()
		for row in results:
			sno=int(row[0])
			dname=row[1]
			defination=row[2]
			symptom=row[3]
			slimmap=row[4]
			
			#now print fetched result
			print ("%d%2s%2s%2s%2s" %(sno,dname,defination,symptom,slimmap))
	except:
		print("Error : Unable to fetch data")
	#disconnect from server
	db.close()
'''
def give_name(line):
	db=MySQLdb.connect("localhost","root","Shaurya@123","sdl")
	cursor=db.cursor()
	#prepare SQL to insert to Insert a record into the database.
	sql='SELECT disease_name,symptom FROM diseases where upper(symptom) like upper("%%%s%%") limit 4;'%line
	#sql="SELECT *FROM diseases;"
	#print (" ad")
	try:
		#execute the Sql command
		cursor.execute(sql)
		#fetch all the rows in al list of lists.
		results=cursor.fetchall()
		count = 1;
		for row in results:
			if(count!=1):
				f.write(",")
			#sno=int(row[0])
			dname=row[0]
			#defination=row[2]
			symptom=row[1]
			#slimmap=row[4]
			count=count+1;
			#now print fetched result
			f.write('"')
			f.write(" %2s %2s" %(dname,symptom))
			f.write('"')
	except:
		print("Error : Unable to fetch data")
	#disconnect from server
	db.close()
	
def give_sym(line):
	db=MySQLdb.connect("localhost","root","Shaurya@123","sdl")
	cursor=db.cursor()
	#prepare SQL to insert to Insert a record into the database.
	sql='SELECT  disease_name,symptom FROM diseases where upper(disease_name) like upper("%%%s%%") limit 4;'%line
	#sql="SELECT *FROM diseases;"
	#print (" ad")
	try:
		#execute the Sql command
		cursor.execute(sql)
		#fetch all the rows in al list of lists.
		results=cursor.fetchall()
		count = 1;
		for row in results:
			if(count!=1):
				f.write(",")
			#sno=int(row[0])
			dname=row[0]
			#defination=row[2]
			symptom=row[1]
			#slimmap=row[4]
			count=count+1;
			#now print fetched result
			f.write('"')
			f.write(" %2s %2s" %(dname,symptom))
			f.write('"')
	except:
		print("Error : Unable to fetch data")
	#disconnect from server
	db.close()
			

#menu()

line=["a","a","f"]
i=0
for arg in sys.argv:
	#print(arg)
	line[i]=arg
	i+=1
if(line[1]=="1"):
	give_sym(line[2])
elif(line[1]=="2"):
	give_name(line[2])


#top(3)
#view()
f.write("]")
f.close()
#create table diseases ( sno int , disease_name varchar(500) , defination varchar(500) , symptom varchar(500) , slimmap varchar(500) , primary key (sno));			













