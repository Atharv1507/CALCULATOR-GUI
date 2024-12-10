from tkinter import*

root=Tk()
root.title("Calculator")
root.resizable(False,False)


def AddDigi():
    pass

e=Entry(width=10,borderwidth=5)
e.grid(pady=10,padx=10,row=0,column=0,columnspan=4)



B0=Button(text="0",padx=80,pady=30,command=lambda:AddDigi())
B1=Button(text="1",padx=30,pady=30,command=lambda:AddDigi())
B2=Button(text="2",padx=30,pady=30,command=lambda:AddDigi())
B3=Button(text="3",padx=30,pady=30,command=lambda:AddDigi())
B4=Button(text="4",padx=30,pady=30,command=lambda:AddDigi())
B5=Button(text="5",padx=30,pady=30,command=lambda:AddDigi())
B6=Button(text="6",padx=30,pady=30,command=lambda:AddDigi())
B7=Button(text="7",padx=30,pady=30,command=lambda:AddDigi())
B8=Button(text="8",padx=30,pady=30,command=lambda:AddDigi())
B9=Button(text="9",padx=30,pady=30,command=lambda:AddDigi())


Bc=Button(text="Clear",padx=173,pady=30,command=lambda:AddDigi())
Ba=Button(text="+",padx=29,pady=30,command=lambda:AddDigi())
Bm=Button(text="x",padx=30,pady=30,command=lambda:AddDigi())
Bd=Button(text="÷",padx=29,pady=30,command=lambda:AddDigi())
Bs=Button(text="-",padx=29,pady=30,command=lambda:AddDigi())
Be=Button(text="=",padx=29,pady=30,command=lambda:AddDigi())



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