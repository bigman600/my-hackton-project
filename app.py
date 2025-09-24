# my weather app
import kivy 
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class MyBox(GridLayout):
   def build(self):
       layout = GridLayout(orientation='vertical' , padding=8 , spacing=8)
       # welcome to the top message of my app
       welcome = Label(
           text="Today weather forecast news in Rwanda",
           font_size=25,
           size_hint_y=(1, 3),
             color=(0, 0, 0, 1)
       )
       return layout

class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 2 #columns
        self.add_widget(Label(text="country: "))
        self.country_name = TextInput()
        self.add_widget(self.country_name)
        self.add_widget(Label(text="province: "))
        self.province_name = TextInput()
        self.add_widget(self.province_name)
        self.add_widget(Label(text="district: "))
        self.district_name = TextInput()
        self.add_widget(self.district_name)
        self.add_widget(Label(text="sector: "))
        self.sector_name = TextInput()
        self.add_widget(self.sector_name)
        self.add_widget(Label(text="cell: "))
        self.cell_name = TextInput()
        self.add_widget(self.cell_name)

class WeatherApp(App):
    def build(self):
        return MyGrid()
        return MyBox()
if __name__ == "__main__":
    WeatherApp().run()