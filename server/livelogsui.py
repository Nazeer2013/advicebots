import tkinter as tk
import requests

class StreamLogDisplay(tk.Tk):
    def __init__(self, logs):
        tk.Tk.__init__(self)
        self.title("Live Stream Logs")
        self.logs = logs
        self.text = tk.Text(self)
        self.text.pack()
        self.update_logs()

    def update_logs(self):
        for log in self.logs:
            self.text.insert("end", log , "\n")
        self.after(1000, self.update_logs)

def get_logs():
    response = requests.get('http://localhost:5000/logs')
    logs = response.json()
    # logs_text.delete("1.0", tk.END)
    # logs_text.insert(tk.END, logs)
    return logs

'''
    root = tk.Tk()
    root.title("Live Logs")

    logs_text = tk.Text(root)
    logs_text.pack()

    get_logs_button = tk.Button(root, text="Get Logs", command=get_logs)
    get_logs_button.pack()
'''


if __name__ == "__main__":
    logs = get_logs() # replace this with your list of logs
    app = StreamLogDisplay(logs)
    app.mainloop()
