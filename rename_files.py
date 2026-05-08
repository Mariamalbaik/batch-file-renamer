"""
Batch File Renamer
-------------------
A simple Python script to batch rename files in any folder by adding
a custom prefix and sequential numbers. Includes preview, confirmation,
and optional extension filtering for safety.
"""

import os

def get_filtered_files(folder_path, extension):
    """Retrieve files from a folder, optionally filtered by a specific extension."""
    all_files = os.listdir(folder_path)
    if not extension:
        return all_files
    return [f for f in all_files if f.lower().endswith(f".{extension.lower()}")]

def preview_rename(folder_path, prefix, extension):
    """Generate a preview list of old and new file names."""
    files = get_filtered_files(folder_path, extension)
    preview_list = []
    for i, filename in enumerate(files, start=1):
        ext = os.path.splitext(filename)[1]
        new_name = f"{prefix}_{i}{ext}"
        preview_list.append((filename, new_name))
    return preview_list

def confirm_rename():
    """Ask the user for confirmation before applying changes."""
    answer = input("\n⚠️  Are you sure you want to proceed? (yes/no): ").strip().lower()
    return answer == "yes"

def execute_rename(folder_path, preview_list):
    """Execute the actual renaming process."""
    for old_name, new_name in preview_list:
        old_path = os.path.join(folder_path, old_name)
        new_path = os.path.join(folder_path, new_name)
        os.rename(old_path, new_path)
    print("✅ All files renamed successfully!")

def main():
    """Main function to coordinate the script workflow."""
    print("=" * 40)
    print("🔄 Batch File Renamer")
    print("=" * 40)
    
    folder_path = input("📁 Enter folder path: ").strip()
    prefix = input("🏷️  Enter desired prefix: ").strip()
    extension = input("🔍 Filter by extension (e.g., jpg) | Enter for all: ").strip()
    
    if not os.path.exists(folder_path):
        print("❌ Folder path does not exist. Please check and try again.")
        return
    
    preview = preview_rename(folder_path, prefix, extension)
    
    if not preview:
        print("📭 No matching files found.")
        return
    
    print("\n👀 Preview of changes:")
    print("-" * 30)
    for old, new in preview:
        print(f"  {old}  ➜  {new}")
    print("-" * 30)
    
    if confirm_rename():
        execute_rename(folder_path, preview)
    else:
        print("❌ Operation cancelled. No files were changed.")

if __name__ == "__main__":
    main()
