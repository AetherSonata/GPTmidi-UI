import mido

def convert_midi_to_text(midi_file_path):
    midi = mido.MidiFile(midi_file_path)
    text = ""

    for message in midi:
        if message.type == 'set_tempo':
            tempo = message.tempo
            text += f"0 Tempo {tempo}\n"
        elif message.type == 'time_signature':
            numerator = message.numerator
            denominator = message.denominator
            metronome = message.clocks_per_click
            thirty_seconds = message.notated_32nd_notes_per_beat
            text += f"0 TimeSig {numerator}/{denominator} {metronome} {thirty_seconds}\n"
        elif message.type == 'note_on':
            channel = message.channel + 1
            note = message.note
            velocity = message.velocity
            text += f"{message.time} NoteOn ch={channel} n={note} v={velocity}\n"
        elif message.type == 'note_off':
            channel = message.channel + 1
            note = message.note
            velocity = message.velocity
            text += f"{message.time} NoteOff ch={channel} n={note} v={velocity}\n"

    return text
