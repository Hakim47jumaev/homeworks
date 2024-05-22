class Name:
    def __init__(self,fname,lname) :
         
        self.fullname=(fname+" "+lname)
        self.lname=lname
        self.fname=fname
        self.initials=(fname[0]+"."+lname[0])

ob1=Name("hakim","jumaev")
print(ob1.fname) 
print(ob1.lname) 
print(ob1.fullname) 
print(ob1.initials) 