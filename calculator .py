print("HELLO AND WELCOME TO THE CALCULATOR")
print("AVAILIBLE COMMANDS ARE \n1.SUBTRACTION\n2.ADDITION\n3.MULTIPLICATION\n4.DIVISION")

isrunning=True
while isrunning==True:
 try:
      operation=int(input("what opperation do you want to perform:"))
      
      if operation==2 :
            n1=  input("type the first number:")
            n1=int(n1)
            n2=  input("type your second number:")
            n2=int(n2)
            print(n1+n2)


      elif operation==1:
            n1=  input("type the first number:")
            n1=int(n1)
            n2=  input("type your second number:")
            n2=int(n2)
            print(n1-n2)

      elif operation==3 :
            n1=  input("type the first number:")
            n1=int(n1)
            n2=  input("type your second number:")
            n2=int(n2)
            print(n1*n2)

      elif operation==4 :
            x1=  input("type the first number:")
            x1=int(x1)
            x2=  input("type your second number:")
            x2=int(x2)
            print(x1/x2)

 except ValueError:
      end=input("do you want to end the program:")


      if end =="yes":
          isrunning=False 
          print("THANK YOU")

      elif end=="no":
            isrunning=True

  
  
    
  
