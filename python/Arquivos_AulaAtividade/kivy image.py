from kivy.app import App
from kivy.uix.image import Image

class MyApp(App):
    def build(self):
        self.title='Kivy'
        return Image(source='Kivy_logo.png')
       
if __name__ == '__main__':
    MyApp().run()