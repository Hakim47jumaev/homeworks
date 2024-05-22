class employe:
    def __init__(self,fname,lname) :
         
        self.fullname=(fname+" "+lname)
        self.email=(fname+"."+lname+"@company.com")   
ob1=employe("hakim","jumaev")
print(ob1.fullname) 
print(ob1.email) 


        