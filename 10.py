import pickle
def insert(name,roll_no):
   with open("reco.dat","ab") as file:
       dic = {"Name":name, "Roll no.":roll_no}  
       pickle.dump(dic,file)
       print("Saved!")
def Search(roll_no):
   f = open("reco.dat","rb")
   while True:
       text = pickle.load(f)
       try:
           if text["Roll no."] == roll_no:
               print("Search result : ")
               print("Roll no : ",text['Roll no.'])
               print("Name: ",text['Name'])
               break
       except EOFError:
           print("Roll no. not found!")
           break
while True:
   print("""\nMENU:
Press 1 to insert data.
Press 2 to search data.
Press 3 to quit.""")
   inp = int(input())
   if inp == 1:
       while True:
           name = input("Enter Name(type 'm' to go to menu) : ")
           if name == "M" or name == "m":
               break
           else:
               roll_no = int(input("Enter Roll No. : "))
               insert(name,roll_no)

   elif inp == 2:
       while True:
           roll_no = input("Enter Roll(type '!b' to go to menu) : ")
           if roll_no == "M" or roll_no == "m":
               break
           else:
               roll_no = int(roll_no)
               Search(roll_no)
   elif inp == 3:
       break
   else:
       print("Invaild input\n")