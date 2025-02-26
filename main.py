from deep_translator import GoogleTranslator
import tkinter as tk

def translate():
    # Get input text & strip whitespace
    src_text = input_text.get("1.0", tk.END).strip()

    if not src_text:
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, "Error: No text provided!")
        return

    # Get source and target language codes
    src_lang = src_lang_entry.get().strip() or "auto"
    dest_lang = dest_lang_entry.get().strip() or "en"

    try:
        # Translate text
        translated_text = GoogleTranslator(source=src_lang, target=dest_lang).translate(src_text)
        
        # Display translation
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, translated_text)
    except Exception as e:
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, f"Translation Error: {e}")

# GUI Setup
root = tk.Tk()
root.title("AI-Powered Language Translator")

# Input text box
tk.Label(root, text="Enter Text:").pack()
input_text = tk.Text(root, height=5, width=50)
input_text.pack()

# Source language input
tk.Label(root, text="Source Language (e.g., 'en')").pack()
src_lang_entry = tk.Entry(root)
src_lang_entry.pack()

# Destination language input
tk.Label(root, text="Target Language (e.g., 'es')").pack()
dest_lang_entry = tk.Entry(root)
dest_lang_entry.pack()

# Translate button
tk.Button(root, text="Translate", command=translate).pack()

# Output text box
tk.Label(root, text="Translated Text:").pack()
output_text = tk.Text(root, height=5, width=50)
output_text.pack()

# Run GUI
root.mainloop()
