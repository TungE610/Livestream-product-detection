import os
import shutil

def move_files(source_folder, dest_folder, extensions):
    # Create destination folders if they don't exist
    os.makedirs(dest_folder, exist_ok=True)

    # Get a list of all files in the source folder
    files = os.listdir(source_folder)

    for file_name in files:
        source_path = os.path.join(source_folder, file_name)

        # Check if the file has a valid extension
        if any(file_name.lower().endswith(ext) for ext in extensions):
            dest_path = os.path.join(dest_folder, file_name)

            # Move the file to the destination folder
            shutil.move(source_path, dest_path)

            print(f'Moved: {file_name} from {source_folder} to {dest_folder}')

if __name__ == "__main__":
    # List of folders to process
    folders_to_process = ['clear_man', 'comfort', 'king_gold', 'kitkitplus', 'kopiko_macchiato', 'likenest', 'ponnie', 'olap', 'thale', 'wantwant']

    # Specify the source and destination folders for images and labels
    images_source_folder = '/path/to/source/images'
    labels_source_folder = '/path/to/source/labels'
    images_dest_folder = '/path/to/destination/images'
    labels_dest_folder = '/path/to/destination/labels'

    # Specify the file extensions to move
    image_extensions = ['.png', '.jpg']
    label_extensions = ['.txt']

    # Move image files
    for folder in folders_to_process:
        move_files(os.path.join(images_source_folder, folder), images_dest_folder, image_extensions)

    # Move label files
    for folder in folders_to_process:
        move_files(os.path.join(labels_source_folder, folder), labels_dest_folder, label_extensions)
