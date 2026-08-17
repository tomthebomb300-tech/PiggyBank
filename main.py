import tkinter as tk

from dataManager import getFinances

window = None

def createWindow():
    window = tk.Tk();
    window.title("Finances")
    window.geometry("1000x700")

    window.mainloop()

def main():
    # finances = getFinances()
    createWindow()
    

main()
