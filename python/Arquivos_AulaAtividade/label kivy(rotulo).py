from kivy.app import App 
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class Umalabel(App):
    def build(self):
        layout=BoxLayout(orientation='vertical')
        self.lab1=Label(
            text='senai- uma label', color=(0, 0, 1),
            font_size=40, bold=True
        )

        self.lab2=Label(
            text='senai- duas label', color=(0, 0, 1),
            font_size=40, bold=True, italic=True
        )

        self.lab3=Label(
            text='senai- três label', color=(0, 0, 1),
            font_size=40, bold=True, font_name='Arial',
            underline=True
        )

        layout.add_widget(self.lab1)
        layout.add_widget(self.lab2)
        layout.add_widget(self.lab3)
        return layout
        
    
if __name__ == '__main__':
    Umalabel().run()