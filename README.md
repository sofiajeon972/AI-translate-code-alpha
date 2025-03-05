# Language Translation Tool

## 📘 Project Overview
This is a simple yet powerful **AI-powered language translation tool** built using Python and the **Deep Translator** library. The tool provides an intuitive GUI with **Tkinter**, allowing users to translate text between multiple languages using the **Google Translator API**.

## 🚀 Features
- **Multi-language support:** Translate text between various languages.
- **Automatic language detection:** Leave the source language field empty to auto-detect.
- **User-friendly interface:** Minimal and clean GUI for smooth usage.
- **Error handling:** Graceful error messages for invalid inputs or API issues.

## 🛠️ Tech Stack
- **Python** (Core logic)
- **Tkinter** (GUI development)
- **Deep Translator** (GoogleTranslator API)

## 📂 Project Structure
```
├── translator.py     # Main script with GUI and translation logic
├── README.md         # Project documentation (this file)
└── requirements.txt  # List of required libraries
```

## ⚙️ Installation
1. **Clone the repository:**
```sh
git clone https://github.com/sofiajeon972/language-translator.git
cd language-translator
```

2. **Create a virtual environment (optional but recommended):**
```sh
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

3. **Install dependencies:**
```sh
pip install -r requirements.txt
```

## ▶️ Usage
1. **Run the script:**
```sh
python translator.py
```

2. **Enter text:** Type the text you want to translate.
3. **Set languages:** Specify the source and target language codes (e.g., `en` for English, `es` for Spanish). Leave the source language blank for auto-detection.
4. **Translate:** Click the **Translate** button to see the result.

## 🛡️ Error Handling
- **No input text:** Displays an error message.
- **Invalid language codes:** Shows a translation error.
- **API issues:** Catches exceptions and informs the user.

## 🧠 How It Works
1. The user inputs text and language codes.
2. The tool uses **GoogleTranslator** to process the request.
3. The translated text is displayed in the GUI.

## 🖼️ Visual Flow
Refer to the flowchart for a high-level view of the translation process.

## 🤝 Contributing
Feel free to fork the repository, create a branch, and submit a pull request with your improvements.

## 📄 License
This project is licensed under the MIT License.

---



