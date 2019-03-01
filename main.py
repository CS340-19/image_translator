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
    self.translate.grid(column=1)

    self.choices = tk.Listbox(self)
    self.choices.insert(1, 'Chinese')
    self.choices.insert(2, 'English')
    self.choices.insert(3, 'Finnish')
    self.choices.insert(4, 'Japanese')
    self.choices.insert(5, 'Spanish')
    self.choices.grid(column=1)

    #self.uploadButton = tk.Button(self, text='Browse', command=self.askopenfile)
    #self.uploadButton.grid(row=1, column=2, padx=2, pady=2)

    self.uploadButton = tk.Button(self, text='Upload', command=self.upload)
    self.uploadButton.grid(row=2, column=2, padx=2, pady=2)

    self.button = tk.Button(self, text="QUIT", command=self.quit)
    self.button.grid(row=3, column=2, padx=2, pady=2)

  def askopenfile(self):
    return tk.filedialog.askopenfile(mode='r', **self.file_opt)

  def upload(self):
    try:
        current_selection = self.choices.get(self.choices.curselection())
        print(current_selection)
    except:
        print("No Language Selected!")

    try:
        current_text = self.translate.get("1.0", 'end')
        print(current_text)
    except:
        print("No Text")

app = Application()
app.mainloop()
