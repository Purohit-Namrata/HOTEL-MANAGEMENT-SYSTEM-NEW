import tkinter as tk

def get_entry_value():
    value = entry.get()
    print("Entry value:", value)

# Create the Tkinter window
window = tk.Tk()
window.title("Entry Widget Value Retrieval")

# Create an Entry widget
entry = tk.Entry(window)
entry.pack()

# Create a button to trigger value retrieval
button = tk.Button(window, text="Get Entry Value", command=get_entry_value)
button.pack()

# Start the Tkinter event loop
window.mainloop()
