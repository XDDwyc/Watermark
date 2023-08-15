import os
import tkinter as tk
import subprocess
from tkinter import filedialog
from tkinter import colorchooser
from watermarker.marker import add_mark

# 创建添加水印的窗口
window = tk.Tk()
window.title("添加水印")

# 创建标签和选择文件夹按钮
tk.Label(window, text="图片路径: ").grid(row=0, column=0)


def choose_file():
    filepath = filedialog.askdirectory()  # 修改为选择文件夹的对话框
    filepath_entry.delete(0, tk.END)
    filepath_entry.insert(0, filepath)


filepath_entry = tk.Entry(window)
filepath_entry.grid(row=0, column=1)
tk.Button(window, text="选择文件夹", command=choose_file).grid(row=0, column=2)

tk.Label(window, text="输出路径: ").grid(row=1, column=0)


def choose_folder():
    outpath = filedialog.askdirectory()
    if outpath:
        outpath_entry.delete(0, tk.END)
        outpath_entry.insert(0, outpath)
    else:
        default_outpath = os.path.join(os.getcwd(), "out")
        os.makedirs(default_outpath, exist_ok=True)
        outpath_entry.delete(0, tk.END)
        outpath_entry.insert(0, default_outpath)


default_outpath = os.path.join(os.getcwd(), "out")
outpath_entry = tk.Entry(window)
outpath_entry.insert(0, default_outpath)
outpath_entry.grid(row=1, column=1)
tk.Button(window, text="选择文件夹", command=choose_folder).grid(row=1, column=2)

tk.Label(window, text="水印文本: ").grid(row=2, column=0)
markstr_entry = tk.Entry(window)
markstr_entry.grid(row=2, column=1)

tk.Label(window, text="水印颜色: ").grid(row=3, column=0)
colorcode = "#00ffff"  # 默认颜色值


def choose_color():
    color = colorchooser.askcolor(color=colorcode)[1]
    if color:
        colorcode_entry.delete(0, tk.END)
        colorcode_entry.insert(0, color)


colorcode_entry = tk.Entry(window)
colorcode_entry.insert(0, colorcode)  # 设置默认颜色值
colorcode_entry.grid(row=3, column=1)
tk.Button(window, text="选择颜色", command=choose_color).grid(row=3, column=2)

tk.Label(window, text="水印大小: ").grid(row=4, column=0)
wordsize_entry = tk.Entry(window)
wordsize_entry.insert(0, "20")  # 设置默认大小值
wordsize_entry.grid(row=4, column=1)

tk.Label(window, text="水印透明度: ").grid(row=5, column=0)
wordopacity_entry = tk.Entry(window)
wordopacity_entry.insert(0, "0.15")  # 设置默认透明度值
wordopacity_entry.grid(row=5, column=1)

tk.Label(window, text="水印旋转角度: ").grid(row=6, column=0)
wordangle_entry = tk.Entry(window)
wordangle_entry.insert(0, "45")  # 设置默认旋转角度值
wordangle_entry.grid(row=6, column=1)

tk.Label(window, text="水印间距: ").grid(row=7, column=0)
wordspace_entry = tk.Entry(window)
wordspace_entry.insert(0, "50")  # 设置默认间距值
wordspace_entry.grid(row=7, column=1)

# 创建结果显示文本框
result_text = tk.Text(window, height=10, width=50)
result_text.grid(row=8, column=0, columnspan=3)


#打开输出文件夹
def open_output_folder():
    outpath = outpath_entry.get()
    subprocess.Popen(f'explorer "{outpath}"')

# 定义点击运行按钮时的操作
def run_program():
    filepath = filepath_entry.get()
    outpath = outpath_entry.get()
    markstr = markstr_entry.get()
    colorcode = colorcode_entry.get()
    wordsize = int(wordsize_entry.get())
    wordopacity = float(wordopacity_entry.get())
    wordangle = int(wordangle_entry.get())
    wordspace = int(wordspace_entry.get())

    if markstr.strip() == "":
        result_text.insert(tk.END, "请填入水印文本\n")
        return

    try:
        add_mark(
            file=filepath,
            out=outpath,
            mark=markstr,
            color=colorcode,
            size=wordsize,
            opacity=wordopacity,
            angle=wordangle,
            space=wordspace,
        )
        result_text.insert(tk.END, "具体信息请看控制台\n")
        open_folder_btn = tk.Button(window, text="打开输出文件夹", command=open_output_folder)
        open_folder_btn.grid(row=9, column=2)
    except Exception as e:
        result_text.insert(tk.END, f"出现错误：{str(e)}")


# 创建运行按钮
tk.Button(window, text="运行", command=run_program).grid(row=9, column=1)

# 运行窗口
window.mainloop()
