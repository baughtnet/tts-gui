import tkinter as tk

def close():
    # Add the functionality for the "Close" button here
    root.destroy()

def speak():
    # Add the functionality for the "Speak" button here
    pass

root = tk.Tk()
root.geometry("800x600")

textbox = tk.Text(root)
textbox.pack()

checkbox = tk.Checkbutton(root)
checkbox.pack(anchor=tk.W)

button_frame = tk.Frame(root)
button_frame.pack(anchor=tk.E)

close_button = tk.Button(button_frame, text="Close", command=close)
close_button.pack(side=tk.LEFT)

speak_button = tk.Button(button_frame, text="Speak", command=speak)
speak_button.pack(side=tk.LEFT)

root.mainloop()
