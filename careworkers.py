from tkinter import *
root = Tk()
class Calculate():
    def __init__(self, parent):
        self.parent = parent
        self.parent.title('Care Workers Payment System')
        self.parent.resizable(0,0)
        self.parent.grid()
        self.parent.geometry("330x380")
        self.parent.configure(background="steel blue")
        self.CreateFrames()
        self.AddLabel()
        self.AddEnts()
        self.AddButtons()

    def Clear1(self, event):
        self.ContactHours.delete(0, END)

    def Clear2(self, event):
        self.ContactMins.delete(0, END)

    def Clear3(self, event):
        self.TravelHours.delete(0, END)

    def Clear4(self, event):
        self.TravelMins.delete(0, END) 
        
    def CreateFrames(self):
        """Create The Frames"""
        self.EntryFrm = Frame(self.parent, bg = "steel blue")
        self.EntryFrm.grid(row = 0, column = 0)
        self.BtnFrm = Frame(self.parent, bg = "steel blue")
        self.BtnFrm.grid(row = 1, column = 0)
        self.Frm = Frame(self.parent, bg = "steel blue")
        self.Frm.grid(row = 2, column = 0)
    def AddEnts(self):
        """Add Entrys"""
        self.ContactHours = Entry(self.EntryFrm, bd = 4, width = 25, font = ("Calibri", 10))
        self.ContactMins = Entry(self.EntryFrm, bd = 4, width = 25, font = ("Calibri", 10))
        self.TravelHours = Entry(self.EntryFrm, bd = 4, width = 25, font = ("Calibri", 10))
        self.TravelMins = Entry(self.EntryFrm, bd = 4, width = 25, font = ("Calibri", 10))
        self.Owed = Entry(self.EntryFrm, bd = 4, width = 25, font = ("Calibri", 10))
        self.ContactHours.insert(END, "Contact Hours")
        self.ContactMins.insert(END, "Contact Mins")
        self.TravelHours.insert(END, "Travel Hours")
        self.TravelMins.insert(END, "Travel Mins")
        self.Owed.insert(END, "Pay Due: ")
        self.ContactHours.bind("<FocusIn>", self.Clear1)
        self.ContactMins.bind("<FocusIn>", self.Clear2)
        self.TravelHours.bind("<FocusIn>", self.Clear3)
        self.TravelMins.bind("<FocusIn>", self.Clear4)
        self.ContactHours.grid(column = 0, row = 1, padx = 70, pady = 10)
        self.ContactMins.grid(column = 0, row = 2, padx = 70, pady = 10)
        self.TravelHours.grid(column = 0, row = 3, padx = 70, pady = 10)
        self.TravelMins.grid(column = 0, row = 4, padx = 70, pady = 10)
        self.Owed.grid(column = 0, row = 5, padx = 70, pady = 10)
    def AddLabel(self):
        """Add Label"""
        self.WelcomeLbl = Label(self.EntryFrm, text = "Welcome to the Carer's payment System!", bg = "steel blue", font = ("Calibri", 12))
        self.WelcomeLbl2 = Label(self.Frm, text = "Oscar Meanwell Software", bg = "steel blue", font = ("Calibri", 12))
        
        self.WelcomeLbl.grid(column = 0, row = 0, padx = 10, pady = 10)
        self.WelcomeLbl2.grid(column = 0, row = 0, padx = 10, pady = 10)

    def AddButtons(self):
        """Add Button"""
        self.Calculate = Button(self.BtnFrm, text = "Calculate", height = 2, width = 10, fg = "black", activebackground = "yellow", bg = "light blue", command = self.Calc)
        self.Reset = Button(self.BtnFrm, text = "Reset", height = 2, width = 10, fg = "black", activebackground = "yellow", bg = "light blue", command = self.Reset)
        self.Calculate.grid(row = 3, column = 0, padx = 10, pady = 10)
        self.Reset.grid(row = 3, column = 1, padx = 10, pady = 10)
        
    def Calc(self):
        self.ContHours = self.ContactHours.get()
        self.ContMins = self.ContactMins.get()
        self.Thours = self.TravelHours.get()
        self.TMins = self.TravelMins.get()
        self.Hold = '0.' + self.ContHours
        self.Hold_2 = '0.' + self.TMins
        self.Option_1 = (float(self.ContHours) + float(self.Hold)) * 7.20
        self.Option_2 = ((float(self.Thours) + float(self.Hold_2)) + (float(self.ContHours) + float(self.Hold))) * 6.50
        self.Owed.delete(0, END)
        if self.Option_1 >= self.Option_2:
            self.Owed.insert(END, "Pay Due: " + "£" + str(int(self.Option_1)))
            print("\nPay is: " + "£" + str(self.Option_1))
        else:
            self.Owed.insert(END, "Pay Due: " + "£" + str(int(self.Option_2)))
            print("\nPay is: " + "£" + str(self.Option_2))

    def Reset(self):
        self.ContactHours.delete(0, END)
        self.ContactMins.delete(0, END)
        self.TravelHours.delete(0, END)
        self.TravelMins.delete(0, END)
        self.Owed.delete(0, END)
        self.ContactHours.insert(END, "Contact Hours")
        self.ContactMins.insert(END, "Contact Mins")
        self.TravelHours.insert(END, "Travel Hours")
        self.TravelMins.insert(END, "Travel Mins")
        self.Owed.insert(END, "Pay Due: ")

calculate = Calculate(root)
root.mainloop()
