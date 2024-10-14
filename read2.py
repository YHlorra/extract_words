import fitz
import re
import tkinter as tk
from tkinter import filedialog

def select_pdf_file():
    # 打开文件选择对话框，选择PDF文件
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if file_path:
        pdf_entry.delete(0, tk.END)  # 清空之前的输入
        pdf_entry.insert(0, file_path)  # 插入选择的文件路径

def convert_pdf_to_txt():
    # 从输入框获取PDF文件路径
    pdf_path = pdf_entry.get()
    if not pdf_path:
        messagebox.showerror("Error", "Please select a PDF file first!")
        return
        # 打开PDF文件
    pdf_document = fitz.open(pdf_path)
    # 创建一个字符串对象来存储文本
    extracted_text = ""
    # 循环遍历文档中的页面
    for page_num in range(len(pdf_document)):
        # 获取页面
        page = pdf_document.load_page(page_num)
        # 从页面中提取文本
        text = page.get_text()
        # 将提取的文本添加到字符串对象中
        extracted_text += text + "\n"  # 添加换行符以区分页面内容
        # 关闭PDF文件
    pdf_document.close()

    # def extract_words(TXT):
    # 定义匹配模式，单词需跟在数字序号之后
    pattern = r'^\d+\s+([a-z]+(?:\'[a-z]+)*)'
    # 用于存储提取的单词的空字符串
    extracted_words = ''
    # 打开文件并逐行读取
    lines = extracted_text.splitlines()  # 使用splitlines()按行分割文本
    for line in lines:
        stripped_line = line.strip()
        # 使用正则表达式搜索匹配项
        match = re.search(pattern, line)
        if match:
            # 如果找到匹配项，则提取单词部分（忽略数字编号）
            extracted_word = match.group(1)
            # 添加字符串中
            extracted_words += extracted_word + '\n'
    # 保存为txt
    save_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    with open(save_path, "w", encoding='utf-8') as file:
        file.write(extracted_words)


# 创建Tkinter窗口
root = tk.Tk()
root.title("PDF to TXT Converter")

# 创建并放置标签和输入框
pdf_label = tk.Label(root, text="Select PDF File:")
pdf_label.pack(pady=10)

pdf_entry = tk.Entry(root, width=50)
pdf_entry.pack(pady=5)

# 创建并放置选择PDF文件的按钮
select_button = tk.Button(root, text="Browse", command=select_pdf_file)
select_button.pack(pady=5)

# 创建并放置转换并保存TXT文件的按钮
convert_button = tk.Button(root, text="Convert to TXT", command=convert_pdf_to_txt)
convert_button.pack(pady=20)

# 运行Tkinter主循环
root.mainloop()