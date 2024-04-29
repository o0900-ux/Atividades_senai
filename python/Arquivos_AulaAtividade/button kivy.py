from kivy.app import App
from kivy.uix.button import Button
from kivy.utils import get_color_from_hex

def botao(instance):
    print('ola mundo')

class MyApp(App):
    def build(self):
        self.title='Kivy'
        btn= Button(text="Clique aqui", size_hint=(0.5, 0.2), font_size=50, background_color=get_color_from_hex('#3498db'))
        btn.bind(on_press=botao)
        return btn
       
if __name__ == '__main__':
    MyApp().run()