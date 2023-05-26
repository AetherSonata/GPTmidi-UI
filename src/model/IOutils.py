import os


def create_unique_filename(save_folder, file_name):
        
    file_number = 1
    while os.path.exists(os.path.join(save_folder, f"{file_name}{file_number}.mid")):
        file_number += 1
    output_filename = f"{file_name}{file_number}.mid"
    output_path = os.path.join(save_folder, output_filename)
        
    return output_path

