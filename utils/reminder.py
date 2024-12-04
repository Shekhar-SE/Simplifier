from datetime import datetime
import threading
from tkinter import messagebox

def set_alarm(alarm_time):
    """Set an alarm to trigger at the specified time."""
    try:
        alarm_datetime = datetime.strptime(alarm_time, "%Y-%m-%d %H:%M:%S")
        delay = (alarm_datetime - datetime.now()).total_seconds()
        if delay > 0:
            threading.Timer(delay, show_reminder).start()
            messagebox.showinfo("Alarm Set", f"Alarm set for {alarm_datetime}")
        else:
            messagebox.showwarning("Invalid Time", "The time has already passed!")
    except ValueError:
        messagebox.showerror("Invalid Format", "Use the format: YYYY-MM-DD HH:MM:SS")

def show_reminder():
    """Display a reminder pop-up."""
    messagebox.showinfo("Reminder", "It's time for your reminder!")
