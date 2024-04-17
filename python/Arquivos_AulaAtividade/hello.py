from kivy.app import App
from kivy.uix.button import Button

class MyApp(App):
    def build(self):
        self.title='Meu primeiro app'
        return Button(text="Hello World")
       
if __name__ == '__main__':
    MyApp().run()


