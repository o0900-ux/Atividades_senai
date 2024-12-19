from kivy.app import App 
from kivy.uix.label import Label

class Umalabel(App):
    def build(self):
        return Label (text = 'Teste de "Label"' , color = (1, 1, 0, 1), bold=True, font_size=100, font_name='arial')
        
    
if __name__ == '__main__':
    Umalabel().run()