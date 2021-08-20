import tkinter 
from tkinter import ttk
from tkinter import*
from tkinter import messagebox
#from PIL import ImageTk,Image
window = tkinter.Tk()
window.title('GUI')
window.geometry("600x600")

# create labels
#namelabel=tkinter.Label(window,text='MODEL EVALUATION',font=("Arial Bold", 15),bg="green",fg="white")
#namelabel.grid(row=0,column=1)

#button
#b=Button(window,text = "MODEL EVALUATION",font=("Arial Bold", 10),bg="green",fg="white")
#b.grid(row=0,column=0)
# create labels
namelabel=tkinter.Label(window,text='MODEL EVALUATION',font=("Arial Bold", 15),bg="green",fg="white")
namelabel.grid(row=0,column=1)


bt = Button (window, text="mobilenet",font=("Arial Bold",10),bg="orange",fg="red")
 
bt.grid (column=1, row=1)
# bt.pack()
abs_file_name = "/"
def browsefunc():
    global abs_file_name
    abs_file_name = filedialog.askopenfilename()
    configs_and_hyperparameter.set(abs_file_name)


#def clicked(): 
#    namelabel.configure (text="Button was clicked !!") 
#bt = Button (window, text="enter", command=clicked)

from tkinter import filedialog
#root = Tk()

'''def browsefunc():
    filename = filedialog.askopenfilename()
    pathlabel.config(text=Roboflow_tensorflow_object_detection_mobilenet_colab)

browsebutton = Button(window, text="Browse", command=browsefunc)
browsebutton.grid(row=0,column=0)'''

#pathlabel = Label(window)
#pathlabel.pack()
abs_file_name = "/"
def browsefunc():
    global abs_file_name
    abs_file_name = filedialog.askopenfilename()
    configs_and_hyperparameter.set(abs_file_name)

configs_and_hyperparameter=StringVar()
b=Button(window,text = "Configs and Hyperparameters",font=("Arial Bold",10),bg="green",fg="white",command=browsefunc)
b.grid(row=2,column=0)
t=Entry(window,width=50,textvariable=configs_and_hyperparameter)
t.grid(row=2,column=1)


'''b=Button(window,text = "Configs and Hyperparameters",font=("Arial Bold",10),bg="green",fg="white")
b.grid(row=2,column=0)
t=Entry(window,width=50)
t.grid(column=1,row=2)'''
import os

def func2():
    os.system('pip install pandas')
    global P_Text_E, P_Text_L, S_K_L, S_K_E, plain_text, cctk
   # clone_tf_object_detection = StringVar()
b=Button(window,text = "Clone the tensorflow-object-detection",font=("Arial Bold",10),command=func2)
b.grid(row=3,column=0)
t=Entry(window,width=50)
t.grid(column=1,row=3)

def func4():
    os.system('pip install pandas')
    #Install_required_packages = StringVar()
b=Button(window,text = "Install required packages",font=("Arial Bold",10),bg="green",fg="white",command=func4)
b.grid(row=4,column=0)
t=Entry(window,width=50)
t.grid(column=1,row=4)

def func5():
    os.system('pip install pandas')
    #Install_required_packages = StringVar()

b=Button(window,text = "Prepare tfrecord files",font=("Arial Bold",10),command=func5)
b.grid(row=5,column=0)
t=Entry(window,width=50)
t.grid(column=1,row=5)

def func6():
    os.system('pip install pandas')
    #Install_required_packages = StringVar()
b=Button(window,text = "Download base model",font=("Arial Bold",10),bg="green",fg="white",command=func6)
b.grid(row=6,column=0)
t=Entry(window,width=50)
t.grid(column=1,row=6)

def func7():
    os.system('pip install pandas')
    #Install_required_packages = StringVar()
b=Button(window,text = "Configuring a Training Pipeline",font=("Arial Bold",10),command=func7)
b.grid(row=7,column=0)
t=Entry(window,width=50)
t.grid(column=1,row=7)

def func8():
    os.system('pip install pandas')
    #Install_required_packages = StringVar()
b=Button(window,text = "Run Tensorboard(Optional",font=("Arial Bold",10),bg="green",fg="white",command=func8)
b.grid(row=8,column=0)
t=Entry(window,width=50)
t.grid(column=1,row=8)

def func9():
    os.system('pip install pandas')
    #Install_required_packages = StringVar()
b=Button(window,text = "Get Tensorboard link",font=("Arial Bold",10),command=func9)
b.grid(row=9,column=0)
t=Entry(window,width=50)
t.grid(column=1,row=9)

def func10():
    os.system('pip install pandas')
    #Install_required_packages = StringVar()
b=Button(window,text = "Train the model",font=("Arial Bold",10),bg="green",fg="white",command=func10)
b.grid(row=10,column=0)
t=Entry(window,width=50)
t.grid(column=1,row=10)

def func11():
    os.system('pip install pandas')
    #Install_required_packages = StringVar()
b=Button(window,text = "click",font=("Arial Bold",10),command=func11)
b.grid(row=11,column=0)
t=Entry(window,width=50)
t.grid(column=1,row=11)

def func12():
    os.system('pip install pandas')
    #Install_required_packages = StringVar()
b=Button(window,text = "Exporting a Trained Inference Graph",font=("Arial Bold",10),bg="green",fg="white",command=func12)
b.grid(row=12,column=0)
t=Entry(window,width=50)
t.grid(column=1,row=12)


def func13():
    os.system('pip install pandas')
    #Install_required_packages = StringVar()
b=Button(window,text = "click",font=("Arial Bold",10),command=func13)
b.grid(row=13,column=0)
t=Entry(window,width=50)
t.grid(column=1,row=13)


def func14():
    os.system('pip install pandas')
    #Install_required_packages = StringVar()
b=Button(window,text = "Download the model .pb file",font=("Arial Bold",10),bg="green",fg="white",command=func14)
b.grid(row=14,column=0)
t=Entry(window,width=50)
t.grid(column=1,row=14)

def func15():
    os.system('pip install pandas')
    #Install_required_packages = StringVar()
b=Button(window,text = "Option1 : upload the .pb file to your Google Drive",font=("Arial Bold",10),command=func15)
b.grid(row=15,column=0)
t=Entry(window,width=100)
t.grid(column=1,row=15)


def func16():
    os.system('pip install pandas')
    #Install_required_packages = StringVar()
b=Button(window,text = "Option2 : Download the .pb file directly to your local file system",font=("Arial Bold",10),bg="green",fg="white",command=func16)
b.grid(row=16,column=0)
t=Entry(window,width=50)
t.grid(column=1,row=16)


def func17():
    os.system('pip install pandas')
    #OPTIONAL:_Download_the_label_map.pbtxt_file = StringVar()
b=Button(window,text = "OPTIONAL: Download the label_map.pbtxt file",font=("Arial Bold",10),command=func17)
b.grid(row=17,column=0)
t=Entry(window,width=100)
t.grid(column=1,row=17)


def func18():
    os.system('pip install pandas')
    #OPTIONAL:_Download_the_modified_pipline_file = StringVar()
b=Button(window,text = "OPTIONAL: Download the modified pipline file",font=("Arial Bold",10),bg="green",fg="white",command=func18)
b.grid(row=18,column=0)
t=Entry(window,width=100)
t.grid(column=1,row=18)



#b = Button(window,text="show image",command=show_image)
#b.grid(row=19,column=0)
def show_image():
    global abs_file_name
    img = ImageTk.PhotoImage(Image.open(abs_file_name))
    ch = Label(window,image=img)
    ch.img = img
    ch.grid(row=5,column=0)
b = Button(window,text="show image",font=("Arial Bold",10),command=show_image)
b.grid(row=19,column=0)
t=Entry(window,width=60)
t.grid(column=1,row=19)




'''rad2 = Radiobutton(window, text="FasterRcnn", value=3)
rad2.grid(column=4, row=3)
import tkinter as tk
from tkinter import ttk
from tkinter import*
from tkinter import scrolledtext
window = tk.Tk()
window.title('scrolledtext')
window.geometry("600x600")

ttk.Label(window,text="mobilenet",background="blue",foreground="white",
          font=("Times new Roman",15)).grid(row=0,column=0)

text1=scrolledtext.ScrolledText(window,wrap=tk.WORD,width=60,height=1)
text1.grid(column=1,row=0,pady=5,padx=5)
ttk.Label(window,text="Clone the tensorflow-object-detection ",background="pink",foreground="red",
          font=("Times new Roman",15)).grid(row=2,column=0)

text2=scrolledtext.ScrolledText(window,wrap=tk.WORD,width=60,height=1)
text2.grid(column=1,row=2,pady=5,padx=5)

ttk.Label(window,text="Install required packages ",background="pink",foreground="red",
          font=("Times new Roman",15)).grid(row=3,column=0)

text3=scrolledtext.ScrolledText(window,wrap=tk.WORD,width=60,height=1)
text3.grid(column=1,row=3,pady=5,padx=5)

ttk.Label(window,text="Prepare tfrecord files",background="pink",foreground="red",
          font=("Times new Roman",15)).grid(row=4,column=0)

text4=scrolledtext.ScrolledText(window,wrap=tk.WORD,width=60,height=1)
text4.grid(column=1,row=4,pady=5,padx=5)

ttk.Label(window,text="Download base model",background="pink",foreground="red",
          font=("Times new Roman",15)).grid(row=5,column=0)

text5=scrolledtext.ScrolledText(window,wrap=tk.WORD,width=40,height=1)
text5.grid(column=1,row=5,pady=5,padx=5)

ttk.Label(window,text="Configuring a Training Pipeline ",background="pink",foreground="red",
          font=("Times new Roman",15)).grid(row=6,column=0)

text6=scrolledtext.ScrolledText(window,wrap=tk.WORD,width=40,height=1)
text6.grid(column=1,row=6,pady=5,padx=5)

ttk.Label(window,text="Run Tensorboard(Optional) ",background="pink",foreground="red",
          font=("Times new Roman",15)).grid(row=7,column=0)

text7=scrolledtext.ScrolledText(window,wrap=tk.WORD,width=40,height=1)
text7.grid(column=1,row=7,pady=5,padx=5)

ttk.Label(window,text="Get Tensorboard link ",background="pink",foreground="red",
          font=("Times new Roman",15)).grid(row=8,column=0)

text8=scrolledtext.ScrolledText(window,wrap=tk.WORD,width=40,height=1)
text8.grid(column=1,row=8,pady=5,padx=5)
ttk.Label(window,text="Train the model ",background="pink",foreground="red",
          font=("Times new Roman",15)).grid(row=9,column=0)

text9=scrolledtext.ScrolledText(window,wrap=tk.WORD,width=40,height=1)
text9.grid(column=1,row=9,pady=5,padx=5)

ttk.Label(window,text="Exporting a Trained Inference Graph",background="pink",foreground="red",
          font=("Times new Roman",15)).grid(row=10,column=0)

text10=scrolledtext.ScrolledText(window,wrap=tk.WORD,width=40,height=1)
text10.grid(column=1,row=5,pady=5,padx=5)

ttk.Label(window,text="Download the model .pb file ",background="pink",foreground="red",
          font=("Times new Roman",15)).grid(row=11,column=0)

text11=scrolledtext.ScrolledText(window,wrap=tk.WORD,width=40,height=1)
text11.grid(column=1,row=11,pady=5,padx=5)

ttk.Label(window,text=" ",background="pink",foreground="red",
          font=("Times new Roman",15)).grid(row=12,column=0)

text12=scrolledtext.ScrolledText(window,wrap=tk.WORD,width=40,height=1)
text12.grid(column=1,row=12,pady=5,padx=5)
ttk.Label(window,text="Download the model .pb file ",background="pink",foreground="red",
          font=("Times new Roman",15)).grid(row=13,column=0)

text13=scrolledtext.ScrolledText(window,wrap=tk.WORD,width=40,height=1)
text13.grid(column=1,row=13,pady=5,padx=5)
ttk.Label(window,text="Download the model .pb file ",background="pink",foreground="red",
          font=("Times new Roman",15)).grid(row=14,column=0)

text14=scrolledtext.ScrolledText(window,wrap=tk.WORD,width=40,height=1)
text14.grid(column=1,row=14,pady=5,padx=5)
ttk.Label(window,text="Download the model .pb file ",background="pink",foreground="red",
          font=("Times new Roman",15)).grid(row=15,column=0)

text15=scrolledtext.ScrolledText(window,wrap=tk.WORD,width=40,height=1)
text15.grid(column=1,row=15,pady=5,padx=5)
ttk.Label(window,text="Download the model .pb file ",background="pink",foreground="red",
          font=("Times new Roman",15)).grid(row=16,column=0)

text16=scrolledtext.ScrolledText(window,wrap=tk.WORD,width=40,height=1)
text16.grid(column=1,row=16,pady=5,padx=5)'''



'''text1.focus()
text2.focus()
text3.focus()
text4.focus()
text5.focus()
text6.focus()
text7.focus()
text8.focus()
text9.focus()
text10.focus()
text11.focus()
text12.focus()
text13.focus()
text14.focus()
text15.focus()
text16.focus()




#from tkinter import messagebox
#messagebox.showinfo('mobilenet', 'message content')
from tkinter import scrolledtext
txt = scrolledtext.ScrolledText(window, width=80,height=50)

#from tkinter import textinsert
#txt = textinsert.TextInsert(window, width=60,height=30)


from tkinter import filedialog

from os import path
files = filedialog.askopenfilenames()

def clicked():
    file = filedialog.askopenfilename(filename= path.filename('C:/Users/deepa/Downloads/Roboflow_tensorflow_object_detection_mobilenet_colab'))

bt=Button(window,text="file",command=clicked)'''










window.mainloop()
