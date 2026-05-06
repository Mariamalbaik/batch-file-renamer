import os

def rename_files(folder_path, prefix):
    # 1. التحقق من وجود المجلد
    if not os.path.isdir(folder_path):
        print("Error: Folder not found!")
        return

    # 2. جلب قائمة الملفات (باستثناء المجلدات الفرعية)
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

    if not files:
        print("The folder is empty. No files to rename.")
        return

    # 3. تجهيز الأسماء الجديدة في قائمة للمعاينة
    new_names = []
    for i, filename in enumerate(files, start=1):
        ext = os.path.splitext(filename)[1]
        new_name = f"{prefix}_{i}{ext}"
        new_names.append((filename, new_name))

    # 4. عرض المعاينة (Preview)
    print("\n" + "=" * 50)
    print("PREVIEW - Files will be renamed as follows:")
    print("=" * 50)
    for old, new in new_names:
        print(f"  '{old}'  -->  '{new}'")
    print("=" * 50)

    # 5. طلب التأكيد من المستخدم (Confirmation)
    confirm = input("\nDo you want to proceed with renaming? (yes/no): ").strip().lower()

    if confirm != 'yes':
        print("\nOperation cancelled. No files were renamed.")
        return

    # 6. إجراء إعادة التسمية الفعلية بعد التأكيد
    print("\nRenaming files...")
    for old, new in new_names:
        old_path = os.path.join(folder_path, old)
        new_path = os.path.join(folder_path, new)
        os.rename(old_path, new_path)
        print(f"  Renamed: '{old}'  -->  '{new}'")

    print("\nDone! All files renamed successfully.")

if __name__ == "__main__":
    folder = input("Enter folder path: ")
    prefix = input("Enter prefix: ")
    rename_files(folder, prefix)
