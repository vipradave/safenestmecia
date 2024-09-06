import tkinter as tk

# Function to be called when the button is pressed
def print_message():
    print("I need help.")

# Create the main window
root = tk.Tk()
root.title("Simple GUI")

# Create a button and attach the print_message function to it
button = tk.Button(root, text="Press here", command=print_message)
button.pack(pady=20)  # Add some padding for aesthetics

# Start the main event loop
root.mainloop()