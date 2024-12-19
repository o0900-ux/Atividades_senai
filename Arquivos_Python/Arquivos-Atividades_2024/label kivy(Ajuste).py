from kivy.app import App 
from kivy.uix.label import Label

class Umalabel(App):
    def build(self):
        return Label (
            text ='Teste de "Label"', 
            color = (1, 1, 0, 1), 
            bold=True, 
            halign='left', 
            valign='top',
            text_size= (150, None),
            size_hint=(None, None),
            size=(150,50)
        )
        
    
if __name__ == '__main__':
    Umalabel().run()