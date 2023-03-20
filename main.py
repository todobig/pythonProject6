import os
import zipfile
import shutil

# Define source and destination folders
source_folder = 'E:/heckless/1/raw'
destination_folder = 'E:/heckless/1/images'

# Loop through all files in the source folder
for file_name in os.listdir(source_folder):
    # Check if file is a ZIP file
    if file_name.endswith('.zip'):
        # Extract the ZIP file to a temporary folder
        temp_folder = os.path.join(source_folder, 'temp')
        with zipfile.ZipFile(os.path.join(source_folder, file_name), 'r') as zip_ref:
            zip_ref.extractall(temp_folder)

        # Loop through all files in the temporary folder
        for root, dirs, files in os.walk(temp_folder):
            for file in files:
                # Check if file is a PNG file
                if file.endswith('.png'):
                    # Move the PNG file to the destination folder
                    source_file = os.path.join(root, file)
                    shutil.move(source_file, destination_folder)

        # Remove the temporary folder
        shutil.rmtree(temp_folder)

        # Delete the source ZIP file
        os.remove(os.path.join(source_folder, file_name))