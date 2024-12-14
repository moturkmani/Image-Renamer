# Image Renamer

## Overview
The **Image Renamer** is a Python-based GUI application designed to make renaming image files quick and easy. Built using `tkinter`, it provides a user-friendly interface for selecting renaming conventions, ordering, and numbering images within a specified folder.

---

## Features
- **User-friendly dialogs**: Provides intuitive prompts for selecting options.
- **Customizable renaming patterns**: Choose from multiple renaming conventions:
  - `image1, image2, image3`
  - `img_01, img_02, img_03`
  - `image0001, image0002, image0003`
- **Ascending or descending order**: Rename images in either ascending or descending sequence.
- **Starting number selection**: Specify the starting number for renaming.
- **Folder selection dialog**: Easily choose the folder containing images to rename.
- **Error handling**: Handles invalid inputs and missing files gracefully.
- **Supports multiple image formats**: `.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp`, `.tiff`, `.webp`.

---

## Prerequisites
- Python 3.x
- `tkinter` module (comes pre-installed with Python on most systems).
## EXE File
- If you don't have python installed, you can run the .exe file.
---

## Usage
1. Run the script:
   ```bash
   python image_renamer.py
   ```
2. Follow the prompts:
   - **Welcome Message**: Start the renaming process.
   - **Order Selection**: Choose ascending or descending order.
   - **Folder Selection**: Select the folder containing your images.
   - **Starting Number**: Enter the starting number for renaming.
   - **Renaming Convention**: Choose one of the provided patterns.
3. The program will rename all images in the selected folder based on your inputs.
4. After successful renaming, your desktop folder will open to confirm completion.

---

## Example
If you select:
- Order: `Ascending`
- Starting number: `1`
- Renaming convention: `img_01, img_02, img_03`

And your folder contains:
- `photo.jpg`
- `image.png`
- `pic.gif`

The renamed files will be:
- `img_01.jpg`
- `img_02.png`
- `img_03.gif`

---

## Supported Image Formats
- `.jpg`
- `.jpeg`
- `.png`
- `.gif`
- `.bmp`
- `.tiff`
- `.webp`

---

## Acknowledgments
- Inspired by the need for an efficient tool to rename large batches of images for imgur uploads.
- Developed with Python and `tkinter`.

## Future Improvements
- I would like to eventually make this where user will type a naming convention example separated by commas and the script will analyze and copy the naming convention.
- Make all the buttons colorful and ensure cursor is always active in the input textbox area.

