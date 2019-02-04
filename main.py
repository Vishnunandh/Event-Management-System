# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 21:46:45 2018

@author: Thejas
"""
def cls():
    print ("\n" * 50)
import random
import time
import sys
import cx_Oracle
conn = cx_Oracle.Connection("system/12")
cur = conn.cursor()

class EVENT():
    eid=0
    eventname=""
    date=""
    dur = ""
    place=""
    web=""
        
        
    def display(self):
        sql = "select * from event"
        cur.execute(sql)
        print(cur.fetchall())
        
        
        
e = EVENT()

class USER:
    id=0
    name=""
    addr=""
    contactno=0
    emailid=""
    usertype=""
    uname=""
    pwd=""

        
class NORMAL(USER):
    def login(self,username,password):
        self.uname=username
        self.pwd=password
        sql="select * from thejas.visitor where vuname = '%s' and vpass = '%s'"%(self.uname,self.pwd)
        r = cur.execute(sql)
        if(len(cur.fetchall())>=1):
            print("Welcome",self.uname)
            time.sleep(1.5)
            self.content()
        else:
            print("Ivalid username and password")
            time.sleep(1.5)
            main()
        
    def reg(self,name,addr,cno,mail,role,uname,pwd):
        self.id = random.randint(1000,9999)
        self.name=name
        self.addr=addr
        self.contactno=cno;
        self.emailid=mail;
        self.usertype=role;
        self.uname = uname;
        self.pwd = pwd;
        sql="INSERT INTO thejas.visitor VALUES(%d,'%s', '%s', '%s', '%s', '%s','%s','%s')" %(self.id,self.name,self.addr,self.contactno,self.emailid,self.usertype,self.uname,self.pwd)
        r = cur.execute(sql)
        conn.commit()
        print("User Registered Successfully ! Your registration ID",self.id)
        self.content()
        
    def content(self):
       inp=0
       print("1.See Events 2.See winner 3.Back")
       inp = int(input("Enter choice:"))
       if(inp==1):
           time.sleep(1)
           self.seeevents()
       elif(inp==2):
            time.sleep(1)
            self.seewinner()
       elif(inp==2):
            time.sleep(1)
            main()
            
    def seeevents(self):
        sql = "select * from thejas.event"
        cur.execute(sql)
        print(cur.fetchall())
        ip = int(input("press 1 to go back"))
        self.content()
        
        
    def seewinner(self):
        sql = "select * from thejas.winner3"
        cur.execute(sql)
        print(cur.fetchall())
        ip = int(input("press 1 to go back"))
        self.content()
        
        

class ADMIN(EVENT):
    def login(self,username,password):
        self.uname=username
        self.pwd=password
        sql="select * from thejas.admin where auname = '%s' and apass = '%s'"%(self.uname,self.pwd)
        cur.execute(sql)
        r = cur.execute(sql)
        if(len(cur.fetchall())>=1):
            print("Welcome",self.uname)
            self.content()
        else:
            print("Ivalid username and password")
            time.sleep(2)
            main()
    def content(self):
        inp=0
        print("1.Add admin 2.Remove admin 3. Update admin 4.Add events 5.Update Events 6.Delete Events 7.Add volunteer  8.main")
        inp = int(input("Enter choice:"))
        if(inp==1):
            time.sleep(1)
            self.addadmin()
        elif(inp==2):
            time.sleep(1)
            self.removeadmin()
        elif(inp==3):
            time.sleep(1)
            self.updateadmin()
        elif(inp==4):
            time.sleep(1)
            self.addevent()
        elif(inp==5):
            time.sleep(1)
            self.updateevent()
        elif(inp==6):
            time.sleep(1)
            self.removeevent()
        elif(inp==7):
            time.sleep(1)
            self.addvolunteer()
        elif(inp==8):
            main()
            
    def addadmin(self):
        id1 = random.randint(1000,9999)
        auname = input("Enter username:")
        addr = input("Enter address:")
        cno = input("Enter contact number:")
        mailid = input("Enter mail Id: ")
        apass1 = input("Enter password:")
        apass2 = input("Confirm password:")
        if(apass1==apass2):
            sql="INSERT INTO thejas.admin VALUES(%d,'%s', '%s', '%s', '%s', '%s','%s')" %(id1,auname,apass2,addr,cno,mailid,'admin')
            r = cur.execute(sql)
            conn.commit()
            print("Admin Registered Successfully ! Your registration ID",id1)
            print("Come back again by login")
            time.sleep(2)
            main()
        else:
            print("Password is incorrect! enter correct password!")
            time.sleep(2)
            self.addadmin()
            

    def updateadmin(self):
        aid = int(input("Enter admin ID to be updated:"))
        print("1.update username 2.update pwd 3.update personal details")
        ch = int(input("Enter the choice:"))
        if(ch==1):
            username = input("Enter new username:")
            sql = "UPDATE thejas.admin set auname = '%s' where id = %d" %(username,aid)
            cur.execute(sql)
            conn.commit()
            if(cur.rowcount>=1):
                print("Updation success!!")
                time.sleep(1.5)
                self.content()
            else:
                print("Updation Unsuccessful!! ID doesn't EXISTS")
                time.sleep(1.5)
                self.content()
        elif(ch==2):
            pwd1 = input("Enter old password:")
            sql1="select apass from thejas.admin where id = %d" %(aid)
            cur.execute(sql1)
            d = cur.fetchone()
            if(d is not None and d[0]==pwd1):
                pwd2 = input("Enter new password:")
                sql = "UPDATE thejas.admin set apass = '%s' where id = %d" %(pwd2,aid)
                cur.execute(sql)
                conn.commit()
                if(cur.rowcount>=1):
                    print("Updation success!!")
                    time.sleep(1.5)
                    self.content()
                else:
                    print("Updation Unsuccessful!!")
                    time.sleep(1.5)
                    self.content()
                
            else:
                print("Old Password doesn't match or ID doesn't exixts!!!")
                time.sleep(1.5)
                self.content()
        elif(ch==3):
            addr = input("Enter address:")
            cno = input("Enter contact number:")
            mailid = input("Enter mail Id: ")
            sql = "UPDATE thejas.admin set ADDRESS = '%s',CONTACTNO = '%s',EMAILADDRESS = '%s'where ID = %d" %(addr,cno,mailid,aid)
            cur.execute(sql)
            conn.commit()
            if(cur.rowcount>=1):
                print("Details Updation success!!")
                time.sleep(1.5)
                self.content()
            else:
                print("Details Updation Unsuccessful!!ID doesn't exixts")
                time.sleep(1.5)
                self.content()
                
    def removeadmin(self):
        idr = int(input("Enter ID to be removed:"))
        sql = "DELETE FROM thejas.admin where id = %d" %(idr)
        cur.execute(sql)
        conn.commit()
        if(cur.rowcount>=1):
            print("User deleted Successfully!!!!")
            time.sleep(1.5)
            self.content()
        else:
            print("User doesn't EXISTS!!!")
            time.sleep(1.5)
            self.content()
            
    def addevent(self):
        ename =input("Enter event name:")
        dat = input("Enter event date:(dd/mm/yyyy)")
        d = input("Enter event duration:(eg:9 am to 6pm)")
        plc = input("Enter venue of the event:")
        w = input("Enter website for reference:")
        self.eid = random.randint(1000,9999)
        self.eventname = ename
        self.date = dat
        self.place = plc
        self.dur = d
        self.web = w
        sql="INSERT INTO thejas.event VALUES(%d,'%s', TO_DATE('%s','dd/mm/yyyy'), '%s', '%s', '%s')" %(self.eid,self.eventname,self.date,self.dur,self.place,self.web)
        cur.execute(sql)
        conn.commit()
        if(cur.rowcount>=1):
            print("Event Added Successfully ! Event ID is",self.eid)
            time.sleep(2)
            self.content()
        else:
            print("Event not added")
            time.sleep(2)
            self.content()
  
    def removeevent(self):
         ename =input("Enter event name to be removed:")
         sql="DELETE FROM thejas.event where eventname = '%s'" %(ename)
         cur.execute(sql)
         conn.commit()
         if(cur.rowcount>=1):
            print("Event deleted Successfully!!!!")
            time.sleep(1.5)
            self.content()
         else:
            print("Event doesn't EXISTS!!!")
            time.sleep(1.5)
            self.content()

    def updateevent(self):
         eid = int(input("Enter event id to be updated:"))
         self.eid = eid
         print("1.update event name 2.update event date 3.update event dur 4.update event place 5.update event website")
         ch = int(input("Enter choice:"))
         if(ch==1):
             ename = input("Enter new event name:")
             self.eventname = ename
             sql="UPDATE thejas.event set eventname = '%s' where id = %d" %(self.eventname,self.eid)
             cur.execute(sql)
             conn.commit()
             if(cur.rowcount>=1):
                print("Eventname Updated successfully!!")
                time.sleep(1.5)
                self.content()
             else:
                print("Unsuucessful!!!Event ID doesn't exixts")
                time.sleep(1.5)
                self.content()
         elif(ch==2):
             d = input("Enter new event date:")
             self.date = d
             sql="UPDATE thejas.event set doe = TO_DATE('%s','dd/mm/yyyy') where id = %d" %(self.date,self.eid)
             cur.execute(sql)
             conn.commit()
             if(cur.rowcount>=1):
                print("EventDate Updated successfully!!")
                time.sleep(1.5)
                self.content()
             else:
                print("Unsuccessful!!!Event ID doesn't exixts")
                time.sleep(1.5)
                self.content()
         elif(ch==3):
             du = input("Enter new event duration:")
             self.dur = du
             sql="UPDATE thejas.event set dur = '%s' where id = %d" %(self.dur,self.eid)
             cur.execute(sql)
             conn.commit()
             if(cur.rowcount>=1):
                print("EventDuration Updated successfully!!")
                time.sleep(1.5)
                self.content()
             else:
                print("Unsuccessful!!!Event ID doesn't exixts")
                time.sleep(1.5)
                self.content()
         elif(ch==4):
             venue = input("Enter new event venue:")
             self.place = venue
             sql="UPDATE thejas.event set plc = '%s' where id = %d" %(self.place,self.eid)
             cur.execute(sql)
             conn.commit()
             if(cur.rowcount>=1):
                print("EventVenue Updated successfully!!")
                time.sleep(1.5)
                self.content()
             else:
                print("Unsuccessful!!!Event ID doesn't exixts")
                time.sleep(1.5)
                self.content()
                
         elif(ch==5):
             wb= input("Enter new event website:")
             self.web = wb
             sql="UPDATE thejas.event set website = '%s' where id = %d" %(self.web,self.eid)
             cur.execute(sql)
             conn.commit()
             if(cur.rowcount>=1):
                print("EventWebiste Updated successfully!!")
                time.sleep(1.5)
                self.content()
             else:
                print("Unsuccessful!!!Event ID doesn't exixts")
                time.sleep(1.5)
                self.content()
                
    def addvolunteer(self):
        id1 = random.randint(1000,9999)
        name = input("Enter volunteer name")
        addr = input("Enter address:")
        cno = input("Enter contact number:")
        mailid = input("Enter mail Id: ")
        voluname = input("Enter username:")
        volpass1 = input("Enter password:")
        volpass2 = input("Confirm password:")
        if(volpass1==volpass2):
            sql="INSERT INTO thejas.volunteer VALUES(%d,'%s', '%s', '%s', '%s','%s','%s','%s')" %(id1,name,addr,cno,mailid,'volunteer',voluname,volpass2)
            r = cur.execute(sql)
            conn.commit()
            print("Volunteer Registered Successfully ! Your registration ID",id1)
            print("Come back again by login")
            time.sleep(2)
            main()
        else:
            print("Password is incorrect! enter correct password!")
            time.sleep(2)
            self.content()
                
        
                
         
class VOLUNTEER(USER):
    def content(self):
       inp=0
       print("1.SEE TEAMS 2.UPDATE WINNER 3.BACK")
       inp = int(input("Enter choice:"))
       if(inp==1):
           time.sleep(1)
           self.seeusers()
       elif(inp==2):
            time.sleep(1)
            self.updatewinner()
       elif(inp==3):
            time.sleep(1)
            main()
            
    def login(self,username,password):
        self.uname=username
        self.pwd=password
        sql="select * from thejas.volunteer where voluname = '%s' and volpass = '%s'"%(self.uname,self.pwd)
        cur.execute(sql)
        r = cur.execute(sql)
        if(len(cur.fetchall())>=1):
            print("Welcome",self.uname)
            self.content()
        else:
            print("Ivalid username and password")
            time.sleep(2)
            main()
                
    
            
    def seeusers(self):
        sql = "select * from thejas.visitor"
        cur.execute(sql)
        print(cur.fetchall())
        ip = int(input("press 1 to go back"))
        if(ip==1):
            self.content()
            
        
        
    def updatewinner(self):
        win = input("Enter winner username")
        sql = "select * from thejas.visitor where vuname = '%s'"%(win)
        cur.execute(sql)
        if(len(cur.fetchall())>=1):
            p=int(input("Enter winner's place (eg:1 or 2 or 3)"))
            sql = "insert into thejas.winner1 values('%s',%d)"%(win,p)
            r = cur.execute(sql)
            conn.commit()
            print("Winner Updated Successfully !")
            time.sleep(2)
            main()
        else:
            print("Winner not updated")
            time.sleep(2)
            self.content()
            
        
        
        
         
    

    
'''class TEAM(USER):
    def login(self,username,password):
        self.name=username
        self.password=password
        sql=""
        cur.execute(sql)'''
        

n = NORMAL()
a = ADMIN()
v = VOLUNTEER()


def main():
    cls()
    print("--------Welcome to Event Manger V-5.0--------")
    print("1.User Login 2.New User Registeration 3.Volunteer Login 4.Admin Login 5.Exit")
    i = int(input())
    if(i==1):
        time.sleep(1.5)
        print("Welcome to User login")
        username = input("Enter your username:")
        passw = input("Enter your password")
        n.login(username,passw)

    elif(i==2):
        time.sleep(1.5)
        print("Welcome to User Registration")
        name = input("Enter your name:")
        addr = input("Enter your address:")
        cno = input("Enter your contact no:")
        mail = input("Enter your mail:")
        role = input("Enter your role:")
        uname = input("Enter user name:")
        pwd1 = input("Enter password:")
        pwd2 = input("Confirm password")
        if(pwd1==pwd2):
            n.reg(name,addr,cno,mail,role,uname,pwd2)
        else:
            main();
    elif(i==3):
        time.sleep(1.5)
        print("Welcome to User login")
        username = input("Enter your username:")
        passw = input("Enter your password")
        v.login(username,passw)
    
    elif(i==4):
        time.sleep(2)
        print("Welcome to Admin login")
        username = input("Enter your username:")
        passw = input("Enter your password:")
        a.login(username,passw)
        
    elif(i==5):
        sys.exit()
        
    
        
    


main()






    

