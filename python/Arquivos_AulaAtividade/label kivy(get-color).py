from kivy.app import App 
from kivy.uix.label import Label
from kivy.utils import get_color_from_hex

class Umalabel(App):
    def build(self):
        return Label (text = 'Teste de "Label"' , color =get_color_from_hex('#ff5733'), bold=True, font_size=100, font_name='arial')
        
    
if __name__ == '__main__':
    Umalabel().run()