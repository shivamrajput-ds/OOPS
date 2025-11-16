class chatbook:
    def __init__(self):
        self.username=""
        self.password=""
        self.loggedin=False
        self.menu()

    def menu(self):
        user_input=input("""welcome to the chatbook !| How would you like to proceed?
                            1. Press 1 to sign up
                            2. Press 2 to sign in
                            3. Press 3 to write a post
                            4. press 4 to message a friend
                            5. press any other key to exit
                        """) 
        if user_input=="1":
            self.signup()
        elif user_input=="2":
            self.signin()
        elif user_input=="3":
            self.mypost()
        elif user_input=="4":
            self.sendmsg()    
        else:
            exit()    

    def signup(self):
        email=input("Enter your email")
        password=input("Setup your password")
        self.username=email
        self.password=password
        print("you have sign up successfully")
        print("\n")
        self.menu()

    def signin(self):
        if self.username=="" and self.password=="":
            print("Please signup first by pressing the 1 in main menu")
        else:
            user_name=input("Enter your email")
            user_password= input("Setup your password")   
            if user_name==self.username and self.password==user_password:
                print("you have sign in successfully")
                print("\n")
                self.loggedin=True
            else:
                print("please input correct credentials")  
            self.menu() 

    def mypost(self):
        if self.loggedin==True:
            txt=input("Enter your message here")
            print(f"Following content has been posted{txt}")
        else:
            print("Please signup first by pressing the 1 in main menu afterward only you can post")

    def sendmsg(self):
        if self.loggedin==True:
            txt=input("Enter your message here")
            frnd=input("Whom you have to seen message?")
            print(f"Your message has sent to {frnd}")
        else:
             print("Please signup first by pressing the 1 in main menu afterward only you can sent message to friend")
                
# obj=chatbook()            
         
