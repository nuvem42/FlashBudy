# ui/edit_flashcard_screen.py
# ui/edit_flashcard_screen.py
from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from models import FlashcardManager

class EditFlashcardScreen(Screen):
    def __init__(self, **kwargs):
        super(EditFlashcardScreen, self).__init__(**kwargs)
        self.flashcard_manager = FlashcardManager()
        self.layout = BoxLayout(orientation='vertical')
        
        self.id_input = TextInput(hint_text='ID')
        self.question_input = TextInput(hint_text='Question')
        self.answer_input = TextInput(hint_text='Answer')
        self.topic_input = TextInput(hint_text='Topic')
        self.difficulty_input = TextInput(hint_text='Difficulty')
        
        self.layout.add_widget(self.id_input)
        self.layout.add_widget(self.question_input)
        self.layout.add_widget(self.answer_input)
        self.layout.add_widget(self.topic_input)
        self.layout.add_widget(self.difficulty_input)
        
        self.save_button = Button(text='Save Flashcard', on_press=self.save_flashcard)
        self.layout.add_widget(self.save_button)
        self.add_widget(self.layout)

    def save_flashcard(self, instance):
        flashcard_id = int(self.id_input.text)
        question = self.question_input.text
        answer = self.answer_input.text
        topic = self.topic_input.text
        difficulty = self.difficulty_input.text
        
        self.flashcard_manager.edit_flashcard(flashcard_id, question, answer, topic, difficulty)
        self.flashcard_manager.save_flashcards()
        self.reset_form()

    def reset_form(self):
        self.id_input.text = ''
        self.question_input.text = ''
        self.answer_input.text = ''
        self.topic_input.text = ''
        self.difficulty_input.text = ''
