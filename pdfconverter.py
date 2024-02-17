import tkinter as tk
import os
from pdf2word import convert_pdf_to_word
from docx2pdf import convert_word_to_pdf

def convert_pdf_to_word_gui():
    input_file = entry.get()
    output_file = os.path.splitext(input_file)[0] + ".docx"
    convert_pdf_to_word(input_file, output_file)
    entry.delete(0, tk.END)
    entry.insert(0, output_file)

def convert_word_to_pdf_gui():
    input_file = entry.get()
    output_file = os.path.splitext(input_file)[0] + ".pdf"
    convert_word_to_pdf(input_file, output_file)
    entry.delete(0, tk.END)
    entry.insert(0, output_file)

window = tk.Tk()
window.title("PDF to Word Converter")
window.geometry("400x100")

entry = tk.Entry(window)
entry.pack(pady=10)

pdf_to_word_button = tk.Button(window, text="Convert PDF to Word", command=convert_pdf_to_word_gui)
pdf_to_word_button.pack(pady=5)

word_to_pdf_button = tk.Button(window, text="Convert Word to PDF", command=convert_word_to_pdf_gui)
word_to_pdf_button.pack(pady=5)

window.mainloop()