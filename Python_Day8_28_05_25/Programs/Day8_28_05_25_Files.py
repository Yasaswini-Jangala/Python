# import shutil
# source_abs = 'C:\\Users\\admin\\Desktop\\ALL FILES\\CapgeminiTraining\\Python\\Python_Day8_28_05_25\\Programs\\country.csv'
# dest_abs = 'C:\\Users\\admin\\Desktop\\ALL FILES\\CapgeminiTraining\\Python\\Python_Day8_28_05_25\\copied_country_absolute.csv'
# shutil.copy(source_abs, dest_abs)

# import shutil
# source_rel = 'country.csv'
# dest_rel = '..\\copied_country_relative.csv'
# shutil.copy(source_rel, dest_rel)

# import shutil
# source_dir = 'C:\\Users\\admin\\Desktop\\ALL FILES\\CapgeminiTraining\\Python\\Python_Day8_28_05_25\\Programs'
# destination_dir = 'C:\\Users\\admin\\Desktop\\ALL FILES\\CapgeminiTraining\\Python\\Python_Day8_28_05_25\\CopyTree_Copied_Programs'
# shutil.copytree(source_dir, destination_dir, dirs_exist_ok=True)
# print(f"Folder copied successfully to: {destination_dir}")

# import os
# file_path = 'C:\\Users\\admin\\Desktop\\ALL FILES\\CapgeminiTraining\\Python\\Python_Day8_28_05_25\\Programs\\country.csv'
# file_size_bytes = os.path.getsize(file_path)
# print(f"File size: {file_size_bytes} bytes")
# print(f"File size: {file_size_bytes / 1024:.2f} KB")