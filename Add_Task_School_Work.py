import tkinter as tk
import tkinter.font as font
from PIL import Image, ImageTk
import QuikSpace as qs
import School_Work as sw
from mysql.connector import connect

window=""

def quikSpace():
    global window
    window.destroy()
    qs.quikspace()
   
def school_work():
    global window
    window.destroy()
    sw.school_Work()

def add_task_school_work():
    global window
    window=tk.Tk()
    window.geometry("780x670")
    window.resizable(0,0)
    window.title("School/Work")
    window.config(bg="#FFD9B3")

    font1=font.Font(family="Times New Roman",size=35,weight='bold')#Created the font
    font2=font.Font(family="Times New Roman",size=15)#Created the font
    font3=font.Font(family="Courier New",size=17)

    title=tk.Label(window, text="QuikSpace",font=font1, bg="#FFD9B3")#Created the title
    title.place(x=260,y=25)

    image=Image.open("Scheduler/logo.png")#Loads the image in RAM
    image=image.resize((90,60))
    photo=ImageTk.PhotoImage(image)#Converts the image into the Tkinter image format
    image_label=tk.Label(window,image=photo)
    image_label.place(x=440,y=20)

    slogan=tk.Label(window, text="All your tasks, in one app", font=font2, bg="#FFD9B3")
    slogan.place(x=315,y=90)

    name_task=tk.Entry(window)
    name_task.place(x=313,y=165)

    date_task=tk.Entry(window)
    date_task.place(x=313,y=240)
   
    Name=tk.Label(window, text="Name", font=font2, bg="#FFD9B3")
    Name.place(x=268, y=167)
    
    name=name_task.get()
    
    Date=tk.Label(window, text="Date", font=font2, bg="#FFD9B3")
    Date.place(x=275, y=242)
    
    date=date_task.get()

    Add_Task=tk.Button(window, text="Add Task", width=25, height=3, highlightbackground="#B3D9FF",fg="white",command=addtasksw)
    Add_Task.place(x=284,y=312)

    main_menu=tk.Button(window, text="Main Menu", width=25, height=3, highlightbackground="#B3D9FF",fg="white",command=quikSpace)
    main_menu.place(x=284,y=423)

    back=tk.Button(window, text="Back", width=25, height=3, highlightbackground="#B3D9FF",fg="white",command=school_work)
    back.place(x=284,y=534)

    label=tk.Label(window, text="Add New Task For School/Work", font=font2, bg="#FFD9B3")
    label.place(x=295,y=645)

    window.mainloop()
   
def addtasksw():
    global name,date
    mydb=connect(host="localhost",user="root",password="12345678",database="Programming")
    db_cursor=mydb.cursor()
    insert_query="insert into QuikSpace(Name,Date)Values(%s,%s)"
    
    data = [(name,date)]
       
    db_cursor.execute(insert_query,data)