#!/usr/bin/env python
import Tkinter as tk

class Application(tk.Frame):
  def __init__(self, master=None):
    tk.Frame.__init__(self, master)
    self.grid()
    self.createWidgets()

  def createWidgets(self):
    self.uploadButton = tk.Button(self, text='Upload', command=self.upload)
    self.uploadButton.grid()

    self.closeButton = tk.Button(self, text='close', command=master.close)
    self.closeButton.grid()

    self.translate = tk.Text(self, height=3, width=50)

    self.choices = tk.Listbox(self)
    self.choices.insert(1, 'Chinese')
    self.choices.insert(2, 'English')
    self.choices.insert(3, 'Finnish')
    self.choices.insert(4, 'Japanese')
    self.choices.insert(5, 'Spanish')

  def upload(self):
    print("Testing upload button!")


app = Application()
app.mainloop()
