from kivy.config import Config
Config.set('graphics', 'width', '360')
Config.set('graphics', 'height', '640')
Config.set('graphics', 'resizable', False)

from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.metrics import dp
from kivy.uix.textinput import TextInput
import os
from kivy.properties import BooleanProperty
from kivy.lang import Builder
from kivymd.uix.list import OneLineIconListItem
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivymd.uix.snackbar import Snackbar
from kivymd.uix.textfield import MDTextField
from kivymd.uix.selectioncontrol import MDSwitch
from kivymd.uix.label import MDLabel
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.uix.switch import Switch
from kivymd.uix.card import MDCard
from kivy.uix.image import Image
from kivy.clock import Clock
import pyrebase

firebaseConfig = {
    'apiKey': "AIzaSyA3gOHi9Q6aHQ5seN5S9bbNmQpPQFMGXFs",
    'authDomain': "magnus-c4b38.firebaseapp.com",
    'databaseURL': "https://magnus-c4b38-default-rtdb.firebaseio.com",
    'projectId': "magnus-c4b38",
    'storageBucket': "magnus-c4b38.appspot.com",
    'messagingSenderId': "458576341456",
    'appId': "1:458576341456:web:6117f4a9160b8667b8f1d5"
}

firebase = pyrebase.initialize_app(firebaseConfig)
database = firebase.database()

class SplashScreen(Screen):
    def __init__(self, **kwargs):
        super(SplashScreen, self).__init__(**kwargs)
        self.image = Image(source='logo.png', size_hint=(0.9, 0.9),
                           pos_hint={'center_x': 0.5, 'center_y': 0.55})
        self.add_widget(self.image)

    def on_enter(self):
        Clock.schedule_once(self.dismiss_screen, 8)

    def dismiss_screen(self, dt):
        self.manager.current = 'Entrar_login'  

class TelaEntrarLogin(Screen):
    def Login(self):
        email = self.ids.email.text
        senha = self.ids.senha.text
        
        if not email or not senha:
            print("Por favor, preencha todos os campos.")
            return
        
        try:
            firebase = pyrebase.initialize_app(firebaseConfig)
            auth = firebase.auth()
            user = auth.sign_in_with_email_and_password(email, senha)
            print("Login realizado com sucesso.")
            self.manager.current = 'Menu'
        except Exception as e:
            print("Erro ao fazer login:", e)

class TelaEntrarLoginJuridico(Screen):
     def LoginJuridico(self):
        cnpj = self.ids.cnpj.text
        email = self.ids.email.text
        senha = self.ids.senha.text
        
        if not all([cnpj, email, senha]):
            print("Por favor, preencha todos os campos.")
            return
        
        try:
            firebase = pyrebase.initialize_app(firebaseConfig)
            auth = firebase.auth()
            user = auth.sign_in_with_email_and_password(email, senha)
            print("Login realizado com sucesso.")
            self.manager.current = 'Menu'
        except Exception as e:
            print("Erro ao fazer login:", e)

class TelaCriarConta(Screen):
    def Cadastra(self):
        nome = self.ids.nome.text
        nome_social = self.ids.nome_social.text
        cpf = self.ids.cpf.text
        email = self.ids.email.text
        senha = self.ids.senha.text
        confirmar_senha = self.ids.confirmar_senha.text
        data_nascimento = self.ids.data_nascimento.text
        
        if not all([nome, cpf, email, senha, confirmar_senha, data_nascimento]):
            print("Por favor, preencha todos os campos.")
            return
        
        if senha != confirmar_senha:
            print("As senhas não coincidem.")
            return
        
        try:
            firebase = pyrebase.initialize_app(firebaseConfig)
            auth = firebase.auth()
            user = auth.create_user_with_email_and_password(email, senha)
            db = firebase.database()
            data = {
                "nome": nome,
                "nome_social": nome_social,
                "cpf": cpf,
                "email": email,
                "data_nascimento": data_nascimento
            }
            db.child("users").child(user["localId"]).set(data)
            print("Usuário registrado com sucesso.")
        except Exception as e:
            print("Erro ao registrar o usuário:", e)

class TelaCriarContaJuridico(Screen):
     def CadastrarJuridico(self):
        nome_empresa = self.ids.nome_empresa.text
        email = self.ids.email.text
        senha = self.ids.senha.text
        telefone = self.ids.telefone.text
        cnpj = self.ids.cnpj.text
        
        if not all([nome_empresa, email, senha, telefone, cnpj]):
            print("Por favor, preencha todos os campos.")
            return
        
        try:
            firebase = pyrebase.initialize_app(firebaseConfig)
            auth = firebase.auth()
            user = auth.create_user_with_email_and_password(email, senha)
            db = firebase.database()
            data = {
                "nome_empresa": nome_empresa,
                "email": email,
                "telefone": telefone,
                "cnpj": cnpj
            }
            db.child("users_juridicos").child(user["localId"]).set(data)
            print("Conta jurídica registrada com sucesso.")
        except Exception as e:
            print("Erro ao registrar a conta jurídica:", e)
            


class TelaMenu(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.on_enter = self.carregar_vagas

    def carregar_vagas(self):
        try:
            vagas = database.child("posts").get().val()
            self.ids.vagas_box.clear_widgets() 
            if vagas:
                for key, vaga in vagas.items():
                    self.adicionar_vaga(vaga)
            else:
                print("Nenhuma vaga encontrada.")
        except Exception as e:
            print("Erro ao carregar vagas:", e)

    def adicionar_vaga(self, vaga):
        especificacao = vaga.get('especificacao', 'N/A')
        cargo = vaga.get('cargo', 'N/A')
        local_de_trabalho = vaga.get('local_de_trabalho', 'N/A')
        localidade = vaga.get('localidade', 'N/A')
        tipo_de_vaga = vaga.get('tipo_de_vaga', 'N/A')
        sobre_vaga = vaga.get('sobre_vaga', 'N/A')
        user_name = vaga.get('user_name', 'N/A')

        card = MDCard(
            orientation='vertical',
            size_hint=(1, None),
            height=dp(180),
            pos_hint={"center_x": 0.5},
            padding=dp(10),
            spacing=dp(10),
        )
        card.add_widget(MDLabel(text=f"Especificação: {especificacao}"))
        card.add_widget(MDLabel(text=f"Cargo: {cargo}"))
        card.add_widget(MDLabel(text=f"Local de Trabalho: {local_de_trabalho}"))
        card.add_widget(MDLabel(text=f"Localidade: {localidade}"))
        card.add_widget(MDLabel(text=f"Tipo de Vaga: {tipo_de_vaga}"))
        card.add_widget(MDLabel(text=f"Sobre: {sobre_vaga}"))
        card.add_widget(MDLabel(text=f"usuario: {user_name}"))

        self.ids.vagas_box.add_widget(card)

class Telacriarvaga(Screen):
    especificacao = [
        'Administração e Escritório',
        'Tecnologia da Informação',
        'Marketing e Vendas',
        'Recursos Humanos',
        'Finanças',
        'Engenharia',
        'Saúde',
        'Educação',
        'Design e Criação',
        'Logística e Transporte',
        'Jurídico',
        'Atendimento ao Cliente',
        'Operações e Produção',
        'Cargos de Nível Executivo'
    ]
    cargo = [
        'Operacionais e de Suporte',
        'Técnico e Especializado',
        'Supervisão e Coordenação',
        'Gerência',
        'Chefia e Direção',
        'Executivos'
    ]
    local_de_trabalho = [
        'Presencial',
        'Híbrido',
        'Remoto'
    ]
    localidade  = [
        'AL - Arapiraca',
        'AL - Campo Alegre',
        'AL - Coruripe',
        'AL - Delmiro Gouveia',
        'AL - Maceió',
        'AL - Palmeira dos Índios',
        'AL - Penedo',
        'AL - Rio Largo',
        'AL - São Miguel dos Campos',
        'AL - União dos Palmares',
        'BA - Camaçari',
        'BA - Feira de Santana',
        'BA - Ilhéus',
        'BA - Itabuna',
        'BA - Jequié',
        'BA - Juazeiro',
        'BA - Lauro de Freitas',
        'BA - Salvador',
        'BA - Teixeira de Freitas',
        'BA - Vitória da Conquista',
        'CE - Caucaia',
        'CE - Crato',
        'CE - Fortaleza',
        'CE - Iguatu',
        'CE - Itapipoca',
        'CE - Juazeiro do Norte',
        'CE - Maracanaú',
        'CE - Maranguape',
        'CE - Quixadá',
        'CE - Sobral',
        'MA - Açailândia',
        'MA - Bacabal',
        'MA - Caxias',
        'MA - Codó',
        'MA - Imperatriz',
        'MA - Paço do Lumiar',
        'MA - Pinheiro',
        'MA - Santa Inês',
        'MA - São Luís',
        'MA - Timon',
        'PB - Bayeux',
        'PB - Cabedelo',
        'PB - Cajazeiras',
        'PB - Campina Grande',
        'PB - Guarabira',
        'PB - João Pessoa',
        'PB - Patos',
        'PB - Pombal',
        'PB - Santa Rita',
        'PB - Sousa',
        'PE - Cabo de Santo Agostinho',
        'PE - Camaragibe',
        'PE - Caruaru',
        'PE - Garanhuns',
        'PE - Jaboatão dos Guararapes',
        'PE - Olinda',
        'PE - Paulista',
        'PE - Petrolina',
        'PE - Recife',
        'PE - Vitória de Santo Antão',
        'PI - Altos',
        'PI - Barras',
        'PI - Campo Maior',
        'PI - Floriano',
        'PI - José de Freitas',
        'PI - Parnaíba',
        'PI - Picos',
        'PI - Piripiri',
        'PI - Teresina',
        'PI - União',
        'RN - Apodi',
        'RN - Caicó',
        'RN - Ceará-Mirim',
        'RN - Currais Novos',
        'RN - Macaíba',
        'RN - Mossoró',
        'RN - Natal',
        'RN - Parnamirim',
        'RN - Santa Cruz',
        'RN - São Gonçalo do Amarante',
        'SE - Aracaju',
        'SE - Estância',
        'SE - Itabaiana',
        'SE - Itaporanga DAjuda',
        'SE - Lagarto',
        'SE - Nossa Senhora do Socorro',
        'SE - Propriá',
        'SE - São Cristóvão',
        'SE - Simão Dias',
        'SE - Tobias Barreto'
    ]
    tipo_de_vaga = [
        'Tempo integral',
        'Meio período',
        'Contrato',
        'Temporário',
        'Outro',
        'Voluntário',
        'Estágio'
    ]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.selected_especificacao = None
        self.selected_cargo = None
        self.selected_local_de_trabalho = None
        self.selected_localidade = None
        self.selected_tipo_de_vaga = None
        self.user_name = None


    def show_especificacao(self, main_button):
        dropdown = DropDown()
        for option in self.especificacao:
            btn = Button(text=option, size_hint_y=None, height=dp(44))
            btn.bind(on_release=lambda btn: self.select_option(dropdown, btn.text, main_button, 'especificacao'))
            btn.background_color = (1, 1, 1, 1)
            btn.color = (0, 0, 0, 1)
            dropdown.add_widget(btn)
        dropdown.open(main_button)

    def show_cargo(self, main_button):
        dropdown = DropDown()
        for option in self.cargo:
            btn = Button(text=option, size_hint_y=None, height=dp(44))
            btn.bind(on_release=lambda btn: self.select_option(dropdown, btn.text, main_button, 'cargo'))
            btn.background_color = (1, 1, 1, 1)
            btn.color = (0, 0, 0, 1)
            dropdown.add_widget(btn)
        dropdown.open(main_button)

    def show_local_de_trabalho(self, main_button):
        dropdown = DropDown()
        for option in self.local_de_trabalho:
            btn = Button(text=option, size_hint_y=None, height=dp(44))
            btn.bind(on_release=lambda btn: self.select_option(dropdown, btn.text, main_button, 'local_de_trabalho'))
            btn.background_color = (1, 1, 1, 1)
            btn.color = (0, 0, 0, 1)
            dropdown.add_widget(btn)
        dropdown.open(main_button)

    def show_localidade(self, main_button):
        dropdown = DropDown()
        for option in self.localidade:
            btn = Button(text=option, size_hint_y=None, height=dp(44))
            btn.bind(on_release=lambda btn: self.select_option(dropdown, btn.text, main_button, 'localidade'))
            btn.background_color = (1, 1, 1, 1)
            btn.color = (0, 0, 0, 1)
            dropdown.add_widget(btn)
        dropdown.open(main_button)
    
    def show_tipo_de_vaga(self, main_button):
        dropdown = DropDown()
        for option in self.tipo_de_vaga:
            btn = Button(text=option, size_hint_y=None, height=dp(44))
            btn.bind(on_release=lambda btn: self.select_option(dropdown, btn.text, main_button, 'tipo_de_vaga'))
            btn.background_color = (1, 1, 1, 1)
            btn.color = (0, 0, 0, 1)
            dropdown.add_widget(btn)
        dropdown.open(main_button)

    def select_option(self, dropdown, text, main_button, option_type):
        main_button.text = text
        dropdown.dismiss()

        main_button.size_hint_x = None
        main_button.width = dp(200)

        if option_type == 'especificacao':
            self.selected_especificacao = text
        elif option_type == 'cargo':
            self.selected_cargo = text
        elif option_type == 'local_de_trabalho':
            self.selected_local_de_trabalho = text
        elif option_type == 'localidade':
            self.selected_localidade = text
        elif option_type == 'tipo_de_vaga':
            self.selected_tipo_de_vaga = text

    def salvar_vaga(self):
        if not all([self.selected_especificacao, self.selected_cargo, self.selected_local_de_trabalho, self.selected_localidade, self.selected_tipo_de_vaga]):
            print("Por favor, preencha todos os campos.")
            return
        
        sobre_vaga = self.ids.sobre_vaga.text
        user_name = self.ids.user_name_input.text

        if not user_name:
            print("Por favor, preencha o nome do usuário.")
            return

        try:
            data = {
                "especificacao": self.selected_especificacao,
                "cargo": self.selected_cargo,
                "local_de_trabalho": self.selected_local_de_trabalho,
                "localidade": self.selected_localidade,
                "tipo_de_vaga": self.selected_tipo_de_vaga,
                "sobre_vaga": sobre_vaga,
                "user_name": user_name 
            }
            if not database:
                print("Erro: Conexão com o banco de dados não configurada.")
                return
            database.child("posts").push(data)
            print("Vaga salva com sucesso.")
        except Exception as e:
            print("Erro ao salvar a vaga:", e)


class TelaPublicacoes(Screen):
     pass

class Telaconfignotificacoes(Screen):
    vagas = BooleanProperty(False)
    contratacao = BooleanProperty(False)
    mensagens = BooleanProperty(False)
    mencoes = BooleanProperty(False)
    publicar_comentar = BooleanProperty(False)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.load_settings()

    def on_pre_enter(self, *args):
        self.load_settings()

    def load_settings(self):
        settings = database.child("users").child("user_id").child("notification_settings").get().val()
        if settings:
            self.vagas = settings.get('vagas', False)
            self.contratacao = settings.get('contratacao', False)
            self.mensagens = settings.get('mensagens', False)
            self.mencoes = settings.get('mencoes', False)
            self.publicar_comentar = settings.get('publicar_comentar', False)

    def save_settings(self):
        settings = {
            'vagas': self.vagas,
            'contratacao': self.contratacao,
            'mensagens': self.mensagens,
            'mencoes': self.mencoes,
            'publicar_comentar': self.publicar_comentar,
        }
        database.child("users").child("user_id").child("notification_settings").set(settings)

class TelaconfigPrivacidadeDados(Screen):
    pass

class TelaconfigVisibilidade(Screen):
    pass

class TelaconfigSeguranca(Screen):
    pass

class TelaconfigPerfil(Screen):
    pass

class TelaSalvos(Screen):
    pass

class Telanotificacoes(Screen):
    pass

class TelaChat(Screen):
    pass

class TelaInformacoesPerfil(Screen):
    pass

class TelaEnderecoemail(Screen):
    pass

class TelaTrocarSenha(Screen):
    pass

class Telanumerostelefone(Screen):
    pass

class ItemConfirm(OneLineIconListItem):
    pass

class ConfigItem(OneLineIconListItem):
    pass

class LimitedMDTextField(MDTextField):
    max_text_length = 500
    def insert_text(self, substring, from_undo=False):
        if len(self.text) + len(substring) > self.max_text_length:
            substring = substring[:self.max_text_length - len(self.text)]
        return super().insert_text(substring, from_undo=from_undo)

class App(MDApp):
    dialog = None

    data = {
        'Bloquear': 'block-helper',
    }

    def build(self):
        Window.size = (dp(360), dp(640))  
        Window.clearcolor = (1, 1, 1, 1)
        self.screen_manager = ScreenManager()
        self.screen_manager.add_widget(Telaconfignotificacoes(name='config_notificacoes'))
        self.theme_cls.primary_palette = "Indigo"
        return Builder.load_file("main.kv")

    def show_logout_dialog(self):
        self.dialog = MDDialog(
            text="Deseja sair da conta?",
            buttons=[
                MDFlatButton(
                    text="Cancelar",
                    on_release=lambda *args: self.dialog.dismiss()
                ),
                MDFlatButton(
                    text="Sim",
                    on_release=lambda *args: self.logout_and_dismiss()
                )
            ]
        )
        self.dialog.open()
    
    def logout_and_dismiss(self):
        self.dialog.dismiss() 
        self.logout() 

    def logout(self):
        self.root.current = 'Entrar_login'

    def refresh_callback(self):
        print("Layout de atualização atualizado!")

    def switch_screen(self, screen_name):
        pass

    def showquem_pode_ver(self, main_button):
        self.quem_pode_ver = ['            Todos            ', 'Apenas Empresas']  
        dropdown = DropDown()
        for option in self.quem_pode_ver:
            btn = Button(text=option, size_hint_y=None, height=dp(44))
            btn.bind(on_release=lambda btn: self.select_option(dropdown, btn.text, main_button))
            btn.background_color = (1, 1, 1, 1)
            btn.color = (1, 1, 1, 1)
            dropdown.add_widget(btn)
        dropdown.open(main_button)

    def menu_callback(self, instance):
        Snackbar(text=instance.text).open()

    def confirm_action(self, dialog):
        selected_item = dialog.item.ids.container.text
        self.menu_callback(instance=selected_item)

    def select_option(self, dropdown, text, main_button):
        main_button.text = text
        dropdown.dismiss()
        main_button.size_hint_x = None
        main_button.width = dp(150)
    
    def update_notification_setting(self, key, value):
        screen = self.screen_manager.get_screen('config_notificacoes')
        setattr(screen, key, value)
        screen.save_settings()

    def open_link(self, url):
        import webbrowser
        webbrowser.open(url)

if __name__ == "__main__":
    App().run()