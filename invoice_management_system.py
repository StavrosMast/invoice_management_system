import tkinter as tk
import customtkinter as ctk
class GUI:
    def __init__(self, title="Invoice Management System", width=800, height=600):
        self.root = ctk.CTk()
        self.root.title(title)
        self.root.geometry(f"{width}x{height}")

        self.create_widgets()

    def create_widgets(self):
        # Create a label
        self.label = ctk.CTkLabel(self.root, text="Upload Invoice")
        self.label.pack()

        # Create a button
        self.button = ctk.CTkButton(self.root, text="Upload", command=self.upload_dialog)
        self.button.pack()

        # Create a button
        self.button = ctk.CTkButton(self.root, text="Quit", command=self.root.destroy)
        self.button.pack()

    def upload_dialog(self):
        print("Button clicked!")

    def run(self):
        self.root.mainloop()

# Create an instance of the GUI class
gui = GUI()
gui.run()