from kivy.app import App
from kivy.uix.label import Label
from kivy.core.window import Window
class MinhaApp(App):
    def build(self):
        # Definindo a cor de fundo da janela como branco
        Window.clearcolor = (1, 1, 1, 1) 
        # (R, G, B, A) -> RGB-1 para branco, A 1 para opacidade total
        
        # Criando um rótulo com texto preto 
        label=Label(text='Esta é uma tela com fundo branco', color=(0, 0, 0, 1)) 
        # (R, G, B, A) RGB 0 para preto, A 1 para opacidade total
        return label
if __name__ =="__main__":
    MinhaApp().run()
