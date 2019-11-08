from tkinter import filedialog, StringVar
import tkinter as tk
from plantLab.Rijstproef.renamer import rename
from tkinter.ttk import *
import threading, time


def main():

    HEIGHT = 700
    WIDTH = 800
    global my_input
    global filename

    def browse_button1():                                   # check: not empty!
        infile = filedialog.askdirectory()
        pathlabel1.config(text=infile)
        return infile

    def browse_button2():                                   # check: empty!
        filename = filedialog.askdirectory()
        pathlabel2.config(text=filename)
        return filename

    def job(infile, outfile):
        rename(infile, outfile)

        # somehow call progress i/size % 10 == 0


    root = tk.Tk()
    canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
    canvas.pack()

    # input
    upper_frame1 = tk.Frame(root)
    upper_frame1.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')
    label1 = tk.Label(upper_frame1, text="Select Input Folder: ", font=11)
    label1.place(relwidth=1, relheight=1)
    mid1_frame = tk.Frame(root)
    mid1_frame.place(relx=0.5, rely=0.2, relwidth=0.75, relheight=0.1, anchor='n')
    button1 = tk.Button(mid1_frame, text="Browse for folder...", bg='lightgray', command=lambda: browse_button1())
    button1.pack()

    # show path----
    mid2_frame = tk.Frame(root)
    mid2_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.025, anchor='n')
    pathlabel1 = tk.Label(mid2_frame)
    pathlabel1.place(relwidth=1, relheight=1)

    # output
    upper_frame2 = tk.Frame(root)
    upper_frame2.place(relx=0.5, rely=0.4, relwidth=0.75, relheight=0.1, anchor='n')
    label2 = tk.Label(upper_frame2, text="Select Output Folder: ", font=11)
    label2.place(relwidth=1, relheight=1)
    mid2_frame = tk.Frame(root)
    mid2_frame.place(relx=0.5, rely=0.5, relwidth=0.75, relheight=0.1, anchor='n')
    button2 = tk.Button(mid2_frame, text="Browse for folder...", bg='lightgray', command=lambda: browse_button2())
    button2.pack()

    # show path----
    mid2_frame = tk.Frame(root)
    mid2_frame.place(relx=0.5, rely=0.55, relwidth=0.75, relheight=0.025, anchor='n')
    pathlabel2 = tk.Label(mid2_frame)
    pathlabel2.place(relwidth=1, relheight=1)

    # rename: take text from labels
    lower_frame = tk.Frame(root)
    lower_frame.place(relx=0.5, rely=0.6, relwidth=0.75, relheight=0.1, anchor='n')
    button = tk.Button(lower_frame, text="Rename", bg='lightgray', command=lambda: job(pathlabel1.cget("text"), pathlabel2.cget("text")))
    button.pack()

    # if clicked show progress bar
    # lowest_frame = tk.Frame(root)
    # lowest_frame.place(relx=0.5, rely=0.7, relwidth=0.75, relheight=0.1, anchor='n')
    # barVar = tk.DoubleVar()
    # barVar.set(0)
    # progress = Progressbar(lowest_frame, orient='horizontal', length=100, style='black.Horizontal.TProgressbar', variable=barVar, mode='determinate')
    # progress.pack()

    # if completed show text
    text = "Renaming Completed."
    root.mainloop()


# Driver Code
if __name__ == '__main__':

    # Calling main() function
    main()


