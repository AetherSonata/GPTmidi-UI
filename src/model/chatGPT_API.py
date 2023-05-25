
import requests

class GPTAPI:

    def sendRequest(self, instruction_text, user_prompt,  deep_instruction, api_key, temperature):
        self.api_key = api_key
        self.temperature = temperature

        url = 'https://api.openai.com/v1/chat/completions'
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer' + api_key
        }
        data = {
            "model": "gpt-3.5-turbo",
            "messages": [{"role": "user", "content": instruction_text + user_prompt + deep_instruction}],
            "temperature": temperature
        }
        response = requests.post(url, headers=headers, json=data)
        response = response.text
        
        print(response)


def main():
    instruction_text = "We will now create a .mid file text. In the following prompt I will describe my idea of a musical piece and you will give me back a .mid file in the stlye of:0 Tempo 500000\n 0 TimeSig 4/4 24 8\n 0 NoteOn ch=1 n=60 v=64\n 240 NoteOff ch=1 n=60 v=64\n The prompt starts now:"
    user_prompt = "Give me happy birthday in Eminor"
    deep_instruction = "Please ensure that the generated MIDI file has precise and consistent timings on 1/16th, 1/8th, 1/4th, 1/2th, and 1/1 note durations. Pay careful attention to the rhythmic grid and align all notes and events to these specified durations. Avoid irregular or fluctuating timings and strive for a steady and accurate rhythmic feel throughout the MIDI file. If necessary, you can quantize the generated MIDI file to fix any timing inconsistencies. Maintain the musicality and expression while adhering to the requested timing precision."
    api_key = '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'
    temperature = 0.7

    gpt_api = GPTAPI()
    gpt_api.sendRequest(instruction_text, user_prompt, deep_instruction, api_key, temperature)

if __name__ == '__main__':
    main()
        
        
    