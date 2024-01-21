import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

import random
kivy.require('1.9.0')

# Build to Android
# Buildozer



class MyRoot(BoxLayout):
    
    def __init__(self):
        super(MyRoot, self).__init__()
        
    def generate_number(self):
        self.random_label.text = str(random.randint(1, 100))

class YourAIApp(App):
    def build(self):
        return MyRoot()
    
app = YourAIApp()
app.run()