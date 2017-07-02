#importing the required libraries
import pickle
import sys
import os
import random

#main class 
class create:

    #function for the admin to log in 
    def password(self):

        i=0
        while i<=3:
            password="hello"
            pass123=raw_input('enter your password')

            if password==pass123:
                self.admin()
            else:
                i=i+0
                pass
                

        else:
            pass
                
            

        
        

        
    # function called if user is logged in as an admin           
    def admin(self):


        print "Welcome ADMIN"
        
        y1=False
        
        file=open('accounts.dat','rb')
        file.seek(0,os.SEEK_SET)
        login_name=raw_input('enter name')
        try:
            while True:
                y=pickle.load(file)
                if(login_name==y.name):
                    y1=True
                    print ''
                    print "account of ",y.name,"has been found"
                    print "name:",y.name
                    print "email:",y.email
                    print "phone",y.phone
                    print "Account Id",y.account_id
                    print y.amount

                else:
                    y1=False
                    pass

                    

        except EOFError:
            pass

        if y1==True:
            
            pass
        else:
            pass
            
           









    

    #function is called if user requests a loan         
    def request_loan(self):
        y1=False
        
        file=open('accounts.dat','rb')
        file.seek(0,os.SEEK_SET)
        login_id=input('enter login_id')
        try:
            while True:
                y=pickle.load(file)
                if(login_id==y.account_id):
                    y1=True
                    print "your current amount is",y.account
                    loan=input("enter your loan amount")
                    print "loan" 
                    


                else:
                    
                    pass

                    
        #if no record is found EOFError is raised
        except EOFError:
            pass

        if y1==True:
            
            pass
        elif y1==False:
            
            print "sorry no record found"

        else:
            pass





        
    


        



    #function is called when a user needs to create a new account , and is given an amount of 50000 as default
    def input(self):
        self.name=raw_input('enter your full name')
        self.email=raw_input('enter your email')
        self.phone=raw_input('enter your phone number')
        self.account_id=random.randint(1000,9999)
        print self.account_id,('PLEASE NOTE THIS UNIQUE ID')
        self.amount=50000

    
    
        #uses pickle library to store the data into a dat file 
        file=open("accounts.dat","ab")
        pickle.dump(self,file)
     
        file.close()

   #opens the file and reads the data from the file using the load function from the pickle library     
    def output(self):
        file=open("accounts.dat","rb")
        try:
            while True:
                
                x=pickle.load(file)
                print x.name
                print x.email
                print x.phone
                print x.account_id
                print x.amount
        
        #EOFError is raised if the file is not found  
        except EOFError:
            pass

        file.close()

    #User can look up their data if the user knows the login id
    def search_data(self):
        y1=False
        
        file=open('accounts.dat','rb')
        file.seek(0,os.SEEK_SET)
        login_id=input('enter login_id')
        try:
            while True:
                y=pickle.load(file)
                if(login_id==y.account_id):
                    y1=True
                    print ''
                    print "Your account has been found"
                    print "name:",y.name
                    print "email:",y.email
                    print "phone",y.phone
                    print "Account Id",y.account_id
                    print y.amount

                else:
                    
                    pass

                    

        except EOFError:
            pass

        if y1==True:
            
            pass
        elif y1==False:
            
            print "sorry no record found"

        else:
            pass

    #function used to transfer the money from one account to another account
    def transfer(self):
        file=open('accounts.dat','rb')
        file.seek(0,os.SEEK_SET)
        login_id1=raw_input('enter login_id')
        try:
            while True:
                y=pickle.load(file)
                if(login_id1==y.account_id):
                    print "/n"
                    print "Your account has been found"
                    print "your current amount is",y.amount
                    deb=input( "enter amount of exchange")
                    y.amount=y.amount-deb
                    print "your new amount is",amount
                    print "/n"
                    print "Thank you for making your transaction"
                    

                else:
                    print "Record not found"

        except EOFError:
            pass

        deb=y.amount
        deb=cred

        file=open('accounts.dat','rb')
        file.seek(0,os.SEEK_SET)
        login_id2=raw_input('enter login_id to which money is to be added')
        try:
            while True:
                z=pickle.load(file)
                if(login_id2==z.account_id):
                    print "/n"
                    print "Your account has been found"
                    print "your current amount is",z.amount
            
                    print "your new amount is",amount+y.amount
                    print "/n"
                    print "Thank you for making your transaction"
                    

                else:
                    print "Record not found"

        except EOFError:
            pass
        


    #function if you want to take money from your account    
    def debit(self):
        
        file=open('accounts.dat','rb')
        file.seek(0,os.SEEK_SET)
        login_id=raw_input('enter login_id')
        try:
            while True:
                y=pickle.load(file)
                if(login_id==y.account_id):
                    print '/n'
                    print "Your account has been found"
                    print "your amount is",y.amount
                    deb=input('enter debit')
                    
                    print "thanks"
                    self.input2()

                else:
                    print "Record not found"

        except EOFError:
            pass
        
                    

                   
                    
                    

                    
                    


#main user work starts here

    def main(self):
        print "Welcome to the bank management system "
        ch1=True

        while ch1==True:

            print "Please select one of the following services"
            print "1) create a new account"
            print "2)display credentials of an existing account"
            print "3)Use the interest calculator"
            print "4)Enter a Loan request"
            print "5)select if you are admin"
            request=input('enter:')


#Creating a new account
            if request==1:
                print '/n'
                print 'you have decided on creating a new account'
                self.input()
                check=raw_input('do you wish to double check your data(Y/N)')
                if check=='y':
                    self.output()
                    cont=raw_input('do you wish to edit credentials(Y/N)')
                    if cont=='y':
                        self.input()
                    elif cont=='n':
                        pass
                    else:
                        print "wrong option entered"
                        
                elif check=='n':
                    pass

                else:
                    print "Sorry you have entered a wrong option"

                print "/n"

                cont1=raw_input('do you wish to continue further (Y/N):')

                if cont1=='y':
                    ch1=True

                elif cont1=='n':
                    ch1=False

#displaying credentials of an existing account
                    
            elif request==2:
                
                print (' ')
                print "you have chosen to display the credentials of an existing account"

                self.search_data()

                cont1=raw_input('do you wish to continue further (Y/N):')
 

                if cont1=='y':
                    ch1=True

                elif cont1=='n':
                    ch1=False

                else:
                    print "enter valid option"

                


#Debit request

            elif request==4:
                print ' '
                print 'you have chosen to make a debit request'
                print ' '

                self.request_loan()

                count2=raw_input('do you wish to continue further (Y/N):')
 

                if cont1=='y':
                    ch1=True

                elif cont1=='n':
                    ch1=False

                else:
                    print "enter valid option" 

            
                 


    
#interest calculator
            elif request==3:
                main_amount=input('enter initial amount')
                time=input('enter time in years')
                percent=input('enter annual interest percent')/100.0
                x=(1+percent)
                b=x**time
                final=main_amount*b
                print "your final amount will be",final
                print ' '
                                

                count2=raw_input('do you wish to continue further (Y/N):')
 

                if cont1=='y':
                    ch1=True

                elif cont1=='n':
                    ch1=False

                else:
                    print "enter valid option" 
                
#ADMIN FUNCTION                
        
            elif request==5:
                x=0
                while x==0:
                    self.password()
                    
                    

                    
                








                    

                
                    
                


 

              
                               



        
