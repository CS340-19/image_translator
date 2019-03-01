#!/usr/bin/env python
import Tkinter as tk

class Application(tk.Frame):
  def __init__(self, master=None):
    tk.Frame.__init__(self, master)

    frame = tk.Frame(width=720, height=480, bg='')
    # frame.pack()

    self.grid(padx=25, pady=25)
    self.createWidgets()

  def createWidgets(self):
    self.translate = tk.Text(self, height=3, width=50)
    self.translate.grid()

    self.uploadButton = tk.Button(self, text='Upload', command=self.upload)
    self.uploadButton.grid(padx=5, pady=5)

    self.button = tk.Button(self, text="QUIT", command=self.quit)
    self.button.grid(padx=5, pady=5)

    self.choices = tk.Listbox(self)
    self.choices.insert(1, 'Chinese')
    self.choices.insert(2, 'English')
    self.choices.insert(3, 'Finnish')
    self.choices.insert(4, 'Japanese')
    self.choices.insert(5, 'Spanish')
    self.choices.grid()

  def upload(self):
    print("Testing upload button!")

app = Application()
app.mainloop()
