# 🔄 Batch File Renamer

![Python](https://img.shields.io/badge/Python-3.6+-blue?logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

A simple and practical tool to batch rename files in any folder, with a preview feature to ensure safety before executing changes.

---

## ✨ Features

- ✅ Rename all files in a folder at once
- ✅ Add a custom prefix and sequential numbers
- ✅ Keep original file extensions
- ✅ **Preview** changes before applying them
- ✅ User **confirmation** required to avoid mistakes
- ✅ Filter files by extension (optional)

---

## 📋 Requirements

- Python 3.6 or higher

---

## 🚀 How to Run

1. Open the terminal in the script folder
2. Run the command:
   ```bash
   python rename_files.py


   1. Follow the prompts:
   · Enter the folder path (e.g., C:\Users\YourName\Desktop\Photos)
   · Enter the desired prefix (e.g., Trip_Turkey)
   · Enter file extension to filter (e.g., jpg) or press Enter for all files
2. A preview of the new names will be displayed
3. Type yes to confirm and apply the changes

---

🖼️ Example

Before Renaming

```
IMG_001.jpg
IMG_002.jpg
photo.png
```

After Renaming (using prefix "Trip")

```
Trip_1.jpg
Trip_2.jpg
Trip_3.png
```

---

🛡️ Why Is This Tool Safe?

Before changing any file name, the tool shows you a complete list of proposed changes and asks for explicit confirmation. Nothing is modified without your approval.

---

📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

👩‍💻 Author

Mariam Albaik

· GitHub
