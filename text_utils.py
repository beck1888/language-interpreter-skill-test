from random import choice

def get_random_pronoun() -> str:
    return choice(["him, her"])

def get_random_country() -> str:
    return choice(["Mexico", "China", "Russia", "Canada", "Spain", "Germany"])

def get_random_topic() -> str:
    return choice([
        "border control", "oil", "trade", "joint cultural celebration", "climate change", 
        "economic cooperation", "military alliances", "space exploration", "technology exchange", 
        "human rights", "education partnerships", "healthcare initiatives", "tourism promotion", 
        "agricultural development", "infrastructure projects", "energy resources", 
        "scientific research", "cultural exchange programs", "disaster relief", "cybersecurity"
    ])

def round_up_to_half_builtin(number):
    """Rounds a number up to the nearest 0.5 using the built-in round() function."""
    return round(number + 0.25, 1)

def calculate_speaking_time(sentence: str) -> float:
    SECONDS_PER_WORD: float = 0.45 # Allow a longer speaking time
    speaking_time_specific: float = len(sentence.split()) * SECONDS_PER_WORD
    return round_up_to_half_builtin(speaking_time_specific)

if __name__ == '__main__':
    print("This file is not meant to be ran directly. Please run main.py instead.")
    raise SystemExit(1)
