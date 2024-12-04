# utils/file_operations.py

def save_file(file_path, content):
    """Save content to a file."""
    try:
        with open(file_path, "w") as file:
            file.write(content)
        print(f"File saved at {file_path}")
    except Exception as e:
        print(f"Error saving file: {e}")

def load_file(file_path):
    """Load content from a file."""
    try:
        with open(file_path, "r") as file:
            return file.read()
    except Exception as e:
        print(f"Error loading file: {e}")
        return ""
