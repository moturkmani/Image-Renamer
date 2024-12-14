import os
import tkinter as tk
from tkinter import simpledialog, messagebox, filedialog
import subprocess

def rename_files():
    # Create the Tkinter root window
    root = tk.Tk()
    root.withdraw()  # Hide the root window as we only need dialogs

    # Configure font size and window scaling
    root.option_add("*Font", "Helvetica 18")
    root.geometry("600x400")  # Set a larger window size

    def create_colored_dialog(title, message, button_text, button_color, cancel_text=None, cancel_color=None):
        """Create a dialog with colored buttons and ensure Enter key works."""
        dialog = tk.Toplevel(root)
        dialog.title(title)
        dialog.geometry("600x200")

        # Center the dialog on the screen
        screen_width = dialog.winfo_screenwidth()
        screen_height = dialog.winfo_screenheight()
        x = (screen_width // 2) - (600 // 2)
        y = (screen_height // 2) - (200 // 2)
        dialog.geometry(f"600x200+{x}+{y}")

        label = tk.Label(
            dialog,
            text=message,
            font=("Helvetica", 18),
            wraplength=500,
            justify="center"
        )
        label.pack(pady=20, padx=20)

        button_frame = tk.Frame(dialog)
        button_frame.pack(pady=10)

        # OK Button
        ok_button = tk.Button(
            button_frame,
            text=button_text,
            command=dialog.destroy,
            font=("Helvetica", 18),
            bg=button_color,
            fg="white"
        )
        ok_button.pack(side="left", padx=10)

        # Bind Enter key to the OK button
        dialog.bind("<Return>", lambda _: ok_button.invoke())
        ok_button.focus_set()

        dialog.grab_set()
        root.wait_window(dialog)

    # Create a custom messagebox for the welcome dialog
    create_colored_dialog(
        "Welcome",
        "Welcome to the Image Renamer!\nLet's get started.",
        "OK",
        "green"
    )

    # Prompt user for ascending or descending order
    def get_order():
        order_dialog = tk.Toplevel(root)
        order_dialog.title("Order Selection")
        order_dialog.geometry("600x200")

        # Center the dialog on the screen
        screen_width = order_dialog.winfo_screenwidth()
        screen_height = order_dialog.winfo_screenheight()
        x = (screen_width // 2) - (600 // 2)
        y = (screen_height // 2) - (200 // 2)
        order_dialog.geometry(f"600x200+{x}+{y}")

        label = tk.Label(
            order_dialog,
            text="Would you like to rename images in ascending or descending order?",
            font=("Helvetica", 18),
            wraplength=500,
            justify="center"
        )
        label.pack(pady=20, padx=20)

        def set_order(order):
            nonlocal order_option
            order_option = "ascending" if order == 1 else "descending"
            order_dialog.destroy()

        button_frame = tk.Frame(order_dialog)
        button_frame.pack(pady=10)

        ascending_button = tk.Button(
            button_frame,
            text="Ascending",
            command=lambda: set_order(1),
            font=("Helvetica", 18),
            bg="green",
            fg="white"
        )
        ascending_button.pack(side="left", padx=10)

        descending_button = tk.Button(
            button_frame,
            text="Descending",
            command=lambda: set_order(2),
            font=("Helvetica", 18),
            bg="red",
            fg="white"
        )
        descending_button.pack(side="left", padx=10)

        ascending_button.bind("<Return>", lambda _: set_order(1))  # Bind Enter key
        ascending_button.focus_set()  # Set focus to the button

        order_dialog.grab_set()
        root.wait_window(order_dialog)

    order_option = None
    get_order()

    if order_option not in {"ascending", "descending"}:  # Invalid input
        messagebox.showerror("Error", "Invalid option selected. Exiting.")
        return

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

    # Prompt user for renaming convention
    def get_rename_option(order_option):
        rename_dialog = tk.Toplevel(root)
        rename_dialog.title("Renaming Convention")
        rename_dialog.geometry("600x300")

        # Center the dialog on the screen
        screen_width = rename_dialog.winfo_screenwidth()
        screen_height = rename_dialog.winfo_screenheight()
        x = (screen_width // 2) - (600 // 2)
        y = (screen_height // 2) - (300 // 2)
        rename_dialog.geometry(f"600x300+{x}+{y}")

        if order_option == "ascending":
            label_text = (
                "Choose a renaming convention:\n"
                "1. image1, image2, image3\n"
                "2. img_01, img_02, img_03\n"
                "3. image0001, image0002, image0003\n"
            )
        else:
            label_text = (
                "Choose a renaming convention:\n"
                "1. image3, image2, image1\n"
                "2. img_03, img_02, img_01\n"
                "3. image0003, image0002, image0001\n"
            )

        label = tk.Label(
            rename_dialog,
            text=label_text,
            font=("Helvetica", 16),
            wraplength=500,
            justify="center"
        )
        label.pack(pady=20, padx=20)

        entry_var = tk.StringVar()
        entry_box = tk.Entry(
            rename_dialog,
            textvariable=entry_var,
            font=("Helvetica", 18),
            justify="center"
        )
        entry_box.pack(pady=10)
        entry_box.focus_set()  # Focus on the input box

        def submit():
            nonlocal rename_option
            try:
                rename_option = int(entry_var.get())
                if rename_option in {1, 2, 3}:
                    rename_dialog.destroy()
                else:
                    raise ValueError
            except ValueError:
                messagebox.showerror("Error", "Please enter a valid option: 1, 2, or 3.")

        submit_button = tk.Button(
            rename_dialog,
            text="OK",
            command=submit,
            font=("Helvetica", 18),
            bg="green",
            fg="white"
        )
        submit_button.pack(pady=10)

        # Bind Enter key to the Submit button
        rename_dialog.bind("<Return>", lambda _: submit())

        rename_dialog.grab_set()
        root.wait_window(rename_dialog)

    rename_option = None
    get_rename_option(order_option)

    if rename_option not in {1, 2, 3}:
        messagebox.showerror("Error", "Invalid renaming option selected. Exiting.")
        return

    # Get a list of files in the directory
    files = sorted(os.listdir(folder_path))

    # Filter files to include only images (by common extensions)
    image_extensions = {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".webp"}
    images = [f for f in files if os.path.splitext(f)[1].lower() in image_extensions]

    if not images:
        messagebox.showerror("Error", "No image files found in the specified directory.")
        return

    # Define renaming patterns based on user selection
    if rename_option == 1:
        name_pattern = lambda count: f"image{count}"
    elif rename_option == 2:
        name_pattern = lambda count: f"img_{count:02d}"
    elif rename_option == 3:
        name_pattern = lambda count: f"image{count:04d}"

    # Determine the range for renaming based on order
    if order_option == "ascending":
        count_range = range(start_number, start_number + len(images))
    else:  # descending
        count_range = range(start_number, start_number - len(images), -1)

    # Rename files
    for count, filename in zip(count_range, images):
        old_path = os.path.join(folder_path, filename)
        new_name = f"{name_pattern(count)}{os.path.splitext(filename)[1].lower()}"
        new_path = os.path.join(folder_path, new_name)

        try:
            os.rename(old_path, new_path)
            print(f"Renamed: {filename} -> {new_name}")  # Log in PowerShell/console
        except Exception as e:
            print(f"Failed to rename {filename}: {e}")  # Log errors in PowerShell/console

    # Display success message
    create_colored_dialog(
        "Success",
        "All files have been renamed successfully!",
        "OK",
        "green"
    )

    # Open the Desktop folder on the C drive dynamically
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    subprocess.Popen(f'explorer "{desktop_path}"')

if __name__ == "__main__":
    rename_files()
