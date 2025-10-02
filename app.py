# my weather app

import kivy
import os
import pandas as pd
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.uix.scrollview import ScrollView


# First Screen (User Inputs)
class FirstScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(orientation="vertical", padding=20, spacing=15)

        # Title
        title = Label(text="🌦️ Weather App", font_size=28, size_hint_y=None, height=50)
        layout.add_widget(title)

        grid = GridLayout(cols=1, padding=10, spacing=10, size_hint_y=None)
        grid.bind(minimum_height=grid.setter("height"))

        grid.add_widget(Label(text="Enter your location details:", font_size=20))

        # Helper to create input rows
        def add_input_row(label_text):
            row = BoxLayout(orientation="horizontal", size_hint_y=None, height=50)
            row.add_widget(Label(text=label_text, size_hint_x=0.3))
            text_input = TextInput(multiline=False, size_hint_x=0.7, background_color=(0.9, 0.9, 0.9, 1))
            row.add_widget(text_input)
            grid.add_widget(row)
            return text_input

        # Input fields
        self.country_name = add_input_row("Country:")
        self.province_name = add_input_row("Province:")
        self.district_name = add_input_row("District:")
        self.sector_name = add_input_row("Sector:")
        self.cell_name = add_input_row("Cell:")

        # Buttons row
        btn_row = BoxLayout(size_hint_y=None, height=60, spacing=15)

        submit_btn = Button(text="NEXT ▶", font_size=18, background_color=(0.2, 0.6, 1, 1))
        submit_btn.bind(on_press=self.go_next)

        exit_btn = Button(text="❌ Exit", font_size=18, background_color=(1, 0.3, 0.3, 1))
        exit_btn.bind(on_press=self.exit_app)

        btn_row.add_widget(submit_btn)
        btn_row.add_widget(exit_btn)

        grid.add_widget(btn_row)
        layout.add_widget(grid)
        self.add_widget(layout)

    def go_next(self, instance):
        self.manager.transition = SlideTransition(direction="left")
        self.manager.current = "second"

    def exit_app(self, instance):
        App.get_running_app().stop()


# Second Screen (Data Viewer)
class SecondScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(orientation="vertical", padding=10, spacing=10)

        title = Label(text="📊 Weather Data Preview", font_size=24, size_hint_y=None, height=50)
        layout.add_widget(title)

        folder = r"C:\Users\user\Documents\hackthon\rwa-nisr-sas-2018-stata"
        preview = "No data found."

        all_data = []
        if os.path.exists(folder):
            for file in os.listdir(folder):
                if file.endswith(".csv"):
                    path = os.path.join(folder, file)
                    df = pd.read_csv(path)
                    all_data.append(df)

            if all_data:
                df_combined = pd.concat(all_data, ignore_index=True)
                preview = df_combined.head(20).to_string()  # show first 20 rows

        scroll = ScrollView(size_hint=(1, 1))
        label = Label(text=preview, font_size=14, size_hint_y=None)
        label.bind(texture_size=label.setter("size"))
        scroll.add_widget(label)

        back_btn = Button(text="⬅ Go Back", size_hint_y=None, height=50, background_color=(0.3, 0.8, 0.3, 1))
        back_btn.bind(on_press=self.go_back)

        layout.add_widget(scroll)
        layout.add_widget(back_btn)
        self.add_widget(layout)

    def go_back(self, instance):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = "first"


# App Manager
class WeatherApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(FirstScreen(name="first"))
        sm.add_widget(SecondScreen(name="second"))
        return sm


if __name__ == "__main__":
    WeatherApp().run()
