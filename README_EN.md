# Watermark Adding Program
This program uses the tkinter library to create a simple GUI interface for adding watermarks to images.
[中文请点击这里](/README.md)

# Dependencies Installation
Before running the program, you need to install the following dependencies:
filetools

You can install the dependencies using the following command:

```shell
pip install filetools

```

# How to Use
After running the program, the program window will be displayed.

Choose the folder where the images to add watermarks are located by clicking the "Choose Folder" button. The selected folder path will be displayed in the "Image Path" input box.

Choose the folder where the watermarked images will be saved by clicking the "Choose Folder" button. The selected folder path will be displayed in the "Output Path" input box. If no output path is selected, a folder named "out" will be created in the current working directory by default.

Enter the text content for the watermark in the "Watermark Text" input box.

Choose the color for the watermark by clicking the "Choose Color" button. The code for the selected color will be displayed in the "Watermark Color" input box. The default color is "#00ffff".

Enter the size for the watermark in the "Watermark Size" input box. The default size is "20".

Enter the transparency for the watermark in the "Watermark Opacity" input box. The default opacity is "0.15".
Enter the rotation angle of the watermark and fill in the "Watermark Rotation Angle" input box. The default angle is "45".

Enter the spacing of the watermark and fill in the "Watermark Spacing" input box. The default spacing is "50".

Click the "Run" button, and the program will generate an image with a watermark in the specified output path.

You can click "Open Output Folder" to quickly open the output folder.

# Notes
1. The program depends on the filetools library, please make sure it is correctly installed.
2. The watermark text cannot be empty.

The above is the description of the watermarking program. If you have any questions or concerns, please contact the developer. Additionally, this program is very basic, so if you have any good ideas, please contact the developer.