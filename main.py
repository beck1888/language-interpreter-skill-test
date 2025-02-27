from playsound import playsound
import terminal
from text_utils import calculate_speaking_time
from audio_utils import (
    record_audio,
    play_audio_from_file
    )
from ai_services import (
    llm_response,
    translate_text,
    generate_text_to_speech,
    transcribe,
    get_how_similar
)
import os
import time

ENFORCE_MINIMUM_DELAY_TO_SPEECH: float = 5.0

def cleanup() -> None:
    os.remove('.tmp/speaker.mp3')
    os.remove('.tmp/mic.mp3')
    os.remove('.tmp/feedback.mp3')

def main() -> None:
    # Test

    if not os.path.exists('.tmp'):
        os.makedirs('.tmp')

    # Make the initial text
    start: float = time.time()
    playsound('public/ai-notice.mp3', False)
    with terminal.spinner("Initialing", "Initialized"):
        initial_text: str = llm_response()
        translated: str = translate_text(initial_text)
        generate_text_to_speech(translated, '.tmp/speaker.mp3', 'coral')


    if time.time() - start < ENFORCE_MINIMUM_DELAY_TO_SPEECH:
        print("Enforcing minimum delay.")
        time.sleep(ENFORCE_MINIMUM_DELAY_TO_SPEECH - (time.time() - start))

    print("Listen carefully!")
    play_audio_from_file('.tmp/speaker.mp3')

    # Record the mic for 5 seconds to let the user say the translation
    print("Say what you just heard in English! Speak loudly and clearly.")
    playsound('public/start.mp3', block=False)

    speaking_time: float = calculate_speaking_time(initial_text)
    with terminal.spinner(f"Recording audio for {str(speaking_time)} seconds", "Recorded audio"):
        record_audio(speaking_time, '.tmp/mic.mp3')
    playsound('public/stop.mp3', block=False)

    # Transcribe to score recording
    with terminal.spinner("Scoring response", "Scored response"):
        transcribed_interpretation: str = transcribe('.tmp/mic.mp3')
        score: str = get_how_similar(translated, transcribed_interpretation)

    # Show results
    print(f"\n\n\n\n\n\n\n\nDEBUG - YOU SAID: {transcribed_interpretation}")
    print("\n\n\n\n\n\n\n\n" + score + "\n\n")

    # generate_text_to_speech(score, 'feedback.mp3', 'shimmer')
    # playsound('feedback.mp3')


    # if input("\n\n>> Okay to clean (y/n)? ") == "y":
    #     cleanup()

if __name__ == '__main__':
    print("All voices you hear are AI generated, not a human speaking")
    main()