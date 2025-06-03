# Batch Image Compression Tool

A Python-based batch image compression tool that allows you to specify target file size and resolution limits.

## Features

- ✅ Batch compress all images in a specified directory
- ✅ Support for multiple image formats (JPG/JPEG/PNG/BMP/TIFF/WEBP)
- ✅ Set maximum file size (in MB)
- ✅ Optional maximum width/height limits
- ✅ Intelligent quality adjustment algorithm to maintain optimal visual 效果
- ✅ Non-destructive compression (original files remain unchanged)

## Installation Guide

### Prerequisites

- Python 3.6 or higher
- pip package management tool

### Installation Steps

1. Clone or download the project code
2. Install dependencies:

bash pip install -r requirements.txt 

## Usage Instructions

### Basic Usage

bash python compress_images.py <input directory> <maximum size (MB)> 

Example: Compress all images in the photos directory to under 2MB

bash python compress_images.py ./photos 2 

### Advanced Usage

bash python compress_images.py <input directory> <maximum size (MB)> [maximum width] [maximum height] 

Example 1: Compress images to under 1MB and limit maximum width to 1920 pixels

bash python compress_images.py ./photos 1 1920 

Example 2: Compress images to under 0.5MB and limit maximum resolution to 1920x1080

bash python compress_images.py ./photos 0.5 1920 1080 

## Compiling to Executable

### Method 1: Using PyInstaller (Recommended)

1. Install the compilation tool:
bash pip install pyinstaller 

2. Execute the compilation (generate a single exe file):
bash pyinstaller --onefile --icon=app.ico compress_images.py 
Note: app.ico is an optional application icon file

3. After compilation:
- Windows system: compress_images.exe is generated in the dist/ directory
- Linux system: An executable file is generated in the dist/ directory

### Method 2: Using auto-py-to-exe (Graphical Interface)

1. Install the tool:
bash pip install auto-py-to-exe 

2. Start the graphical interface:
bash auto-py-to-exe 
In the interface, select:
- Python file: compress_images.py
- Check "One File" mode
- You can add an ICO icon file
- Click "CONVERT .PY TO .EXE"

### Compilation Notes

1. Icon File Requirements:
- Must be in .ico format
- Recommended to include multiple sizes such as 16x16/32x32/48x48/256x256
- Online tools can be used to convert PNG to ICO

2. Cross-Platform Compilation:
- Compile the Windows version on a Windows system
- Compile the Linux version on a Linux system
- Use the py2app tool on Mac systems

## Output Explanation

The program will create a compressed subdirectory in the input directory, and all compressed images will be saved in this directory.

During processing, it will display:
- The file currently being processed
- The original file size
- The compressed file size

## Precautions

1. The program will not modify the original image files
2. Images that are already smaller than the target size will be skipped
3. It is recommended to set resolution limits for large images to achieve better compression 效果
4. The compression quality is automatically adjusted between 85-10 to meet size limits

## Frequently Asked Questions

Q: What image formats does the program support?
A: It supports JPG, JPEG, PNG, BMP, TIFF, and WEBP formats

Q: Will the resolution of compressed images be reduced?
A: The resolution will only be adjusted if maximum width/height parameters are specified; otherwise, only the compression quality is adjusted

Q: Why is the compiled exe file so large?
A: This is a normal phenomenon when PyInstaller packages the Python interpreter. You can use UPX compression to reduce the size:
bash pyinstaller --onefile --upx-dir=path/to/upx compress_images.py 

## License

This project uses the MIT license
