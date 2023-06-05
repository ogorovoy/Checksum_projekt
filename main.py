import os
import shutil
import hashlib

my_dir= "C:XXXX"

def mask_funkction(my_dir):
    for file in os.listdir(my_dir):
        if os.path.isfile(os.path.join(my_dir, file)):

            create_new_folder = os.path.splitext(file)[0]
            os.makedirs(os.path.join(my_dir, create_new_folder), exist_ok=True)

            old_path = os.path.join(my_dir, file)
            new_path = os.path.join(my_dir, create_new_folder, file)
            shutil.copy2(old_path, new_path)

            txt_file_name = os.path.splitext(file)[0] + ".txt"
            txt_file_path = os.path.join(my_dir, create_new_folder, txt_file_name)
            with open(old_path, 'rb') as file:
                file_content = file.read()
                control_summe = hashlib.md5(file_content).hexdigest()

            with open(txt_file_path, 'w') as txt_file:
                txt_file.write(f"control_summe: {control_summe}")

mask_funkction(my_dir)
