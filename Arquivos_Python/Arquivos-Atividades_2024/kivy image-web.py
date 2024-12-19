from kivy.app import App
from kivy.uix.image import Image, AsyncImage
class MyApp(App):
 def build(self):
       
        return  AsyncImage (source='https://s2-oglobo.glbimg.com/E8XWh3VljU2_mPlMyK3zN8aNYIQ=/0x0:1300x929/888x0/smart/filters:strip_icc()/i.s3.glbimg.com/v1/AUTH_da025474c0c44edd99332dddb09cabe8/internal_photos/bs/2024/R/Z/H1mWvcToSMdM4uzDd1Vg/106718481-ri-rio-de-janeiro-rj-26-04-2024-entrevista-com-a-socialite-regina-goncalves-idosa-en.jpg')
if __name__ == '__main__':
    MyApp().run()
