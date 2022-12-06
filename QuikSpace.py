import tkinter as tk
import tkinter.font as font
from PIL import Image, ImageTk
import School_Work as sw

window =""
print(tk.TkVersion)
def school_work():
    global window
    window.destroy()
    sw.school_Work()

def quikspace():
    global window
    window=tk.Tk()
    window.geometry("780x670")
    window.resizable(0,0)
    window.title("QuikSpace")
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

    school_work_button=tk.Button(text="School/Work", highlightbackground="#B3D9FF",fg="white",width=40,height=5,command=school_work)
    school_work_button.place(x=215,y=150)

    activities_button=tk.Button(text="Activities", highlightbackground="#B3D9FF",fg="white",width=40,height=5)
    activities_button.place(x=215,y=325)

    home_button=tk.Button(text="Home", highlightbackground="#B3D9FF",fg="white",width=40,height=5)
    home_button.place(x=215,y=500)

    credits=tk.Label(window, text="Created By: Smyan and Rithwik", font=font3, bg="#FFD9B3")
    credits.place(x=470,y=640)

    window.mainloop()
    
if __name__=='__main__':
    quikspace()