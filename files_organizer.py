"""
Script to organize files into folders based on their file extensions.
"""

import os
import shutil

def organize_files_by_extension():
    # Get the target folder path from user input
    folder_path = input("Enter the path of the folder to organize: ").strip()
    
    # Validate the folder path exists
    if not os.path.exists(folder_path):
        print("Error: The specified folder does not exist.")
        return
    
    # Get all items in the folder
    try:
        items = os.listdir(folder_path)
    except PermissionError:
        print("Error: Permission denied when accessing the folder.")
        return
    
    for item in items:
        item_path = os.path.join(folder_path, item)
        
        # Skip if it's a directory
        if os.path.isdir(item_path):
            continue
            
        # Split filename and extension
        try:
            filename, extension = os.path.splitext(item)
            if not extension:  # Skip files without extensions
                continue
                
            # Remove the dot from extension and convert to lowercase
            extension = extension[1:].lower()
            
            # Skip system files like desktop.ini
            if extension in ['ini', 'lnk', 'tmp']:
                continue
                
            # Create target directory if it doesn't exist
            target_dir = os.path.join(folder_path, f"{extension}_files")
            if not os.path.exists(target_dir):
                os.makedirs(target_dir)
                
            # Check if file already exists in target directory
            target_path = os.path.join(target_dir, item)
            if not os.path.exists(target_path):
                shutil.move(item_path, target_dir)
                print(f"Moved: {item} -> {extension}_files/")
                
        except (shutil.Error, OSError) as e:
            print(f"Error processing {item}: {str(e)}")
            continue

if __name__ == "__main__":
    organize_files_by_extension()
    print("File organization complete!")
