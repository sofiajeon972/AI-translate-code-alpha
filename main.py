from deep_translator import GoogleTranslator
import tkinter as tk
from tkinter import ttk, messagebox


def translate():
    # Get input text & strip whitespace
    src_text = input_text.get("1.0", tk.END).strip()

    if not src_text:
        messagebox.showerror("Input Error", "Please enter text to translate.")
        return

    # Get source and target languages
    src_lang = src_lang_combo.get()
    dest_lang = dest_lang_combo.get()

    try:
        # Translate text
        translated_text = GoogleTranslator(source=src_lang, target=dest_lang).translate(src_text)
        
        # Display translation
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, translated_text)
    except Exception as e:
        messagebox.showerror("Translation Error", str(e))


def clear_text():
    input_text.delete("1.0", tk.END)
    output_text.delete("1.0", tk.END)


# GUI Setup
root = tk.Tk()
root.title("AI-Powered Language Translator")
root.geometry("600x500")
root.configure(bg="#f0f0f0")

languages = GoogleTranslator().get_supported_languages()

# Title
tk.Label(root, text="Language Translator", font=("Arial", 20, "bold"), bg="#f0f0f0").pack(pady=10)

# Input Text
input_frame = tk.LabelFrame(root, text="Enter Text", font=("Arial", 12), padx=10, pady=10)
input_frame.pack(padx=10, pady=10, fill="both")

input_text = tk.Text(input_frame, height=5, wrap="word")
input_text.pack(fill="both")

# Language Selection
options_frame = tk.Frame(root, bg="#f0f0f0")
options_frame.pack(pady=10)

src_lang_label = tk.Label(options_frame, text="From:", font=("Arial", 12), bg="#f0f0f0")
src_lang_label.grid(row=0, column=0, padx=10)

src_lang_combo = ttk.Combobox(options_frame, values=languages, state="readonly")
src_lang_combo.set("auto")
src_lang_combo.grid(row=0, column=1, padx=10)


dest_lang_label = tk.Label(options_frame, text="To:", font=("Arial", 12), bg="#f0f0f0")
dest_lang_label.grid(row=0, column=2, padx=10)


dest_lang_combo = ttk.Combobox(options_frame, values=languages, state="readonly")
dest_lang_combo.set("english")
dest_lang_combo.grid(row=0, column=3, padx=10)


# Buttons
btn_frame = tk.Frame(root, bg="#f0f0f0")
btn_frame.pack(pady=10)

translate_btn = tk.Button(btn_frame, text="Translate", command=translate, font=("Arial", 12), bg="#4CAF50", fg="white")
translate_btn.grid(row=0, column=0, padx=10)

clear_btn = tk.Button(btn_frame, text="Clear", command=clear_text, font=("Arial", 12), bg="#FF5733", fg="white")
clear_btn.grid(row=0, column=1, padx=10)

# Output Text
output_frame = tk.LabelFrame(root, text="Translated Text", font=("Arial", 12), padx=10, pady=10)
output_frame.pack(padx=10, pady=10, fill="both")

output_text = tk.Text(output_frame, height=5, wrap="word")
output_text.pack(fill="both")


# Run GUI
root.mainloop()

