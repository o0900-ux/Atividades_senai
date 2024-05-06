from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.image import AsyncImage
from kivy.core.window import Window
from kivy.utils import get_color_from_hex

class Telalogin(BoxLayout):
    def __init__(self, **kwargs):
        super(Telalogin, self).__init__(**kwargs)
        self.orientation = "vertical"
        self.padding = 20

        self.add_widget(AsyncImage(source='https://github.com/MateusN17/Reposit-rio-/blob/main/Kivy/images.png?raw=true'))
        
        self.add_widget(Label(text="Insira o seu E-mail", color=(0, 0, 0.2, 1),bold=True,font_size= 26))
        self.Email = TextInput(hint_text="Digite o Seu E-mail")
        self.add_widget(self.Email)
        
        self.add_widget(Label(text="Insira sua Senha:", color=(0, 0, 0.2, 1),bold=True,font_size= 26))
        self.Senha = TextInput(hint_text="Digite sua senha", password=True)
        self.add_widget(self.Senha)
        
        botao_layout = BoxLayout(padding=8)
        self.add_widget(botao_layout)
        
        self.enviar = Button(text="Enviar", background_color=get_color_from_hex('#3498db'))
        self.enviar.bind(on_press=self.Login)
        botao_layout.add_widget(self.enviar)
        
        self.cancelar = Button(text="Cancelar", background_color=get_color_from_hex('#ff0000'))
        self.cancelar.bind(on_press=self.botao_cancelar)
        botao_layout.add_widget(self.cancelar)
        
    def Login(self, instance):
        print("Nome de usuário:", self.Email.text)
        print("Senha:", self.Senha.text)
    
    def botao_cancelar(self, instance):
        print("Login cancelado.")

class Umatela(App):
    def build(self):
        Window.clearcolor = (1, 1, 1, 1)
        return Telalogin()

Window.size = (360, 640)  

if __name__ == '__main__':
    Umatela().run()
