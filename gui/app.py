import tkinter as tk

from gui.main_window import MainWindow


def run_app():
    root = tk.Tk()
    app = MainWindow(master=root)
    app.mainloop()
