import time
from tkinter import *
from customtkinter import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import customtkinter
import matplotlib.pyplot as plt

app = CTk()
plt.imshow([[(100, 0, 50)]])
plt.show()
customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")


# Define some variables that is going to be usefull in feature
BG_GRAY = "#ABB2B9"
BG_COLOR = "#17202A"
TEXT_COLOR = "#EAECEE"
FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 13 bold"

# Customizable
frame_1 = customtkinter.CTkFrame(master=app,fg_color=BG_COLOR)
frame_1.pack(pady=20, padx=60, fill="both", expand=True)

head_label = Label(master=frame_1, bg=BG_COLOR, fg=TEXT_COLOR,text="RGB Color Projector", font=FONT_BOLD, pady=10)
head_label.pack(pady=30,padx=60)

app.geometry("700x700")
app.configure(bg="black")
red_var= IntVar()
blue_var = IntVar()
green_var = IntVar()

red_entry = CTkEntry(master=frame_1,placeholder_text="Enter Red values",placeholder_text_color="red",bg_color="grey",textvariable=red_var,text_color="red",font=CTkFont(FONT))

red_entry.pack(pady=30,padx=40)
green_entry = CTkEntry(master=frame_1,placeholder_text="Enter Green values",placeholder_text_color="green",bg_color="grey",textvariable=green_var,text_color="green",font=CTkFont(FONT))
green_entry.pack(pady=30,padx=40)
blue_entry = CTkEntry(master=frame_1,placeholder_text="Enter Blue values",placeholder_text_color="blue",bg_color="grey",textvariable=blue_var,text_color="blue",font=CTkFont(FONT))
blue_entry.pack(pady=30,padx=40)


# MAIN function
def plotter():
    fig = Figure(figsize=(5, 5),
                 dpi=100)
    r = red_entry.get()
    g = green_entry.get()
    b = blue_entry.get()
    time.sleep(1)
    r = float(r)
    g = float(g)
    b = float(b)
    # list of squares]


    # adding the subplot
    plot1 = fig.add_subplot(111)

    # plotting the graph
    plot1.imshow([[(r,g,b)]])

    # creating the Tkinter canvas
    # containing the Matplotlib figure
    canvas = FigureCanvasTkAgg(fig,
                               master=app)
    canvas.draw()

    # placing the canvas on the Tkinter window
    canvas.get_tk_widget().pack()
    #plt.imshow([[(r, g, b)]])
    #plt.show()
button = CTkButton(master=frame_1,command=plotter,text="Plot")
button.pack(pady=30,padx=40)



app.mainloop()