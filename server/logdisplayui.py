import tkinter as tk
import requests

def get_logs():
    response = requests.get('http://localhost:5000/logs')
    logs = response.json()
    logs_text.delete("1.0", tk.END)
    logs_text.insert(tk.END, logs)

root = tk.Tk()
root.title("Live Logs")

logs_text = tk.Text(root)
logs_text.pack()

get_logs_button = tk.Button(root, text="Get Logs", command=get_logs)
get_logs_button.pack()

root.mainloop()
