# Mass File Rename

## Description
A simple Python script that copies files with specified extensions to a new folder, renaming them with randomly generated alphanumeric filenames.

## Features
- Copies files from the current directory
- Generates unique random filenames
- Supports multiple file extensions
- Preserves original file extensions
- Creates a dedicated 'renamedDocuments' folder for output

## Requirements
- Python 3.x
- No additional libraries required (uses standard Python libraries)

## Installation
1. Clone or download the script
2. Ensure you have Python 3 installed

## Usage
1. Place the script in the folder containing files you want to rename
2. Run the script:
   ```
   python rename_files.py
   ```
3. When prompted, you can:
   - Press Enter to use default extensions (.txt, .png, .jpg)
   - Enter custom extensions (e.g., `.pdf, .docx`)

## Example
```
Enter file extensions to rename (comma-separated, or press Enter for default .txt, .png, .jpg): 
Copied: photo1.jpg -> A7xK9mB2Tz.jpg
Copied: document.txt -> Q5nJ3fH8Lp.txt

Total files copied: 2
Files saved to: /path/to/current/directory/renamedPhotos
```

## Precautions
- Always backup your files before running
- Original files remain untouched
- Unique random filenames prevent overwriting

## License
MIT License

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss proposed changes.