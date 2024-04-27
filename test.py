import zipfile
import os
import shutil


shutil.rmtree("./del")







# def create_vsix_archive(source_dir, output_file):
#     # Create a ZIP archive
#     with zipfile.ZipFile(output_file, 'w', zipfile.ZIP_DEFLATED) as vsix_zip:
#         # Walk through the source directory and add its contents to the archive
#         for root, dirs, files in os.walk(source_dir):
#             for file in files:
#                 file_path = os.path.join(root, file)
#                 archive_path = os.path.relpath(file_path, source_dir)
#                 vsix_zip.write(file_path, archive_path)

# # Example usage
# source_directory = '/new'
# vsix_output_file = '/'

# create_vsix_archive(source_directory, vsix_output_file)
