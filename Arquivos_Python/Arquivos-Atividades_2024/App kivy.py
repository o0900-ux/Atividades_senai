from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
 
class MinhaApp(App):
    def build(self):
    # Layout principal
        layout_principal=BoxLayout(orientation='vertical')
    # Widget de entrada para o nome do usuário
        self.input_nome=TextInput (hint_text='Digite seu nome')
        layout_principal.add_widget(self.input_nome)
    #Botão para enviar o nome e exibir a mensagem
        botao_enviar = Button(text='Enviar', on_press=self.exibir_mensagem)
        layout_principal.add_widget(botao_enviar)
    # Label para exibir a mensagem
        self.label_mensagem=Label()
        layout_principal.add_widget(self.label_mensagem)
        return layout_principal
    def exibir_mensagem(self, instance):
        nome_usuario=self.input_nome.text
        mensagem=f'Olá {nome_usuario}, você está avançando no Kivy! Parabéns SESIANO!!!'
        self.label_mensagem.text=mensagem
if __name__=="__main__":
    MinhaApp().run()
