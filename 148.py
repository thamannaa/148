from tkinter import *
import random
root=Tk()
root.title("picnic items")
root.geometry("400x400")
label1=Label(root)
label2=Label(root)
list1=["bottle","tiffin","chocolate","chips","tickets","hanky","id card"]
label1["text"]="listed items:"+str(list1)

def bagcontents():
    random_list=random.sample(range(0,7),1)
    label2["text"]="put item number "+str(random_list)+" in the bag"
    
label1.place(relx=0.5,rely=0.4,anchor=CENTER)
label2.place(relx=0.5,rely=0.5,anchor=CENTER)
btn=Button(root,text="which item to put in the bag",command=bagcontents,bg="orange",fg="white")
btn.place(relx=0.5,rely=0.6,anchor=CENTER)
root.mainloop()

