from tkinter import Tk, Frame, BOTH
from tkinter.ttk import Button
import tkinter.messagebox as mbox

class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title("Message Boxes")
        self.pack(fill=BOTH, expand=True)

        error = Button(self, text="Error", command=self.onError)
        error.grid(row=0, column=0, padx=5, pady=5)

        warning = Button(self, text="Warning", command=self.onWarn)
        warning.grid(row=1, column=0, padx=5, pady=5)

        question = Button(self, text="Question", command=self.onQuest)
        question.grid(row=0, column=1, padx=5, pady=5)

        inform = Button(self, text="Information", command=self.onInfo)
        inform.grid(row=1, column=1, padx=5, pady=5)

    def onError(self):
        mbox.showerror("Error", "Could not open file")

    def onWarn(self):
        mbox.showwarning("Warning", "Deprecated function call")

    def onQuest(self):
        response = mbox.askquestion("Question", "Are you sure to quit?")
        if response == "yes":
            self.parent.quit()

    def onInfo(self):
        mbox.showinfo("Information", "Download completed")

root = Tk()
root.geometry("300x150+600+300")
app = Example(root)
root.mainloop()
