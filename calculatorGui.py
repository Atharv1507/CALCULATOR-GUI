from tkinter import*

root=Tk()
root.title("Calculator")
root.resizable(False,False)
L1=Label(text="WELCOME")
L1.grid(row=6,column=0,columnspan=5)
e=Entry(width=30,borderwidth=5,state=DISABLED)
e.grid(pady=10,padx=10,row=0,column=0,columnspan=4)

num=[]
op=[]

def Toggle(bool):
    global Toggle
    if bool==True:
        e.config(state=NORMAL)
    else:
        e.config(state=DISABLED)


def AddDigi(number):
    Toggle(True)
    i=e.get()
    e.delete(0,END)
    x=str(number)   
    e.insert(0,i+x)
    Toggle(False)


def clr():
    global num
    global op
    num=[]
    op=[]
    Toggle(True)
    e.delete(0,END)
    Toggle(False)

def Add():
    if op!='a'and len(op)!=0:
        Equal()
    op.append('a')
    Toggle(True)
    num.append(float(e.get()))
    e.delete(0,END)
    if len(num)>1:
        s=num[0]+num[1]
        num.clear()
        num.append(s)
    Toggle(False)
        
def Sub():
    if op!='s' and len(op)!=0:
        Equal()
    op.append('s')
    Toggle(True)
    num.append(float(e.get()))
    e.delete(0,END)
    if len(num)>1:
        s=num[0]-num[1]
        num.clear()
        num.append(s)
    Toggle(False)

def Mul():
    if op!='m'and len(op)!=0:
        Equal()
    op.append('m')
    Toggle(True)
    num.append(float(e.get()))
    e.delete(0,END)
    if len(num)>1:
        s=num[0]*num[1]
        num.clear()
        num.append(s)
    Toggle(False)

def Div():
    if op!='d' and len(op)!=0:
        Equal()
    op.append('d')
    Toggle(True)
    num.append(float(e.get()))
    e.delete(0,END)
    if len(num)>1:
        s=num[0]/num[1]
        num.clear()
        num.append(s)
    Toggle(False)

def Equal():
    Toggle(True)

    num.append(float(e.get()))
    x=len(op)

    if op[x-1]=='a':
        s=num[0]+num[1]
        num.clear()
    
    elif op[x-1]=='s':
        s=num[0]-num[1]
        num.clear()
    
    elif op[x-1]=='d':
        s=num[0]/num[1]
        num.clear()
    
    elif op[x-1]=='m':
        s=num[0]*num[1]
        num.clear()

    e.delete(0,END)
    e.insert(0,s)

    Toggle(False)



B0=Button(text="0",padx=80,pady=30,command=lambda:AddDigi(0))
B1=Button(text="1",padx=30,pady=30,command=lambda:AddDigi(1))
B2=Button(text="2",padx=30,pady=30,command=lambda:AddDigi(2))
B3=Button(text="3",padx=30,pady=30,command=lambda:AddDigi(3))
B4=Button(text="4",padx=30,pady=30,command=lambda:AddDigi(4))
B5=Button(text="5",padx=30,pady=30,command=lambda:AddDigi(5))
B6=Button(text="6",padx=30,pady=30,command=lambda:AddDigi(6))
B7=Button(text="7",padx=30,pady=30,command=lambda:AddDigi(7))
B8=Button(text="8",padx=30,pady=30,command=lambda:AddDigi(8))
B9=Button(text="9",padx=30,pady=30,command=lambda:AddDigi(9))


Bc=Button(text="Clear",padx=173,pady=30,command=lambda:clr())
Ba=Button(text="+",padx=29,pady=30,command=lambda:Add())
Bm=Button(text="x",padx=30,pady=30,command=lambda:Mul())
Bd=Button(text="÷",padx=29,pady=30,command=lambda:Div())
Bs=Button(text="-",padx=29,pady=30,command=lambda:Sub())
Be=Button(text="=",padx=29,pady=30,command=lambda:Equal())



Bc.grid(row=1,column=0,columnspan=4)

B7.grid(row=2,column=0)
B8.grid(row=2,column=1)
B9.grid(row=2,column=2)
Ba.grid(row=2,column=3)

B4.grid(row=3,column=0)
B5.grid(row=3,column=1)
B6.grid(row=3,column=2)
Bs.grid(row=3,column=3)


B1.grid(row=4,column=0)
B2.grid(row=4,column=1)
B3.grid(row=4,column=2)
Bd.grid(row=4,column=3)

B0.grid(row=5,column=0,columnspan=2)
Be.grid(row=5,column=2)
Bm.grid(row=5,column=3)





root.mainloop()