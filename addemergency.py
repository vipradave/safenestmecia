import tkinter as tk
from tkinter import messagebox

class Emergency_contact:
    def __init__(self, root):
        self.root = root
        self.root.title("Emergency Contacts")
        
        # Frame for the contact
        self.contact_frame = tk.Frame(self.root)
        self.contact_frame.pack(pady=10)
        
        # Listbox to display contact
        self.contact_listbox = tk.Listbox(self.contact_frame, width=50, height=15, selectmode=tk.SINGLE)
        self.contact_listbox.pack(side=tk.LEFT, fill=tk.BOTH)
        
        # Scrollbar for the listbox
        self.scrollbar = tk.Scrollbar(self.contact_frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)
        
        self.contact_listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.contact_listbox.yview)
        
        # Entry box to add new contacts
        self.entry_contact = tk.Entry(self.root, width=50)
        self.entry_contact.pack(pady=10)
        
        # Button to add contacts
        self.add_button = tk.Button(self.root, text="Add Contact", command=self.add_contact)
        self.add_button.pack(pady=5)
        
        # Button to delete contacts
        self.delete_button = tk.Button(self.root, text="Delete Contact", command=self.delete_contact)
        self.delete_button.pack(pady=5)

    def add_contact(self):
        contact = self.entry_contact.get()
        if contact != "":
            self.contact_listbox.insert(tk.END, contact)
            self.entry_contact.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You must enter a contact.")

    def delete_contact(self):
        try:
            selected_contact_index = self.contact_listbox.curselection()[0]
            self.contact_listbox.delete(selected_contact_index)
        except IndexError:
            messagebox.showwarning("Warning", "You must select a contactxxxxxxxx to delete.")


if __name__ == "__main__":
    root = tk.Tk()
    app = Emergency_contact(root)
    root.mainloop()
