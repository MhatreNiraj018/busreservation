import pandas as pd
import pymysql
import pandas.io.sql as sqlio

conn=pymysql.connect(host="localhost",user="root",password="",database="busreservation")
cursor=conn.cursor()
 
def menu():
    print("1.Create table for passenger")
    print("2.Add new passenger detail")
    print("3.Create table busdetail")
    print("4.Add new in busdetail")
    print("5.Show all bus detial table")
    print("6.show all from passenger detail")
    print("7.Reservation of ticket")
    print("8.cancelletion of the ticket")

menu()

def create_passengers():
    c1=conn.cursor()
    query='create table if not exists passengers(pname varchar(30), age varchar(10),busno varchar(30),destination varchar(30),amt varchar(20),status varchar(20))'
    c1.execute(query)
    print('table passenger created successfully') 


def add_passengers():
    c1=conn.cursor()
    l=[]
    pname=input("ENTER PNAME:")
    l.append(pname)
    age=input("ENTER AGE:")
    l.append(age)
    busno=input("ENTER BUSNO:")
    l.append(busno)
    destination=input("ENTER DESTINATION:")
    l.append(destination)
    amt=input("ENTER AMOUNT:")
    l.append(amt)
    status=input("ENTER STATUS:")
    l.append(status)
    pas=(l)
    sql='insert into passengers(pname,age,busno,destination,amt,status)values(%s,%s,%s,%s,%s,%s)'
    c1.execute(sql,pas)
    conn.commit()
    print("RECORD OF PASSENGERS INSERTED")
    df=sqlio.read_sql_query('select * from passengers',conn)
    print(df)


def create_busdetail():
    c1=conn.cursor()
    query='create table if not exists busdetail(bname varchar(30),bnum varchar(10),source varchar(30),destination varchar(30),amt varchar(20),status varchar(20))'
    c1.execute(query)
    print("table busdetail created")


def add_busdetails():
    c1=conn.cursor()
    df=sqlio.read_sql_query('select * from busdetail',conn)
    print(df)
    l=[]
    bname=input('ENTER BUS NAME :')
    l.append(bname)
    bnum=input('ENTER BUS NUMBER :')
    l.append(bnum)
    source=input('ENTER YOUR SOURCE NAME:')
    l.append(source)
    destination=input('ENTER YOUR DESTINATION NAME :')
    l.append(destination)
    amt=input('ENTER AMOUNT :')
    l.append(amt)
    status=input('ENTER BUS STATUS :')
    l.append(status)
    f=(l)
    sql="insert into busdetail(bname,bnum,source,destination,amt,status)values(%s,%s,%s,%s,%s,%s)"
    c1.execute(sql,f)
    conn.commit()
    print('RECORD INSERTED IN BUSDETAIL')

def showbusdetail():
    print('ALL BUS DETAIL')
    df=sqlio.read_sql_query("select * from busdetail",conn)
    print(df)

def showpassengers():
    print("ALL PASSENGERS DETAIL")
    df=sqlio.read_sql_query("select * from passengers",conn)
    print(df)


def ticketreservation():
    print("WE HAVE THE FOLLOWING TYPES OF BUS AVAILABLE FOR YOU")
    print()
    print("BNAME IS 1 FOR BANGALURU TO GOA ") 
    print("PRICE FOR BANGALORE TO GOA PER PERSON IS 2000")
    print("BNAME IS 2 FOR BANGALURU TO CHENNAI ") 
    print("PRICE FOR BANGALORE TO CHENNAI PER PERSON IS 3000")
    bname=(input("ENTER YOUR CHOICE OF BUS YOU WANT TO TRAVEL :"))
    x=int(input("ENTER YOUR CHOICE OF TICKET PLEASE :"))
    n=int(input("ENTER HOW MANY TICKETS YOU NEED PLEASE :"))

    if(x==1):
        print(" YOU HAVE CHOOSE A BUS FROM BANGULURU TO GOA")
        s=2000*n
    elif(x==2):
        print(" YOU HAVE CHOOSE A BUS FROM BANGULURU TO CHENNAI")
        s=3000*n
    else:
        print("INVALID OPTION")
    print("YOUR TOTAL TICKET PRICE IS =",s,"\n")

def cancel():
    print("BEFORE ANY CHANGES IN STATUS")
    df=sqlio.read_sql_query("select * from passengers",conn)
    print(df)
    mc=conn.cursor()
    query="update passengers set status='cancelled' where busno='1045"
    mc.execute(query)
    conn.commit()
    df=sqlio.read_sql_query("select * from passsengers",conn)
    print(df)



opt=""
opt=int(input("ENTER YOUR CHOICE :"))
if opt==1:
    create_passengers()
elif opt==2:
    add_passengers()
elif opt==3:
    create_busdetail()
elif opt==4:
    add_busdetails()
elif opt==5:
    showbusdetail()
elif opt==6:
    showpassengers()
elif opt==7:
    ticketreservation()
elif opt==8:
    cancel()
else:
    "PLEASE ENTER VALID INPUT"










