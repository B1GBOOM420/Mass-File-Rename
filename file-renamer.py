import os
import random
import string
import shutil


def rename_files_in_folder(folder_path=None, extensions=[".txt", ".png", ".jpg"]):
    """
    Copy files from specified folder to a 'renamedDocuments' folder with random filenames.

    :param folder_path: Path to the folder containing files to rename (defaults to current directory)
    :param extensions: List of file extensions to rename (default: .txt, .png, .jpg)
    """
    # Use current directory if no path specified
    if folder_path is None:
        folder_path = os.getcwd()

    # Create 'renamedDocuments' folder if it doesn't exist
    renamed_folder = os.path.join(folder_path, "renamedDocuments")
    os.makedirs(renamed_folder, exist_ok=True)

    # Validate input folder path
    if not os.path.isdir(folder_path):
        print(f"Error: {folder_path} is not a valid directory.")
        return

    # Function to generate random filename
    def generate_random_filename(length=10):
        """
        Generate a random filename of specified length using alphanumeric characters.

        :param length: Length of the random filename (default: 10)
        :return: Randomly generated filename
        """
        characters = string.ascii_letters + string.digits
        return "".join(random.choice(characters) for _ in range(length))

    # Counter for copied files
    copied_files = 0

    # Loop through all files in the directory
    for filename in os.listdir(folder_path):
        # Check if file has one of the specified extensions
        if any(filename.lower().endswith(ext.lower()) for ext in extensions):
            # Get full file paths
            old_path = os.path.join(folder_path, filename)

            # Skip if it's a directory
            if os.path.isdir(old_path):
                continue

            # Generate new filename with original extension
            file_extension = os.path.splitext(filename)[1]

            # Ensure unique filename
            while True:
                new_filename = generate_random_filename() + file_extension
                new_path = os.path.join(renamed_folder, new_filename)

                # Check if filename already exists
                if not os.path.exists(new_path):
                    break

            # Copy the file to the new folder
            try:
                shutil.copy2(old_path, new_path)
                print(f"Copied: {filename} -> {new_filename}")
                copied_files += 1
            except Exception as e:
                print(f"Error copying {filename}: {e}")

    # Print summary
    print(f"\nTotal files copied: {copied_files}")
    print(f"Files saved to: {renamed_folder}")


# Default script execution
if __name__ == "__main__":
    # Optional: Specify custom extensions
    custom_extensions = input(
        "Enter file extensions to rename (comma-separated, or press Enter for default .txt, .png, .jpg): "
    )

    # Process custom extensions
    if custom_extensions.strip():
        extensions = [ext.strip() for ext in custom_extensions.split(",")]
        rename_files_in_folder(extensions=extensions)
    else:
        rename_files_in_folder()
