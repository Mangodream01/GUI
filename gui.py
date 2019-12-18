import os
from tkinter import filedialog, IntVar, messagebox
import tkinter as tk
from tkinter import ttk
from year3.plantLab.Rijstproef.renamer_3 import rice_rename
from year3.plantLab.Sojaproef.renamer import soy_rename
from tkinter.ttk import *
from PIL import ImageTk, Image
import time
import warnings
warnings.filterwarnings('ignore')


def main():

    HEIGHT = 700
    WIDTH = 800

    def browse_button1():                                   # check: not empty!
        infile = filedialog.askdirectory()
        pathlabel1.config(text=infile)
        return infile

    def browse_button2():                                   # check: empty!
        filename = filedialog.askdirectory()
        pathlabel2.config(text=filename)
        return filename

    def job(infile, outfile, rice, soy):
        if rice == soy:
            messagebox.showinfo("Error message", "Choose (either) Rice or Soy!")
        else:
            # progress
            size = len(os.listdir(infile)) + 1
            barVar = tk.DoubleVar()
            barVar.set(0)
            progress = Progressbar(lowest_frame, orient='horizontal', length=100, style='black.Horizontal.TProgressbar',
                                   variable=barVar, mode='determinate')
            progress['maximum'] = size
            progress.pack()
            start_time = time.time()

            # renamer
            if rice:
                rice_rename(progress, infile, outfile)
            else:
                soy_rename(progress, infile, outfile)
            end_time = time.time()

            end = tk.Label(end_frame)
            end.config(text="Renaming Completed. (took %i seconds)" % (end_time-start_time), font=("calibri", 12))
            end.place(relwidth=1, relheight=1)

    root = tk.Tk()
    canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
    canvas.pack()

    # image logo
    upper_img = tk.Frame(root)
    upper_img.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')
    img = Image.open("C:/Users/tmdad/Documents/Master/year3/plantLab/lab.png")
    img = img.resize((60, 60), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    logo = tk.Label(upper_img, image=img)
    logo.pack()

    # input
    upper_frame1 = tk.Frame(root)
    upper_frame1.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.1, anchor='n')
    label1 = tk.Label(upper_frame1, text="Select Input Folder: ", font=("calibri", 12, "bold"))
    label1.place(relwidth=1, relheight=1)
    mid1_frame = tk.Frame(root)
    mid1_frame.place(relx=0.5, rely=0.35, relwidth=0.75, relheight=0.1, anchor='n')
    button1 = tk.Button(mid1_frame, text="Browse for folder...",  font=("calibri", 10), bg='lightgray', command=lambda: browse_button1())
    button1.config(borderwidth=0)
    button1.pack()

    # show path----
    mid2_frame = tk.Frame(root)
    mid2_frame.place(relx=0.5, rely=0.4, relwidth=0.75, relheight=0.025, anchor='n')
    pathlabel1 = tk.Label(mid2_frame, font=("calibri", 10))
    pathlabel1.place(relwidth=1, relheight=1)

    # output
    upper_frame2 = tk.Frame(root)
    upper_frame2.place(relx=0.5, rely=0.45, relwidth=0.75, relheight=0.1, anchor='n')
    label2 = tk.Label(upper_frame2, text="Select Output Folder: ", font=("calibri", 12, "bold"))
    label2.place(relwidth=1, relheight=1)
    mid2_frame = tk.Frame(root)
    mid2_frame.place(relx=0.5, rely=0.55, relwidth=0.75, relheight=0.1, anchor='n')
    button2 = tk.Button(mid2_frame, text="Browse for folder...",  font=("calibri", 10), bg='lightgray', command=lambda: browse_button2())
    button2.config(borderwidth=0)
    button2.pack()

    # show path----
    mid2_frame = tk.Frame(root)
    mid2_frame.place(relx=0.5, rely=0.6, relwidth=0.75, relheight=0.025, anchor='n')
    pathlabel2 = tk.Label(mid2_frame, font=("calibri", 10))
    pathlabel2.place(relwidth=1, relheight=1)

    # checkboxes
    check = tk.Frame(root)
    check.place(relx=0.5, rely=0.7, relwidth=0.2, relheight=0.025, anchor='n')
    rice = IntVar()
    soy = IntVar()
    c1 = Checkbutton(check, text="Rice", variable=rice).pack(side=tk.LEFT)
    c2 = Checkbutton(check, text="Soy", variable=soy).pack(side=tk.RIGHT)

    # rename: take text from labels
    lower_frame = tk.Frame(root)
    lower_frame.place(relx=0.5, rely=0.8, relwidth=0.75, relheight=0.1, anchor='n')
    button = tk.Button(lower_frame, text="Rename", bg='lightgray', command=lambda: job(pathlabel1.cget("text"), pathlabel2.cget("text"), rice.get(), soy.get()))
    button.config(borderwidth=0)
    button.pack()

    # progress and completed
    lowest_frame = tk.Frame(root)
    lowest_frame.place(relx=0.5, rely=0.9, relwidth=0.75, relheight=0.1, anchor='n')
    end_frame = tk.Frame(root)
    end_frame.place(relx=0.5, rely=0.91, relwidth=0.75, relheight=0.1, anchor='n')

    root.mainloop()


# Driver Code
if __name__ == '__main__':

    # Calling main() function
    main()


