# ui/__init__.py
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from ui.main_screen import MainScreen
from ui.flashcard_screen import FlashcardScreen
from ui.topic_screen import TopicScreen
from ui.edit_flashcard_screen import EditFlashcardScreen

class FlashcardApp(App):
    def build(self):
        sm = ScreenManager()

        main_screen = MainScreen(name='main')
        flashcard_screen = FlashcardScreen(name='flashcard')
        topic_screen = TopicScreen(name='topic')
        edit_flashcard_screen = EditFlashcardScreen(name='edit_flashcard')

        print(f"Adding {main_screen.name} to ScreenManager")
        sm.add_widget(main_screen)

        print(f"Adding {flashcard_screen.name} to ScreenManager")
        sm.add_widget(flashcard_screen)

        print(f"Adding {topic_screen.name} to ScreenManager")
        sm.add_widget(topic_screen)

        print(f"Adding {edit_flashcard_screen.name} to ScreenManager")
        sm.add_widget(edit_flashcard_screen)

        return sm

if __name__ == '__main__':
    FlashcardApp().run()
