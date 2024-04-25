from kivy.app import App 
from kivy.uix.label import Label

class Umalabel(App):
    def build(self):
        return Label (
            text ='Teste de "Label"' , 
            color = (1, 1, 0, 1), 
            bold=True, 
            halign='left', 
            valign='top',
            font_size= 100
        )
        
    
if __name__ == '__main__':
    Umalabel().run()