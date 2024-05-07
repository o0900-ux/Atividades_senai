from kivy.config import Config

Config.set('graphics', 'width', '360')
Config.set('graphics', 'height', '640')
Config.set('graphics', 'resizable', False)

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.image import AsyncImage
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
import mysql.connector

class TelaPerfil(BoxLayout):
    def __init__(self, email, **kwargs):
        super(TelaPerfil, self).__init__(**kwargs)
        self.orientation = "vertical"
        self.spacing = 10  
        self.padding = 20
        
        self.add_widget(Label(text=f"Bem-vindo, {email}", color=(0, 0, 0.2, 1), bold=True, font_size=26))
        
        botao_layout = BoxLayout(padding=8)
        self.add_widget(botao_layout)
        
        self.deslogar = Button(text="Deslogar", background_color=get_color_from_hex('#ff0000') )
        self.deslogar.bind(on_press=self.Deslogar)
        botao_layout.add_widget(self.deslogar)
        
    def Deslogar(self, instance):
        App.get_running_app().change_screen("login") 

class Telalogin(BoxLayout):
    def __init__(self, **kwargs):
        super(Telalogin, self).__init__(**kwargs)
        self.orientation = "vertical"
        self.spacing = 10  
        self.padding = 20

        self.add_widget(AsyncImage(source='https://github.com/MateusN17/Reposit-rio-/blob/main/Kivy/images.png?raw=true'))
        
        self.add_widget(Label(text="Insira o seu E-mail", color=(0, 0, 0.2, 1), bold=True, font_size=26, size_hint_y=None, height=40))
        self.Email = TextInput(hint_text="Digite o Seu E-mail", multiline=False, width=410, size_hint=(None, None), height=40)
        self.add_widget(self.Email)
        
        self.add_widget(Label(text="Insira sua Senha:", color=(0, 0, 0.2, 1), bold=True, font_size=26, size_hint_y=None, height=40))
        self.Senha = TextInput(hint_text="Digite sua senha", password=True, multiline=False, width=410, size_hint=(None, None), height=40)
        self.add_widget(self.Senha)
        
        botao_layout = BoxLayout(padding=8, size_hint_y=None, height=100)
        self.add_widget(botao_layout)
        
        self.enviar = Button(text="Cadastra", background_color=get_color_from_hex('#3498db'), size_hint=(None, None), width=200, height=50, )
        self.enviar.bind(on_press=self.Cadastra)
        botao_layout.add_widget(self.enviar)
        
        self.login = Button(text="login", background_color=get_color_from_hex('#ff0000'), size_hint=(None, None), width=200, height=50, )
        self.login.bind(on_press=self.Login)
        botao_layout.add_widget(self.login)

        self.esquecisenha = Button(text="Esqueceu a senha ?", color=(0, 0, 0.2, 1), bold=True, font_size=16, background_color=(1, 1, 1, 0), size_hint_y=None, height=50)
        self.esquecisenha.bind(on_press=self.reset_senha)
        self.add_widget(self.esquecisenha)
        
    def Cadastra(self, instance):
        email = self.Email.text
        senha = self.Senha.text
        if email.strip() == "" or senha.strip() == "":
            print("Por favor, preencha todos os campos.")
            return
        try:
            connection = mysql.connector.connect(
                host="127.0.0.1",
                user="root",
                database="usuarios"
            )
            cursor = connection.cursor()
            query = "SELECT id FROM users WHERE email = %s"
            cursor.execute(query, (email,))
            result = cursor.fetchall() 
            if result:
                print("Este email já está cadastrado.")
                return
            query = "INSERT INTO users (email, senha) VALUES (%s, %s)"
            cursor.execute(query, (email, senha))
            connection.commit()
            print("Usuário registrado com sucesso.")
        except Exception as e:
            print("Erro ao registrar o usuário:", e)
        finally:
            if 'connection' in locals():
                cursor.close()
                connection.close()
    
    def Login(self, instance):
        email = self.Email.text
        senha = self.Senha.text
        if email.strip() == "" or senha.strip() == "":
            print("Por favor, preencha todos os campos.")
            return
        try:
            connection = mysql.connector.connect(
                host="127.0.0.1",
                user="root",
                database="usuarios"
            )
            cursor = connection.cursor()
            query = "SELECT id FROM users WHERE email = %s AND senha = %s"
            cursor.execute(query, (email, senha))
            result = cursor.fetchone()
            if result:
                App.get_running_app().change_screen("perfil") 
            else:
                print("Email ou senha incorretos.")
        except Exception as e:
            print("Erro ao verificar login:", e)
        finally:
            if 'connection' in locals():
                cursor.close()
                connection.close()

    def reset_senha(self, instance):
        print("Redefinir senha")


class Umatela(App):
    def build(self):
        Window.clearcolor = (1, 1, 1, 1)
        self.login_screen = Telalogin()
        
        return self.login_screen

    def change_screen(self, screen_name):
        # Método para trocar de tela
        if screen_name == "perfil":
            # Se o nome da tela for "perfil", cria e mostra a tela de perfil
            self.profile_screen = TelaPerfil(email=self.login_screen.Email.text)  # Passando o email do usuário logado
            self.root.clear_widgets()  # Remove todos os widgets da tela atual
            self.root.add_widget(self.profile_screen)  # Adiciona a tela de perfil à raiz do aplicativo
        elif screen_name == "login":
            # Se o nome da tela for "login", cria uma nova instância da tela de login e mostra ela
            self.login_screen = Telalogin()
            self.root.clear_widgets()  # Remove todos os widgets da tela atual
            self.root.add_widget(self.login_screen)  # Adiciona a nova instância da tela de login à raiz do aplicativo


if __name__ == '__main__':
    Umatela().run()
