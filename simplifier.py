import tkinter as tk
from tkinter import filedialog, messagebox
from utils.file_operations import save_file, load_file
from utils.reminder import set_alarm

# Main application window
root = tk.Tk()
root.title("Simplifier - Notepad with Reminders")
root.geometry("600x400")

# Text area for the Notepad
text_area = tk.Text(root, wrap="word", font=("Arial", 12))
text_area.pack(expand=True, fill="both")

# File Menu Functions
def save():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                             filetypes=[("Text Files", "*.txt"),
                                                        ("All Files", "*.*")])
    if file_path:
        save_file(file_path, text_area.get("1.0", tk.END))

def load():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"),
                                                      ("All Files", "*.*")])
    if file_path:
        content = load_file(file_path)
        text_area.delete("1.0", tk.END)
        text_area.insert("1.0", content)

# Add Menu Bar
menu_bar = tk.Menu(root)
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Save", command=save)
file_menu.add_command(label="Load", command=load)
menu_bar.add_cascade(label="File", menu=file_menu)

# Reminder Section
alarm_label = tk.Label(root, text="Set Alarm (YYYY-MM-DD HH:MM:SS):", font=("Arial", 10))
alarm_label.pack(pady=5)

alarm_entry = tk.Entry(root, font=("Arial", 12), width=30)
alarm_entry.pack(pady=5)

set_alarm_button = tk.Button(root, text="Set Alarm",
                              command=lambda: set_alarm(alarm_entry.get()),
                              font=("Arial", 10))
set_alarm_button.pack(pady=10)

root.config(menu=menu_bar)

# Run the app
if __name__ == "__main__":
    root.mainloop()
