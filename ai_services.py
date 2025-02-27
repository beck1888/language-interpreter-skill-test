from openai import OpenAI
from text_utils import get_random_pronoun, get_random_country, get_random_topic

def transcribe(file_path_of_recording: str) -> str:
    client: OpenAI = OpenAI()
    audio_file = open(file_path_of_recording, "rb")
    transcription = client.audio.transcriptions.create(
        model="whisper-1",
        file=audio_file
    )
    client.close()
    return transcription.text

def llm_response() -> str:
    # return "Please bring me a glass of water"
    client: OpenAI = OpenAI()
    response: str = client.chat.completions.create(
        model="gpt-4o-mini",
        temperature=1,
        messages=[
            {
                "role": "system",
                "content": "You are a speech writer for 1-2 sentence speeches. You use short, basic, and simple words. Your responses are as short as possible, never over 30 words."
            },
            {
                "role": "user",
                "content": f"Pretend you are the US president sitting down with the president of {get_random_country()}. Greet {get_random_pronoun()}, ask how they are, say the point of this meeting is to discuss {get_random_topic()}, and give an opening question."
            }
        ]
    ).choices[0].message.content
    client.close()
    return response

def translate_text(text: str, target_lang: str = "Spanish") -> str:
    client: OpenAI = OpenAI()
    response: str = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": "You are an expert translator who translates text word-for-word while adjusting grammar when needed."
            },
            {
                "role": "user",
                "content": f"Please translate this text to {target_lang}: {text}"
            }
        ]
    ).choices[0].message.content
    client.close()
    return response

def generate_text_to_speech(text_to_speak: str, save_file_as: str, voice: str = 'onyx') -> None:
    client: OpenAI = OpenAI()
    speech = client.audio.speech.create(
        input=text_to_speak,
        voice=voice,
        model='tts-1'
    ).write_to_file(save_file_as)
    client.close()

def get_how_similar(original_text_translated: str, interpretation: str) -> str:
    client: OpenAI = OpenAI()
    response: str = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": "You are an expert in rating translation. Evaluate how accurate the interpretation was and why (cite parts). Give it a grade from A+ to F. The user is the one who did the translation. Address them directly with 'you'. Be gentle. Keep responses very short."
            },
            {
                "role": "user",
                "content": f"Here is the original text: {original_text_translated}."
            },
            {
                "role": "user",
                "content": f"Here is the that text, interpreted to English: {interpretation}"
            }
        ]
    ).choices[0].message.content
    client.close()
    return response

if __name__ == '__main__':
    print("This file is not meant to be ran directly. Please run main.py instead.")
    raise SystemExit(1)
