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
        self.label = Label(text='', font_size='20sp', size_hint_y=None, halign='center', color = (1, 1, 0, 1))
        layout.add_widget(self.label)

        texto = """
        Tarzan.
        \n
        Quem foi que disse que eu era forte?
        Nunca pratiquei esporte, nem conheço futebol...
        O meu parceiro sempre foi o travesseiro
        E eu passo o ano inteiro sem ver um raio de sol
        A minha força bruta reside
        Em um clássico cabide, já cansado de sofrer
        Minha armadura é de casimira dura
        Que me dá musculatura, mas que pesa e faz doer
        \n
        Eu poso pros fotógrafos, e destribuo autógrafos
        A todas as pequenas lá da praia de manhã
        Um argentino disse, me vendo em Copacabana:
        'No hay fuerza sobre-humana que detenga este Tarzan'
        \n
        De lutas não entendo abacate
        Pois o meu grande alfaiate não faz roupa pra brigar
        Sou incapaz de machucar uma formiga
        Não há homem que consiga nos meus músculos pegar
        Cheguei até a ser contratado
        Pra subir em um tablado, pra vencer um campeão
        Mas a empresa, pra evitar assassinato
        Rasgou logo o meu contrato quando me viu sem roupão
        \n
        Eu poso pros fotógrafos, e destribuo autógrafos
        A todas as pequenas lá da praia de manhã
        Um argentino disse, me vendo em Copacabana:
        'No hay fuerza sobre-humana que detenga este Tarzan'
        \n
        Quem foi que disse que eu era forte?
        Nunca pratiquei esporte, nem conheço futebol...
        O meu parceiro sempre foi o travesseiro
        E eu passo o ano inteiro sem ver um raio de sol
        A minha força bruta reside
        Em um clássico cabide, já cansado de sofrer
        Minha armadura é de casimira dura
        Que me dá musculatura, mas que pesa e faz doer
        """

        self.frases = texto.split("\n\n")
        self.index = 0
        self.mostrar_texto()

        self.sound = SoundLoader.load('Tarzan.mp3')
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