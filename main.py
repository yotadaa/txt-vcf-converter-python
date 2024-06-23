import tkinter as tk
from tkinterdnd2 import TkinterDnD, DND_FILES
from tkinter import ttk, filedialog
import rename

input_files = []

def drop(event):
    # Get the list of files dropped
    file_list = root.tk.splitlist(event.data)
    
    # Filter for text files and add to input_files
    for file in file_list:
        if file.endswith('.txt') and file not in input_files:
            input_files.append(file)
            listbox.insert(tk.END, file)

def select_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if file_path:
        if file_path not in input_files:
            input_files.append(file_path)
            listbox.insert(tk.END, file_path)

def process():
    entry_value = entry.get()
    if entry_value and input_files:
        rename.main(sorted(input_files), entry_value)

def clear_files():
    input_files.clear()
    listbox.delete(0, tk.END)

# Create the main window
root = TkinterDnD.Tk()
root.title("File Processing App")
root.geometry("400x400")

# Create a style object
style = ttk.Style()
style.configure('TButton', font=('Helvetica', 9, 'bold'), foreground='black', background='blue', padding=1)
style.map('TButton', foreground=[('pressed', 'red'), ('active', 'blue')])

# Create a label for the textbox
label = tk.Label(root, text="Enter file path:")
label.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)

# Create an entry widget for text input (single line)
entry = tk.Entry(root, width=40)
entry.grid(row=0, column=1, padx=10, pady=10, sticky=tk.W)

# Create a button to select files manually
select_file_button = ttk.Button(root, text="Select File", command=select_file, style='TButton')
select_file_button.grid(row=0, column=2, padx=10, pady=0)

# Create a listbox to display the dropped files
listbox = tk.Listbox(root, bg="white", fg="black")
listbox.grid(row=1, column=0, columnspan=3, padx=10, pady=(10, 50), sticky=tk.NSEW)  # Span over three columns

# Create a button to process the files and place it at the bottom
process_button = ttk.Button(root, text="Process Files", command=process, style='TButton')
process_button.grid(row=2, column=0, columnspan=3, pady=10)  # Span over three columns

# Create a button to clear the files and place it below the process button
clear_button = ttk.Button(root, text="Clear Files", command=clear_files, style='TButton')
clear_button.grid(row=3, column=0, columnspan=3, pady=10)  # Span over three columns

# Bind the drop event
root.drop_target_register(DND_FILES)
root.dnd_bind('<<Drop>>', drop)

# Configure grid weights to make listbox expandable
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)

# Run the Tkinter event loop
root.mainloop()
