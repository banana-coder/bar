import time

def zeitanzeigen():
    lokalzeit = time.localtime()
    zeit_anzeige =str(lokalzeit[3])+":"+str(lokalzeit[4])+":"+str(lokalzeit[5])             # wandelt die zeit in die form HH:MM:SS um
    zeit_anzeige = "11:22:3"
    if zeit_anzeige[1] ==":":
        zeit_anzeige = "0" + zeit_anzeige
    if zeit_anzeige[4] ==":":
        zeit_anzeige = zeit_anzeige[:3]+"0"+zeit_anzeige[3:]
    if len(zeit_anzeige) == 7:
        zeit_anzeige = zeit_anzeige[:6]+"0"+zeit_anzeige[6]
            
    zeitanzeige = Label(frame_clock, text = zeit_anzeige,bg="black",fg = "white", font=("Helvetica", 20))
    zeitanzeige.pack(fill=BOTH, expand = 1)
    print(zeit_anzeige)
    return


#-----------------------------------------------------------------------------------------------------------------------------
#setting up the window

from tkinter import *
fenster = Tk()
fenster.title("GUI")
#Tk.attributes("-fullscreen", True)
fenster.geometry("800x480")

#-----------------------------------------------------------------------------------------------------------------------------
#declare static variables
my_image =PhotoImage(file="/home/oli/Downloads/options.png")		#import the settings-logo



#-----------------------------------------------------------------------------------------------------------------------------
#setting up the frames for clock, list and options

frame_buttons = Frame(width=600, height=480, bg="green")
frame_buttons.place(relx=0, rely=0)
frame_buttons.grid_columnconfigure(0, weight=1)

frame_clock = Frame(width = 200, height = 48, bg = "blue")
frame_clock.place(relx= 0.75, rely=0)
frame_clock.pack_propagate(0)

frame_options = Frame(width = 200, height = 200, bg = "white")
frame_options.place(relx=0.75, rely=0.1)

#-----------------------------------------------------------------------------------------------------------------------------
#

zeitanzeigen()

#-----------------------------------------------------------------------------------------------------------------------------
#setting up the options button

knopf_options = Button(frame_options, text="", bg ="white")
my_image =PhotoImage(file="/home/oli/Downloads/options.png")
knopf_options.config(image= my_image)
knopf_options.pack()



knopf1 = Button(frame_buttons, text="Knopf 1", bg="white",fg = "black", font=("Helvetica", 25), width = 32)
knopf2 = Button(frame_buttons, text="Knopf 2", bg="white",fg = "black", font=("Helvetica", 25), width = 32)
knopf3 = Button(frame_buttons, text="Knopf 3", bg="white",fg = "black", font=("Helvetica", 25), width = 32)
knopf4 = Button(frame_buttons, text="Knopf 4", bg="white",fg = "black", font=("Helvetica", 25), width = 32)

knopf1.grid(row=0)
knopf2.grid(row=1)
knopf3.grid(row=2)
knopf4.grid(row=3)


