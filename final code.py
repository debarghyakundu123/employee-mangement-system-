import pickle 
import datetime

d=datetime.datetime.now()
a=d.hour
b=d.minute
c=a+b
e=int(c)
print(c)

"PART1"

while True:                #Password manager=Changes the password in every minute. 
  d=int(input("enter password="))
  if d!=e:
    print("wrong password")
  else:
    print("ok")
    break


def menu():             #Complete Menu Driven
  print("*"*140)
  print("MAIN MENU".center(140))
  print(" "*45+"1. Insert employee record/records=")
  print(" "*45+"2. Display sorted employee record as per emp no")
  print(" "*45+"3. Display sorted employee record as per names ")
  print(" "*45+"4. Display sorted employee record as per Designation")
  print(" "*45+"5. Display employee record as the designation ")
  print(" "*45+"6. Delete Record")
  print(" "*45+"7. Update Record")
  print(" "*45+"8. Search employee record details as per the employee number")
  print(" "*45+"9. search record details as per the customer name")
  print(" "*45+"10. Display gross salary breakup")
  print(" "*45+"11. Exit")
  print("*"*140)


def SortAcc(F):   #Arrage employee records in assending orders of employee number
  try:
    with open(F,"rb+") as fil:
      rec=pickle.load(fil)
      rec.sort(key=lambda rec:rec["ID"])
      fil.seek(0)
      pickle.dump(rec,fil)
  except FileNotFoundError:
    print(F,"File has no Records")


def SortName(F):   #Arrage employee records in assending orders of employee name
  try:
    with open(F,"rb+") as fil:
      rec=pickle.load(fil)
      rec.sort(key=lambda rec:rec["NAME"])
      fil.seek(0)
      pickle.dump(rec,fil)
  except FileNotFoundError:
    print(F,"File has no Records")

def SortDesig(F):  #Arrage employee records in assending orders of designation
  try:
    with open(F,"rb+") as fil:
      rec=pickle.load(fil)
      rec.sort(key=lambda rec:rec["Desig"])
      fil.seek(0)
      pickle.dump(rec,fil)
  except FileNotFoundError:
    print(F,"File has no Records")


"PART2"
def Insert(F):   #Insert all the required details 
  try:
            fil=open(F,"ab+")
            print(fil.tell())
            Des=["MGR","CLK","VP","PRES"]
            Dep=["HR","IT","SALES","FIN"]
            if fil.tell()>0:
              fil.seek(0)
              Rec1=pickle.load(fil)
            else:
              Rec1=[]
            while True:
              while True:
                Eid=input("enter emp id ")
                Eid=Eid.upper()
                if any(dict.get("ID")==Eid for dict in Rec1):
                  print("Employee already exists")
                else:
                  break
              Name=input("enter employee name=")

# mobile number = Only valid 10 digit mobile numbers are accepted 
              while True:
                Mob=input("Enter Mobile=")
                if len(Mob)!=10 or Mob.isdigit()==False:
                  print("please enter valid mobile no") 
                else:
                  break

#email id = Only vaild mail id with proper sign(@,.) are accepted 
              while True:
                Email=input("enter email=")
                if "@" not in Email or "." not in Email:
                  print("enter valid mail address")
                else:
                  break

#specific dept id
              while True:
                Deptid=input("enter dept name of the employee(HR/IT/SALES/FIN)")
                if Deptid.upper() in Dep:
                  break

#designation
              while True:
                Desig=input("enter the designation(MGR/CLK/PRES/VP)")
                if Desig.upper() in Des:
                  break
  
  
              Sal=float(input("enter salary="))
#The current date is stored as the date of joining of the employee
              import datetime 
              Dat=datetime.datetime.now()
              Dat=Dat.date()
              Rec={"ID":Eid.upper(),"NAME":Name.upper(),"MOB":Mob,"EMAIL":Email.upper()
                   ,"DEPTID":Deptid.upper(),"Desig":Desig.upper(),"Sal":Sal
                   ,"date of joining":Dat}
              Rec1.append(Rec)
              pickle.dump(Rec,fil)
              ch=input("do you want to enter more records")
              if ch=="N" or ch=="n":
                break
            fil.close()
            with open(F,"wb") as fil:
              pickle.dump(Rec1,fil)
  except ValueError:
    print("invalid values entered")



"PART 3"
#Display all the input detail with proper heading
def Display(F):
  try:
    with open(F,'rb') as fil:
      print('='*140)
      F='%15s %15s %15s %15s %15s %15s %15s %15s'
      print(F%('ID','NAME','MOBILE','EMAIL ADDRESS','DeptID','DESIGNATION','Salary',
               'Joining Date'))
      print('='*180)
      Rec=pickle.load(fil)
      c=len(Rec)
      for i in Rec:
        for j in i.values():
          print("%15s"%j, end='    ')
        print()
      print('*'*180)
      print('Records Read:',c)
   


  except EOFError:
      print('='*140)
      print('Records Read:',c)

  except FileNotFoundError:
     print(F,"File Doesn't exist")    


#Display on the basis of designation 
def DislpayonDesign(F):
  try:
    with open(F,'rb') as fil:
      Des=['MGR','CLK','VP','PRES']
      print('='*140)
      Rec=pickle.load(fil)
      while True:
        D=input("Enter the Designation(MGR/CLK/PRES/VP)")
        if D.upper() in Des:
          break

      c=0
      F='%15s %15s %15s %15s %15s %15s %15s %15s'
      print(F%('ID' ,'NAME','MOBILE','EMAIL ADDRESS','Dept ID','Designation'
               ,'Salary','Date of Joining'))
      print('='*140)
      for i in Rec:
        if i['Desig']==D.upper():
          c+=1
          for j in i.values():
            print('%15s'%j,end=' ')
          print()
        
      print('*'*140)
      print('Records Read:',c)
      
  except EOFError:
     print('*'*140)
     print('Records Read:',c)

  except FileNotFoundError:
     print(F, "File Doesn't exist")


  
def Update(F):       #Function to update the details of a employee
  try:
    with open(F,'rb+') as fil:
      found=1
      Rec=pickle.load(fil)
      A=input('Enter the Emp ID whose details to be changed')
      for p in Rec:
        if A==p['ID']:
          found=0
          for i,j in p.items():
            if i!='DOJ':
              ch=input('Change' + i + '(Y/N)')
              if ch=='y' or ch=='Y':
                p[i]=input('Enter  ' +i)
                p[i]=p[i].upper()
            elif i=='Sal':
              ch=input('Change' + i + '(Y/N)')
              if ch=='y' or ch=='Y':
                p[i]=float(input('Enter' +i))
          break      
      if found==-1:
        print('Employee details not found')
      else:
        fil.seek(0)
        pickle.dump(Rec,fil)
    
  except EOFError:
      print('Records not found')

  except FileNotFoundError:
     print(F,"File Doesn't exist")

def Delete(F):        #Function to delete the record from the file if it exists.
  try:
    with open(F,'rb+') as fil:
      Rec=pickle.load(fil)
      ch=input('Enter the Employee ID to be deleted')
      for i in range(0,len(Rec)):
        if Rec[i]['ID']==ch:
          print('*'*140)
          F='%5s %15s %15s %20s %15s %15s %7s %22s'
          print(F%('ID' ,'NAME','MOBILE','EMAIL ADDRESS','Dept ID','Designation','Salary','Date of Joining'))
          N=Rec.pop(i)
          for j in N.values():
            print(j,end='  ')
          print('RECORD DELETED')
          break
      else:
        print('Record Not found')
      fil.seek(0)
      pickle.dump(Rec,fil)

  except FileNotFoundError:
     print(F,"File Doesn't exist")
  except KeyError:
    print('Record Not found')
  except IndexError:
    print("Record Not found")

def SearchAcc(F): #Function to search for the record from the file with Empolyee ID
  try:
      with open(F,'rb+')  as fil:
        Rec=pickle.load(fil)
        ch=input('Enter the Employee ID to the searched')
        for i in Rec:
          if i['ID']==ch.upper():
            print('='*140)
            F='%5s %15s %15s %20s %15s %15s %7s %22s'
            print(F%('ID' ,'NAME','MOBILE','EMAIL ADDRESS','Dept ID','Designation','Salary','Date of Joining'))
            print('='*140)
            for j in i.values():
              print('%15s' % j, end=" ")
            print()
            break
        else:
          print("Record not found")
  except FileNotFoundError:
    print(F,"File Doesn't exist")        
      

          
def SearchName(F):#Func to search for the record from the file with the Employee name
  try:
    with open(F,'rb')  as fil:
      Rec=pickle.load(fil)
      found=0
      ch=input('Enter the Customer Name to be searched')
      print('='*140)
      F='%5s %15s %15s %20s %15s %15s %7s %22s'
      print(F%('ID' ,'NAME','MOBILE','EMAIL ADDRESS','Dept ID','Designation','Salary',
               'Date of Joining'))
      print('='*140)
      for i in Rec:
        if i['NAME']==ch.upper():
          found+=1
          for j in i.values():
            print('%15s' % j, end='  ')
          print()
      if found==0:
        print('Record not found')
      else:
        print('Total records displayed :  ', found)
            
    
  except FileNotFoundError:
     print(F, "File Doesn't exist")
  
  except EOFError:
    print('Record not found')



def TOTSal(F):    # Func to show the total Gross salary distribution 
  try:
    with open(F,'rb') as fil:
      Rec=pickle.load(fil)
      print("Please Note the Gross Salary is calculated on the basis of the criteria:")
      print("1. HRA is 30% of Basic Salary")
      print("2.  DA is 15% of Basic Salary")
      print("3.  TAX deducted is 15% of (Basic + HRA +DA)")
      print("4.  Total Gross Salary is: Basic + HRA + DA -Tax ")
      ch=input("Continue(Y/N)")
      if ch=='y' or ch=='Y':
        F='%15s %15s %15s %15s %15s %15s %15s'
        print(F%('ID','NAME','Basic Salary','HRA','DA','TAX','Gross Salary'))
        for i in Rec:
          HRA=round(30*i["Sal"]/100,0)
          DA=round(15*i["Sal"]/100,0)
          Tax=round(((i["Sal"]+HRA+DA)*15/100),0)
          GROSS=HRA+DA+i["Sal"]-Tax
          print(F% (i['ID'],i['NAME'],i['Sal'],HRA,DA,Tax,GROSS))
      else:
        print("Going to the main menu")
      
  except FileNotFoundError:
    print(F,"File Doesn't exist")
      

Fi='Employee'
while True:
  menu()
  ch=input("Enter your Choice")
  if ch=='1':
    Insert(Fi)
  elif ch=='2':
    SortAcc(Fi)
    Display(Fi)
  elif ch=='3':
    SortName(Fi)
    Display(Fi)
  elif ch=='4':
    SortDesig(Fi)
    Display(Fi)
  elif ch=='5':
    DislpayonDesign(Fi)
  elif ch=='6':
    Delete(Fi)
  elif ch=='7':
    Update(Fi)
  elif ch=='8':
    SearchAcc(Fi)
  elif ch=='9':
    SearchName(Fi)
  elif ch=='10':
    TOTSal(Fi)
  elif ch=='11':
    print("EXISTING.......")
    break
