import tkinter as tk
import tkinter.font as font
from PIL import Image, ImageTk
import QuikSpace as qs
import Add_Task_School_Work as atsw
import Review_Task_School_Work as rtsw

window=""

def quikSpace():
    global window
    window.destroy()
    qs.quikspace()

def ADD_Task_School_Work():
    global window
    window.destroy()
    atsw.add_task_school_work()
    
def Review_Task_School_Work():
    global window
    window.destroy()
    rtsw.review_task_school_work()
    
def school_Work():
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

    add_task=tk.Button(window, text="Add Task",width=25, height=5, highlightbackground="#B3D9FF",fg="white",command=ADD_Task_School_Work)
    add_task.place(x=285,y=170)

    review_tasks=tk.Button(window, text="Review Tasks",width=25, height=5, highlightbackground="#B3D9FF",fg="white",command=Review_Task_School_Work)
    review_tasks.place(x=285,y=320)

    main_menu=tk.Button(window, text="Main Menu",width=25, height=5, highlightbackground="#B3D9FF",fg="white",command=quikSpace)
    main_menu.place(x=285,y=470)

    label=tk.Label(window, text="School/Work", font=font2, bg="#FFD9B3")
    label.place(x=360,y=645)

    credits=tk.Label(window, text="Created By: Smyan and Rithwik", font=font3, bg="#FFD9B3")
    credits.place(x=470,y=640)

    window.mainloop()