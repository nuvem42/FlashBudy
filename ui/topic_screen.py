# ui/topic_screen.py
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from models import FlashcardManager

class TopicScreen(Screen):
    def __init__(self, **kwargs):
        super(TopicScreen, self).__init__(**kwargs)
        self.flashcard_manager = FlashcardManager()
        self.layout = BoxLayout(orientation='vertical')
        self.layout.add_widget(Label(text='Select a Topic'))
        self.add_topics()
        self.add_widget(self.layout)

    def add_topics(self):
        topics = set(fc.topic for fc in self.flashcard_manager.flashcards)
        for topic in topics:
            self.layout.add_widget(Button(text=topic, on_press=self.select_topic))

    def select_topic(self, instance):
        selected_topic = instance.text
        flashcards = self.flashcard_manager.get_flashcards_by_topic(selected_topic)
        self.show_flashcards(flashcards)

    def show_flashcards(self, flashcards):
        self.layout.clear_widgets()
        if flashcards:
            for flashcard in flashcards:
                card_layout = BoxLayout(orientation='vertical')
                card_layout.add_widget(Label(text=flashcard.question))
                card_layout.add_widget(Label(text=flashcard.answer))
                self.layout.add_widget(card_layout)
        else:
            self.layout.add_widget(Label(text='No flashcards available for this topic'))
        self.layout.add_widget(Button(text='Back', on_press=self.go_back))

    def go_back(self, instance):
        self.layout.clear_widgets()
        self.layout.add_widget(Label(text='Select a Topic'))
        self.add_topics()
