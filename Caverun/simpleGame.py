#import tkinter as tk
#from tkinter import filedialog, Text
#import os
import sys


#GUI example
#def addApp():
    #GUI examplefilename = filedialog.askopenfilename(initialdir = "/", title = "Select File", filetypes=(("executables", "*.exe"),("all files","*.*")))
                                                                                                    

    


#root = tk.Tk()
#canvas = tk.Canvas(root, height=700, width=700, bg="#263D42")
#canvas.pack()
#frame = tk.Frame(root, bg = "white")
#frame.place(relwidth = 0.8, relheight = 0.8, relx = 0.1, rely = 0.1)
#openFile = tk.Button(root, text="Open File", padx = 10, pady = 5, fg = "white", bg = "#263D42", command =addApp)
#openFile.pack()
#runApps = tk.Button(root, text="Run Apps", padx = 10, pady = 5, fg = "white", bg = "#263D42")
#runApps.pack()
#root.mainloop()


print("Welcome to my game. Type 'inspect' to gather hints about your surroundings.")

val = ""
while(val !="leave cave"):	
  val = input("What do you want to do?")
  
  if val == "inspect":
   print("You are in a cave (leave cave)")
  
  elif val == "leave cave":
    print("You leave the cave")

  else:
    print("Not a valid command")

val = ""
while(val !="follow path"):
  val = input("What do you want to do?")

  if val == "inspect":
   print("You are at the base of the hill. There is a path (follow path).")

  elif val == "follow path":
    print("You follow the path")

  else:
    print("Not a valid command")


val = ""
have_key = False

while not(have_key == True and val == "open gate"):
    val = input("What do you want to do?")
   
  
    if (val == "inspect" and have_key == False):
        print("There is a gate. A key is hidden in the grass. (grab key) (open gate)")
      
    elif (val == "inspect" and have_key == True):
       print("There is a gate. Maybe you could try this key... (open gate)")
      
    elif (val == "grab key" and have_key == True):
        print("You already grabbed the key. (open gate)")

    elif (val == "grab key" and have_key == False):
        have_key = True
        print("You grabbed the key.")
      
    elif val == "open gate":
        if have_key == True:
            print("You have opened the gate and escaped.")
        else:
            print("The gate is locked. (grab key)")
    else:
        print("Not a valid command")
            
print("You win!")




