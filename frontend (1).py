#Frontend


from tkinter import *
import tkinter.messagebox
from backend import *

root=Tk()
root.title("First & Follow")
root.geometry("1366x768")
root.config(bg="grey")
            

Input=StringVar()
txtInput=StringVar()


            
#Fuctions
def iExit():
        iExit=tkinter.messagebox.askyesno("First & Follow", "Are you sure???")
        if iExit>0:
                root.destroy()
        return

def clcdata():
        txtInput.delete(0,END)


def adddata():
        inp = txtInput.get("1.0",'end-1c')
        ans=parsefn(inp)
        a=""
        for i in ans:
            a+="\n"+i
        lbl.config(text = "Result : "+a)
    



#Frames
MainFrame=Frame(root, bg="silver")
MainFrame.grid()

TFrame=Frame(MainFrame, bd=5, padx=200, pady=120, bg="grey", relief=RIDGE)
TFrame.pack(side=TOP)

TFrame=Label(TFrame, font=('Roboto', 51, 'bold'), text="First & Follow", bg="grey", fg="orange")
TFrame.grid() 

BFrame=Frame(MainFrame, bd=2, width=0, height=0, padx=18, pady=10, bg="grey", relief=RIDGE)
BFrame.pack(side=BOTTOM)

DFrame=Frame(MainFrame, bd=2, width=0, height=0, padx=20, pady=20, bg="grey", relief=RIDGE)
DFrame.pack(side=BOTTOM)

DFrameL=LabelFrame(DFrame, bd=2, width=0, height=0, padx=100, bg="grey", relief=RIDGE, font=('Arial', 20, 'bold'), text="Input Info\n", fg="white")
DFrameL.pack(side=LEFT)

DFrameR=LabelFrame(DFrame, bd=2, width=0, height=0, padx=310, pady=3, bg="grey", relief=RIDGE, font=('Arial', 20, 'bold'), text="Output\n", fg="white")
DFrameR.pack(side=RIGHT)

#Labels & Entry Box

lblInput=Label(DFrameL, font=('Arial', 18, 'bold'), text="Grammar :", padx=2, pady=2, bg="grey", fg="orange")
lblInput.grid(row=0, column=0, sticky=W)
txtInput=Text(DFrameL, font=('Arial', 18, 'bold'), height = 4,width=30, bg="grey", fg="white")
txtInput.grid(row=0, column=1)


#output kabel

lbl = Label(DFrameR, text = "")
lbl.pack()




#Buttons
btnadd=Button(BFrame, text="Evaluate", font=('Arial', 20, 'bold'), width=10, height=1, bd=4, bg="orange", command=adddata)
btnadd.grid(row=0, column=0)
btnadd.pack()



if __name__=='__main__':
        root=Tk()
        root.mainloop()
