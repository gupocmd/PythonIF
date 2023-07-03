import tkinter as tk
from tkinter import filedialog
import os

def browse_folder():
    folder_path = filedialog.askdirectory()
    if folder_path:
        listbox.delete(0, tk.END)
        for filename in os.listdir(folder_path):
            listbox.insert(tk.END, filename)

root = tk.Tk()
root.title("Navegador de Arquivos")

frame = tk.Frame(root)
frame.pack(pady=20)

browse_button = tk.Button(frame, text="Navegar", command=browse_folder)
browse_button.pack(side=tk.LEFT)

listbox = tk.Listbox(root, width=50)
listbox.pack()

root.mainloop()