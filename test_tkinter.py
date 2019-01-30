#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
import sys
from Tkinter import *
import tkMessageBox

class Application(Frame):

  def createWidgets(self):

    self.HELLO = Label(self)
    self.HELLO["text"] = 'NFC読み取り'
    #self.HELLO["foreground"] = '#ff0000'
    #self.HELLO["background"] = '#ffaacc'
    self.HELLO.pack()

    self.INPUT = Entry(self)
    self.INPUT.pack()

    self.VALUE = Label(self)
    self.VALUE["text"] = self.INPUT.get()
    self.VALUE.pack()

    self.QUIT = Button(self)
    self.QUIT["text"] = "終了"
    self.QUIT["fg"]   = "red"
    self.QUIT["command"] =  self.quit
    self.QUIT.pack()




  def __init__(self, master=None):
    Frame.__init__(self, master)
    self.pack()
    self.createWidgets()


if __name__ == "__main__":
  root = Tk()
  app = Application(master=root)
  app.master.title("My Application")
  app.master.geometry("400x300")



  app.mainloop()
  root.destroy
