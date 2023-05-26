import json

class Preferences:
    def __init__(self):
        self.default_preferences = {
            "save_folder": ".\output",
            "file_name": "output",
            "API_KEY": "insert your OpenAI API-KEY here",
            "instruction_text": "We will now create a .mid file text. In the following prompt I will describe my idea of a musical piece and you will give me back a .mid file in the style of:0 Tempo 500000\n 0 TimeSig 4/4 24 8\n 0 NoteOn ch=1 n=60 v=64\n 240 NoteOff ch=1 n=60 v=64\n The prompt starts now:",
            "deep_instruction": "Please ensure that the generated MIDI file has precise and consistent timings on 1/16th, 1/8th, 1/4th, 1/2th, and 1/1 note durations. Pay careful attention to the rhythmic grid and align all notes and events to these specified durations. Avoid irregular or fluctuating timings and strive for a steady and accurate rhythmic feel throughout the MIDI file. If necessary, you can quantize the generated MIDI file to fix any timing inconsistencies. Maintain the musicality and expression while adhering to the requested timing precision.",
            "temperature": 0.7
        }



    def write_default_preferences():
        import os


        # Define the file path
        file_path = "preferences.txt"

        # Check if the preferences file already exists
        if not os.path.exists(file_path):
            # Create the file and store the default preferences
            with open(file_path, "w") as file:
                json.dump(Preferences().default_preferences, file)

            print("Default preferences restored.")
        else:
            print("")



    def write_new_preferences(new_preferences):

        # Define the file path
        file_path = "preferences.txt"

        try:
            # Open the file and store the new preferences
            with open(file_path, "w") as file:
                json.dump(new_preferences, file)
            
            print("Preferences saved.")
        except IOError as e:
            print(f"Error occurred while saving preferences: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")



    def load_preferences():
        preferences = {}
        file_path = "preferences.txt"

        try:
            with open(file_path, "r") as file:
                preferences = json.load(file)
            print("Preferences loaded.")
        except IOError as e:
            print(f"Error occurred while loading preferences: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")

        return preferences
