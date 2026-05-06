import os

def rename_files(folder_path, prefix):
    if not os.path.isdir(folder_path):
        print("Error: Folder not found!")
        return
    
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    
    for i, filename in enumerate(files, start=1):
        ext = os.path.splitext(filename)[1]
        new_name = f"{prefix}_{i}{ext}"
        
        old = os.path.join(folder_path, filename)
        new = os.path.join(folder_path, new_name)
        
        os.rename(old, new)
        print(f"Renamed: {filename}  -->  {new_name}")

    print("\nDone! All files renamed.")

if __name__ == "__main__":
    folder = input("Enter folder path: ")
    prefix = input("Enter prefix: ")
    rename_files(folder, prefix)
