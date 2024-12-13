import os
import tkinter as tk
from tkinter import simpledialog, messagebox, filedialog
import subprocess

def rename_files():
    # Create the Tkinter root window (invisible)
    root = tk.Tk()
    root.withdraw()  # Hide the root window as we only need dialogs

    # Show the welcome dialog
    messagebox.showinfo("Welcome", "Welcome to the Image Renamer! Let's get started.")
    
    # Prompt user for folder location using a file dialog
    folder_path = filedialog.askdirectory(title="Select Folder Containing Images")
    
    # Check if the directory exists
    if not folder_path:
        messagebox.showerror("Error", "No folder selected. Exiting.")
        return

    # Prompt user for starting number
    start_number = simpledialog.askinteger("Starting Number", "Enter the starting number for image naming:")

    if start_number is None:  # User cancelled input
        messagebox.showerror("Error", "Invalid input. Exiting.")
        return

    # Get a list of files in the directory
    files = sorted(os.listdir(folder_path))

    # Filter files to include only images (by common extensions)
    image_extensions = {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".webp"}
    images = [f for f in files if os.path.splitext(f)[1].lower() in image_extensions]

    if not images:
        messagebox.showerror("Error", "No image files found in the specified directory.")
        return

    # Rename files
    for count, filename in enumerate(images, start=start_number):
        old_path = os.path.join(folder_path, filename)
        new_name = f"image{count}{os.path.splitext(filename)[1].lower()}"
        new_path = os.path.join(folder_path, new_name)

        try:
            os.rename(old_path, new_path)
            print(f"Renamed: {filename} -> {new_name}")  # Log in PowerShell/console
        except Exception as e:
            print(f"Failed to rename {filename}: {e}")  # Log errors in PowerShell/console

    # Display success message and open the folder
    messagebox.showinfo("Success", "All files have been renamed successfully!")
    
    # Open the folder in the default file explorer
    subprocess.Popen(f'explorer "{folder_path}"')

if __name__ == "__main__":
    rename_files()
