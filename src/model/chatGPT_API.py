import requests
import json

class GPTAPI:
    def sendRequest(self, instruction_text, user_prompt, example_midi, deep_instruction, api_key, temperature):
        self.api_key = api_key
        self.temperature = temperature

        url = 'https://api.openai.com/v1/chat/completions'
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + api_key
        }
        data = {
            "model": "gpt-3.5-turbo",
            "messages": [{"role": "user", "content": instruction_text + user_prompt + example_midi + deep_instruction}],
            "temperature": temperature
        }
        response = requests.post(url, headers=headers, json=data)
        response = response.text

        # Print message if request is invalid
        json_response = json.loads(response)
        if 'error' in json_response:
            error_message = json_response['error']['message']
            error_type = json_response['error']['type']
            print(f"{error_type}\n{error_message}\nCheck your API key!")
            return None

        return response

    def extractContent(self, response):
        try:
            # Parse the JSON response
            json_response = json.loads(response)

            # Get the 'content' content only from the JSON response
            content = json_response['choices'][0]['message']['content']

            # Remove '\n' and leading/trailing spaces from the content
            clean_content_response = content.strip().replace('\n', '')

            # Return the cleaned string
            return clean_content_response
        except (json.JSONDecodeError, KeyError):
            print("Invalid response object.")
            return None


def main():
    instruction_text = ""
    user_prompt = "Give me happy birthday in E-minor"
    example_midi = ""  # Add the example MIDI here if needed
    deep_instruction = ""
    api_key = "YOUR_API_KEY"  # Replace with your actual API key
    temperature = 0.7

    gpt_api = GPTAPI()
    json_response = gpt_api.sendRequest(instruction_text, user_prompt, example_midi, deep_instruction, api_key, temperature)
    if json_response is not None:
        answer = gpt_api.extractContent(json_response)
        if answer is not None:
            print(answer)


if __name__ == '__main__':
    main()
