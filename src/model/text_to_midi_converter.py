import mido

def convert_text_to_midi(text, output_filename):

    try:
        # Create a new MIDI file
        midi_file = mido.MidiFile(ticks_per_beat=480, type=1)

        # Create a new track
        track = mido.MidiTrack()

        # Process each line of the text
        for line in text.strip().split('\n'):
            line = line.strip()
            if line:
                parts = line.split()
                tick = int(parts[0])
                command = parts[1]

                if command == 'Tempo':
                    # Tempo event
                    tempo = int(parts[2])
                    track.append(mido.MetaMessage('set_tempo', tempo=tempo, time=tick))
                elif command == 'TimeSig':
                    # Time signature event
                    numerator, denominator = map(int, parts[2].split('/'))
                    clock_ticks_per_click = int(parts[3])
                    notated_32nd_notes_per_beat = int(parts[4])
                    track.append(mido.MetaMessage('time_signature', numerator=numerator, denominator=denominator, clocks_per_click=clock_ticks_per_click, notated_32nd_notes_per_beat=notated_32nd_notes_per_beat, time=tick))
                elif command == 'NoteOn':
                    # Note on event
                    channel = int(parts[2].split('=')[1])
                    note = int(parts[3].split('=')[1])
                    velocity = int(parts[4].split('=')[1])
                    track.append(mido.Message('note_on', note=note, velocity=velocity, time=tick, channel=channel))
                elif command == 'NoteOff':
                    # Note off event
                    channel = int(parts[2].split('=')[1])
                    note = int(parts[3].split('=')[1])
                    velocity = int(parts[4].split('=')[1])
                    track.append(mido.Message('note_off', note=note, velocity=velocity, time=tick, channel=channel))

        # Add the track to the MIDI file
        midi_file.tracks.append(track)

        # Save the MIDI file
        midi_file.save(output_filename)
        
        print("MIDI conversion successful.")

        # for checking purposes
        successful = 1
        return successful
    
    except Exception as e:
        print(f"Error occurred while converting text to MIDI: {e} \n Text could not be converted")


