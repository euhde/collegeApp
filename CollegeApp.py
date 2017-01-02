from tkinter import *

class Application(Frame):

    def __init__ (self, master):
        Frame.__init__(self, master)
        self.grid()
        self.create_widget()

    def create_widget(self):
        Label(self, text='Enter student information.').grid(row=0, column=0, columnspan=3, sticky=S)
        Label(self, text='Student Name:').grid(row = 1, column=0, sticky=W)
        Label(self, text='GPA:').grid(row=2, column=0, sticky=W)
        Label(self, text='Essay:').grid(row=3, column=0, sticky=W)

        self.student_name = Entry (self, width = 40)
        self.student_name.grid (row=1, column=1, columnspan=2, sticky=W)

        self.student_gpa = Entry (self, width=40)
        self.student_gpa.grid(row=2, column=1, columnspan=2, sticky=W)

        self.essay = Text (self, width = 50, height = 10, wrap = WORD)
        self.essay.grid(row=4, column =0, columnspan = 3, sticky = W)

        Button (self, text = 'Save', command = self.save).grid (row=5, column=0, columnspan = 2, sticky = S)
        Button (self, text = 'Clear', command=self.clear).grid(row=5, column=2, sticky=W)

    def clear(self):
        self.student_name.delete(0, END)
        self.student_gpa.delete(0, END)
        self.essay.delete(0.0, END)

    def save(self):
        try:
            write_file = open("applications.txt", "a")
            write_file.write(self.student_name.get() + "\t")
            write_file.write(self.student_gpa.get() + "\t")
            write_file.write(self.essay.get(0.0, END))
            write_file.write("\n")
            write_file.close()
        except:
            self.essay.delete(0.0, END)
            self.essay.insert(0.0, "Error writing to file.")
        
# main
root = Tk()
root.title("College Application")
root.geometry("410x280")

app = Application(root)
root.mainloop()
