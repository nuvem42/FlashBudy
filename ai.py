import random

class AIModel:
    def __init__(self, flashcards):
        self.flashcards = flashcards
        self.difficulty_weights = {
            "easy": 1,
            "medium": 2,
            "hard": 3
        }

    def get_recommendation(self):
        weighted_flashcards = []
        for fc in self.flashcards:
            weight = self.difficulty_weights[fc.difficulty]
            weighted_flashcards.extend([fc] * weight)
        return random.choice(weighted_flashcards) if weighted_flashcards else None

    def update_difficulty(self, flashcard, difficulty):
        flashcard.difficulty = difficulty
