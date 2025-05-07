import os
import tkinter as tk
from tkinter import PhotoImage, filedialog, messagebox
from tkinter.ttk import Button, Entry, Label


class MainWindow(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master.title("Audio Sanitizer")
        self.master.geometry("400x140")
        self.master.resizable(False, False)
        self.pack(padx=15, pady=15)
        self.master.iconphoto(True, PhotoImage(file="gui\\assets\\mixing-table.png"))

        self.input_file = ""
        self.output_dir = ""

        Label(self, text="Input File:").grid(row=0, column=0, sticky="w", pady=5)
        self.input_entry = Entry(self, width=30)
        self.input_entry.grid(row=0, column=1, sticky="w")
        Button(self, text="Select", width=12, command=self.select_input).grid(
            row=0, column=2, padx=(5, 0)
        )

        Label(self, text="Output Folder:").grid(row=1, column=0, sticky="w", pady=5)
        self.output_entry = Entry(self, width=30)
        self.output_entry.grid(row=1, column=1, sticky="w")
        Button(self, text="Select", width=12, command=self.select_output_dir).grid(
            row=1, column=2, padx=(5, 0)
        )

        Button(self, text="Remove Silence", command=self.process).grid(
            row=2, column=0, columnspan=3, pady=15
        )

    def select_input(self):
        path = filedialog.askopenfilename(filetypes=[("MP3 files", "*.mp3")])
        if path:
            self.input_file = path
            self.input_entry.delete(0, tk.END)
            self.input_entry.insert(0, path)

    def select_output_dir(self):
        path = filedialog.askdirectory()
        if path:
            self.output_dir = path
            self.output_entry.delete(0, tk.END)
            self.output_entry.insert(0, path)

    def get_unique_filename(self, directory, base_name):
        name, ext = os.path.splitext(base_name)
        candidate = f"{name}_cleaned{ext}"
        counter = 1
        while os.path.exists(os.path.join(directory, candidate)):
            candidate = f"{name}_cleaned_{counter}{ext}"
            counter += 1
        return os.path.join(directory, candidate)

    def process(self):
        if not self.input_file or not self.output_dir:
            messagebox.showerror(
                "Error", "Please select both input file and output folder."
            )
            return

        base_name = os.path.basename(self.input_file)
        output_file = self.get_unique_filename(self.output_dir, base_name)

        from services.audio_processor import remove_silence

        success, message = remove_silence(self.input_file, output_file)
        if success:
            messagebox.showinfo("Success", f"{message}\nSaved to:\n{output_file}")
        else:
            messagebox.showerror("Error", message)
