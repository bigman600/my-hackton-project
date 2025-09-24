# my weather app
import kivy 
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

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


        #to run my app
class WeatherApp(App):
    def build(self):
        return MyGrid()
if __name__ == "__main__":
    WeatherApp().run()