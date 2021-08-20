import tkinter 
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from PIL import ImageTk,Image
import os
window = tkinter.Tk()
window.title('GUI')

# create labels
namelabel=tkinter.Label(window,text='MODEL EVALUATION',font=("Arial Bold", 15),bg="green",fg="white")
namelabel.grid(row=0,column=1)

#button
#b=Button(window,text = "MODEL EVALUATION",font=("Arial Bold", 10),bg="green",fg="white")
#b.grid(row=0,column=0)
bt = Button (window, text="mobilenet",font=("Arial Bold",10),bg="orange",fg="red")
 
bt.grid (column=1, row=1)
# bt.pack()
abs_file_name = "/"
def browsefunc():
    global abs_file_name
    abs_file_name = filedialog.askopenfilename()
    configs_and_hyperparameter.set(abs_file_name)

configs_and_hyperparameter=StringVar(None)
b=Button(window,text = "Configs and Hyperparameters",font=("Arial Bold",10),command=browsefunc)
b.grid(row=2,column=0)
t=Entry(window,width=100,textvariable=configs_and_hyperparameter)
t.grid(row=2,column=1)

def func2():
    os.system('pip install pillow')

# clone_tf_object_detection = StringVar(None)
b=Button(window,text = "Clone the tensorflow-object-detection",font=("Arial Bold",10),command=func2)
b.grid(row=3,column=0)
t=Entry(window,width=100)
t.grid(column=1,row=3)
def show_image():
    global abs_file_name
    img = ImageTk.PhotoImage(Image.open(abs_file_name))
    ch = Label(window,image=img)
    ch.img = img
    ch.grid(row=5,column=0)


b = Button(window,text="show image",command=show_image)
b.grid(row=4,column=1)

# b=Button(window,text = "Install required packages",font=("Arial Bold",10),bg="green",fg="white")
# b.grid(row=4,column=0)
# t=Entry(window,width=100)
# t.grid(column=1,row=4)


# b=Button(window,text = "Prepare tfrecord files",font=("Arial Bold",10),bg="green",fg="white")
# b.grid(row=5,column=0)
# t=Entry(window,width=100)
# t.grid(column=1,row=5)


# b=Button(window,text = "Download base model",font=("Arial Bold",10),bg="green",fg="white")
# b.grid(row=6,column=0)
# t=Entry(window,width=100)
# t.grid(column=1,row=6)


# b=Button(window,text = "Configuring a Training Pipeline",font=("Arial Bold",10),bg="green",fg="white")
# b.grid(row=7,column=0)
# t=Entry(window,width=100)
# t.grid(column=1,row=7)


# b=Button(window,text = "Run Tensorboard(Optional",font=("Arial Bold",10),bg="green",fg="white")
# b.grid(row=8,column=0)
# t=Entry(window,width=100)
# t.grid(column=1,row=8)


# b=Button(window,text = "Get Tensorboard link",font=("Arial Bold",10),bg="green",fg="white")
# b.grid(row=9,column=0)
# t=Entry(window,width=100)
# t.grid(column=1,row=9)


# b=Button(window,text = "Train the model",font=("Arial Bold",10),bg="green",fg="white")
# b.grid(row=10,column=0)
# t=Entry(window,width=100)
# t.grid(column=1,row=10)


# b=Button(window,text = "click",font=("Arial Bold",10),bg="green",fg="white")
# b.grid(row=11,column=0)
# t=Entry(window,width=100)
# t.grid(column=1,row=11)


# b=Button(window,text = "Exporting a Trained Inference Graph",font=("Arial Bold",10),bg="green",fg="white")
# b.grid(row=12,column=0)
# t=Entry(window,width=100)
# t.grid(column=1,row=12)

# b=Button(window,text = "click",font=("Arial Bold",10),bg="green",fg="white")
# b.grid(row=13,column=0)
# t=Entry(window,width=100)
# t.grid(column=1,row=13)

# b=Button(window,text = "Download the model .pb file",font=("Arial Bold",10),bg="green",fg="white")
# b.grid(row=14,column=0)
# t=Entry(window,width=100)
# t.grid(column=1,row=14)

# b=Button(window,text = "Option1 : upload the .pb file to your Google Drive",font=("Arial Bold",10),bg="green",fg="white")
# b.grid(row=15,column=0)
# t=Entry(window,width=100)
# t.grid(column=1,row=15)



# b=Button(window,text = "Option2 : Download the .pb file directly to your local file system",font=("Arial Bold",10),bg="green",fg="white")
# b.grid(row=16,column=0)
# t=Entry(window,width=100)
# t.grid(column=1,row=16)

# b=Button(window,text = "OPTIONAL: Download the label_map.pbtxt file",font=("Arial Bold",10),bg="green",fg="white")
# b.grid(row=17,column=0)
# t=Entry(window,width=100)
# t.grid(column=1,row=17)


# b=Button(window,text = "OPTIONAL: Download the modified pipline file",font=("Arial Bold",10),bg="green",fg="white")
# b.grid(row=18,column=0)
# t=Entry(window,width=100)
# t.grid(column=1,row=18)

# b=Button(window,text = "Run inference test",font=("Arial Bold",10),bg="green",fg="white")
# b.grid(row=19,column=0)
# t=Entry(window,width=100)
# t.grid(column=1,row=19)

window.mainloop()
