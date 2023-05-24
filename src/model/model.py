


class Model:
    @staticmethod
    #ToDo fix the damn circular import error!
    
    def handle_text_to_midi_conversion(text, file_name, save_folder):
        import os
        # Convert text to MIDI using the converter function
        file_number = 1
        while os.path.exists(os.path.join(save_folder, f"{file_name}{file_number}.mid")):
            file_number += 1
        # Generate the output file name with the unique number
        output_filename = f"{file_name}{file_number}.mid"
        output_path = os.path.join(save_folder, output_filename)
        from text_to_midi_converter import convert_text_to_midi
        convert_text_to_midi.convert_text_to_midi(text, output_path)
        print("File saved:", output_path)
