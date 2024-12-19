from kivy.app import App
from kivy.uix.carousel import Carousel
from kivy.uix.label import Label
class MinhaApp(App):
    def build(self):
        #Criando um Carousel
        carousel=Carousel()
        #Adicionando widgets ao Carousel
        for i in range(3): 
            label=Label(text=f"Slide {i+1}") 
            carousel.add_widget(label)
        
        return carousel

if __name__=="__main__":
    MinhaApp().run()
