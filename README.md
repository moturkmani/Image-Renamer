# Image Renamer

This Python script simplifies the process of renaming image files in a specified folder. It uses a graphical user interface (GUI) for a user-friendly experience, making it easy to select folders, set starting numbers, and rename files sequentially.

## Features

- **Interactive GUI**: Built with `tkinter`, it provides dialogs for folder selection, number input, and feedback.
- **Image Filtering**: Automatically identifies and processes image files based on common extensions (e.g., `.jpg`, `.png`, `.gif`).
- **Sequential Renaming**: Allows users to set a starting number for sequential file naming.
- **Error Handling**: Provides clear messages if no folder is selected or if no image files are found.
- **Automatic Folder Opening**: Opens the renamed files' folder upon completion (needs work).

## Requirements

- Python 3.x
- Required libraries: `tkinter`

## How to Use

1. Clone or download the repository:
   ```bash
   git clone https://github.com/moturkmani/rename-files.git
   cd image-renamer
   ```

2. Run the script in CMD or PowerShell:
   ```bash
   python rename_files.py
   ```

3. Follow the prompts:
   - Select the folder containing the images.
   - Enter the starting number for renaming.
   - Enter which image naming format you prefer.

4. View the renamed files in the folder, which opens automatically after completion (still not working how I want it to).

## Example Workflow

1. **Welcome Message**: A welcome dialog greets the user.
2. **Folder Selection**: The user selects a folder using a file dialog.
3. **Starting Number**: The user enters a starting number for the new filenames.
4. **Selecting Name Format**: User selects how to rename the images from 3 options. 
5. **Renaming**: The script renames all images sequentially in the format you chose (e.g., `image1.jpg`, `image2.png`).
6. **Completion**: A success message is displayed, and the folder opens (not quite the correct file location).

## Customization

- Modify `image_extensions` in the script to include additional file types.
- Adjust naming conventions in the `new_name` variable.

## Contributions

Contributions are welcome! Feel free to submit a pull request or open an issue for suggestions or improvements.


