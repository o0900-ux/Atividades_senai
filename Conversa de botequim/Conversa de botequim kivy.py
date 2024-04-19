from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from kivy.animation import Animation
from kivy.core.audio import SoundLoader
from kivy.uix.image import Image

class TextoApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        background = Image(source='img.jpg')
        layout.add_widget(background)
        self.label = Label(text='', font_size='20sp', size_hint_y=None, halign='center', color=(1, 0, 0, 1))
        layout.add_widget(self.label)

        texto = """
        Conversa de botequim.

        Seu garçom faça o favor de me trazer depressa 
        Uma boa média que não seja requentada 
        Um pão bem quente com manteiga à beça Um 
        guardanapo e um copo d'água bem gelada.

        Feche a porta da direita com muito cuidado Que 
        não estou disposto a ficar exposto ao sol 
        Vá perguntar ao seu freguês do 
        lado Qual foi o resultado do futebol.

        Se você ficar limpando a mesa Não me 
        levanto nem pago a despesa Vá pedir ao seu 
        patrão Uma caneta, um tinteiro
         Um envelope e um cartão.

        Não se esqueça de me dar palitos E um 
        cigarro pra espantar mosquitos Vá dizer 
        ao charuteiro Que me empreste umas 
        revistas Um isqueiro e um cinzeiro.

        Seu garçom faça o favor de me trazer 
        depressa Uma boa média que não seja requentada 
        Um pão bem quente com manteiga à 
        beça Um guardanapo e um copo d'água bem gelada.

        Feche a porta da direita com muito cuidado 
        Que não estou disposto a ficar exposto ao 
        sol Vá perguntar ao seu freguês do 
        lado Qual foi o resultado do futebol.

        Telefone ao menos uma vez Para 
        três-quatro-quatro-três-três-três 
        E ordene ao seu Osório 
        Que me mande um guarda-chuva Aqui 
        pro nosso escritório.

        Seu garçom me empresta algum 
        dinheiro Que eu deixei 
        o meu com o bicheiro Vá dizer 
        ao seu gerente Que pendure esta 
        despesa No cabide ali em frente.

        Seu garçom faça o favor de me 
        trazer depressa Uma
         boa média que não seja requentada 
        Um pão bem quente com manteiga à beça 
        Um guardanapo e um copo d'água bem gelada.

        Feche a porta da direita com
         muito cuidado Que 
        não estou disposto a ficar exposto 
        ao sol Vá perguntar ao seu freguês 
        do lado Qual foi o resultado do futebol.
        """

        self.frases = texto.split("\n\n")
        self.index = 0
        self.mostrar_texto()

        self.sound = SoundLoader.load('musica.mp3')
        if self.sound:
            self.sound.play()

        return layout

    def mostrar_texto(self, *args):
        if self.index < len(self.frases):
            self.label.text = self.frases[self.index]
            anim = Animation(opacity=1, duration=2)  
            anim += Animation(y=self.label.height, duration=15)  
            anim.start(self.label)
            self.index += 1
            Clock.schedule_once(self.mostrar_texto, 17)

if __name__ == '__main__':
    TextoApp().run()