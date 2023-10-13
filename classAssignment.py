class multiple():
    def subfield():
        print("Sub-fields in AI are:")
        list=['Machine learning','Neural Networks','Vision','Robotics','Speech processing','Natural language processing']
        for value in list:
            print(value)
            
    def oddeven():
        num=int(input("Enter the number:"))
        if((num%2)==0):
            print("52452 is even number")
        else:
            print("not even number")
            
    def marriageeligibility():
        gender=input("gender:")
        age=int(input("enter age:"))
        if(gender=='male'):
                    if(age>=21):
                         print("eligibile")
                    else:
                         print("not eligibile")
        elif(gender=='female'):
                    if(age>18):
                         print("eligibile")
                    else:
                         print("not eligibile")
        else:
            print("no data")
            
    def percentage():
        sub1=int(input("subject1:"))
        sub2=int(input("subject2:"))
        sub3=int(input("subject3:"))
        sub4=int(input("subject4:"))
        sub5=int(input("subject5:"))
        print("Total:",sub1+sub2+sub3+sub4+sub5)
        print("percentage:",((sub1+sub2+sub3+sub4+sub5)/500*100))
        
    def Triangel():
        Height=int(input("Height:"))
        breadth=int(input("breadth:"))
        print("Area formula=(Height*breadth)/2")
        print("Area of triagle:",(Height*breadth)/2)
        Height1=int(input("Height1:"))
        Height2=int(input("Height2:"))
        Breadth=int(input("Breadth:"))
        print("perimeter formula: Height1+Height2+Breadth")
        print("perimeter of triangle:",Height1+Height2+Breadth)