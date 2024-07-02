import json
import os

class Flashcard:
    def __init__(self, id, question, answer, topic, difficulty):
        self.id = id
        self.question = question
        self.answer = answer
        self.topic = topic
        self.difficulty = difficulty

class FlashcardManager:
    def __init__(self, data_file='data/flashcards.json'):
        self.data_file = data_file
        self.flashcards = self.load_flashcards()

    def load_flashcards(self):
        if not os.path.exists(self.data_file):
            return []
        with open(self.data_file, 'r') as file:
            data = json.load(file)
            return [Flashcard(**fc) for fc in data]

    def save_flashcards(self):
        with open(self.data_file, 'w') as file:
            json.dump([fc.__dict__ for fc in self.flashcards], file, indent=4)

    def add_flashcard(self, question, answer, topic, difficulty):
        new_id = max([fc.id for fc in self.flashcards], default=0) + 1
        flashcard = Flashcard(new_id, question, answer, topic, difficulty)
        self.flashcards.append(flashcard)
        self.save_flashcards()

    def edit_flashcard(self, id, question, answer, topic, difficulty):
        for fc in self.flashcards:
            if fc.id == id:
                fc.question = question
                fc.answer = answer
                fc.topic = topic
                fc.difficulty = difficulty
                self.save_flashcards()
                break

    def delete_flashcard(self, id):
        self.flashcards = [fc for fc in self.flashcards if fc.id != id]
        self.save_flashcards()

    def get_flashcards_by_topic(self, topic):
        return [fc for fc in self.flashcards if fc.topic == topic]

    def get_flashcards_by_difficulty(self, difficulty):
        return [fc for fc in self.flashcards if fc.difficulty == difficulty]

    def get_random_flashcard(self):
        import random
        return random.choice(self.flashcards) if self.flashcards else None
