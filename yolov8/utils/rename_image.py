import os
import re

def rename_image(directory, extension, range_start, range_end, start_number):
    # Path to the directory containing your images
    directory_path = directory

    # Desired file extension
    file_extension = extension

    # Starting number for renaming
    start_number = start_number

    # Iterate through the range of numbers (49 to 132)
    for i in range(range_start, range_end):
        # Old file name (original name)
        old_name = f'{i}{file_extension}'
        
        # New file name
        new_name = f'{start_number}{file_extension}'
        
        # Full paths
        old_path = os.path.join(directory_path, old_name)
        new_path = os.path.join(directory_path, new_name)
        
        try:
            # Rename the file
            os.rename(old_path, new_path)
            print(f'Renamed: {old_path} to {new_path}')
        except FileNotFoundError:
            print(f'File not found: {old_path}')
        except FileExistsError:
            print(f'File already exists: {new_path}')
        except Exception as e:
            print(f'Error renaming file: {e}')
        
        # Increment the start number for the next iteration
        start_number += 1

    print('Rename process completed.')
def change_extension(directory, old_extension, new_extension):

    # Path to the directory containing your images
    directory_path = directory

    # Desired new file extension
    new_file_extension = new_extension

    # Iterate through the files in the directory
    for filename in os.listdir(directory_path):
        # Check if the file has the old extension (.jpg)
        if filename.endswith(old_extension):
            # Build the full paths
            old_path = os.path.join(directory_path, filename)
            new_path = os.path.join(directory_path, os.path.splitext(filename)[0] + new_file_extension)

            try:
                # Rename the file with the new extension
                os.rename(old_path, new_path)
                print(f'Renamed: {old_path} to {new_path}')
            except FileNotFoundError:
                print(f'File not found: {old_path}')
            except FileExistsError:
                print(f'File already exists: {new_path}')
            except Exception as e:
                print(f'Error renaming file: {e}')

    print('Rename process completed.')

def remove_all_label(directory):
    directory_path = directory

    # Desired file extension to remove
    file_extension_to_remove = '.txt'

    # Iterate through the files in the directory
    for filename in os.listdir(directory_path):
        # Check if the file has the specified extension (.txt)
        if filename.endswith(file_extension_to_remove):
            # Build the full path
            file_path = os.path.join(directory_path, filename)

            try:
                # Remove the file
                os.remove(file_path)
                print(f'Removed: {file_path}')
            except FileNotFoundError:
                print(f'File not found: {file_path}')
            except Exception as e:
                print(f'Error removing file: {e}')

    print('File removal process completed.')

def rename_all_file_with_first_letter_not_equal(directory, letter, start_index):
    for filename in os.listdir(directory):
        # Check if the file does not start with the specified letter
        if not filename.lower().startswith(letter.lower()):
            # Build the full paths
            old_path = os.path.join(directory, filename)
            
            # Create a new file name based on the start_index
            new_name = f'4{start_index}.png'
            new_path = os.path.join(directory, new_name)
            
            try:
                # Rename the file
                os.rename(old_path, new_path)
                print(f'Renamed: {old_path} to {new_path}')
                start_index += 1
            except FileNotFoundError:
                print(f'File not found: {old_path}')
            except FileExistsError:
                print(f'File already exists: {new_path}')
            except Exception as e:
                print(f'Error renaming file: {e}')

    print('Rename process completed.')
def replace_a_in_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    with open(file_path, 'w') as file:
        for line in lines:
            # Replace '1' with '5' in the line
            modified_line = line.replace('1 ', '5 ')
            file.write(modified_line)

def replace_a_in_all_files(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            file_path = os.path.join(directory, filename)
            replace_a_in_file(file_path)

def rename_files(directory_path):
    # Get a list of all files in the specified directory
    files = os.listdir(directory_path)

    for file_name in files:
        old_path = os.path.join(directory_path, file_name)

        # Check if the file starts with a number
        if file_name[0].isdigit():
            # Extract the numeric part from the old name
            numeric_part = file_name.rstrip('.png').rstrip('.txt')

            # Determine the number of zeros to add based on the length of the numeric part
            num_zeros = max(0, 4 - len(numeric_part))

            # Create the new name with added zeros and '4' as a prefix
            new_name = '4' + '0' * num_zeros + numeric_part

            # Add the original extension back to the new name
            if file_name.lower().endswith('.png'):
                new_name += '.png'
            elif file_name.lower().endswith('.txt'):
                new_name += '.txt'

            new_path = os.path.join(directory_path, new_name)

            # Rename the file
            os.rename(old_path, new_path)

            print(f'Renamed: {file_name} -> {new_name}')


def remove_non_png_files(directory_path):
    # Get a list of all files in the specified directory
    files = os.listdir(directory_path)

    for file_name in files:
        file_path = os.path.join(directory_path, file_name)

        # Check if the file does not have a .png extension
        if not file_name.lower().endswith('.png'):
            # Remove the file
            os.remove(file_path)
            print(f'Removed: {file_name}')

def remove_second_char(directory_path):
    # Get a list of all files in the specified directory
    files = os.listdir(directory_path)

    for file_name in files:
        old_path = os.path.join(directory_path, file_name)

        # Check if the file starts with a digit
        if file_name[0].isdigit():
            # Remove the second character from the file name
            new_name = file_name[0] + file_name[2:]

            new_path = os.path.join(directory_path, new_name)

            # Rename the file
            os.rename(old_path, new_path)

            print(f'Renamed: {file_name} -> {new_name}')

def main():
    # change_extension('../../datasets/train/images/kopiko_macchiato', '.jpeg', '.png')
    # rename_image('kinggold', '.png', 1, 103, 2001)
    remove_all_label('../../datasets/train/images/kopiko_macchiato')
    # rename_all_file_with_first_letter_not_equal('../../datasets/train/images/kopiko_macchiato', '4', 183)
    # replace_a_in_all_files('likenest')
    # remove_all_label('olap')
    # add_mid_zeros('../../datasets/train/images/kopiko_macchiato')
    # remove_second_char('../../datasets/train/images/kopiko_macchiato')

if __name__ == "__main__":
    main()
