import kivy
import os
import csv
import pandas as pd
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.uix.scrollview import ScrollView


# ----------- First Screen (User Input) ------------
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
            text_input = TextInput(multiline=False, size_hint_x=0.7, background_color=(0.95, 0.95, 0.95, 1))
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


# second screen
class SecondScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # --- Main vertical layout ---
        main_layout = BoxLayout(orientation="vertical", padding=10, spacing=10)

        # --- Top navigation bar ---
        top_nav = BoxLayout(size_hint_y=0.12, spacing=5, padding=5)
        self.add_top_button(top_nav, "Home", self.go_home)
        self.add_top_button(top_nav, "Iteganyagihe", self.go_iteganyagihe)
        self.add_top_button(top_nav, "Ubuhinzi", self.go_ubuhinzi)
        main_layout.add_widget(top_nav)

        # --- Title ---
        title = Label(text="📊 Weather Data Preview", font_size=24, size_hint_y=None, height=50)
        main_layout.add_widget(title)

        # --- Scrollable area for CSV/data preview ---
        self.data_scroll = ScrollView(size_hint=(1, 1))
        self.data_label = Label(text="", font_size=14, size_hint_y=None, halign="left", valign="top")
        self.data_label.bind(texture_size=self.data_label.setter("size"))
        self.data_scroll.add_widget(self.data_label)
        main_layout.add_widget(self.data_scroll)

        # --- Bottom navigation bar with only Back button ---
        bottom_nav = BoxLayout(size_hint_y=0.12, spacing=5, padding=5)
        self.add_bottom_button(bottom_nav, "Back", self.go_back)
        main_layout.add_widget(bottom_nav)

        self.add_widget(main_layout)

        # --- Prepare sample CSV data ---
        self.prepare_sample_csv()

    # --- Helper functions for buttons ---
    def add_top_button(self, layout, text, callback):
        btn = Button(text=text, background_color=(0.5, 0.7, 1, 1))
        btn.bind(on_press=callback)
        layout.add_widget(btn)

    def add_bottom_button(self, layout, text, callback):
        btn = Button(text=text, background_color=(0.6, 0.4, 1, 1))
        btn.bind(on_press=callback)
        layout.add_widget(btn)

    # --- Sample CSV creation ---
    def prepare_sample_csv(self):
        data_to_write = [
            ["Country","Province","District","Sector","Cell","Year","Month","Day","Precipitation","Max Temp","Min Temp"],
            ["Rwanda","Kigali","Gasabo","Kacyiru","Gisozi",2018,1,1,0.0,28.0,15.0],
            ["Rwanda","Eastern","Rwamagana","Rubona","Mabare",2018,1,2,5.0,27.0,14.0],
            ["Rwanda","Southern","Huye","Tumba","Kigoma",2018,1,3,2.0,26.0,13.0],
            ["Rwanda","Western","Rusizi","Bugarama","Nyundo",2018,1,4,0.0,29.0,16.0],
            ["Rwanda","Northern","Musanze","Muhoza","Kigali",2018,1,5,3.0,25.0,12.0]
        ]
        with open("data.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(data_to_write)

    # --- Navigation callbacks ---
    def go_home(self, instance):
        print("Home clicked!")

    def go_iteganyagihe(self, instance):
        try:
            df = pd.read_csv("data.csv")
            preview = df.head(20).to_string(index=False)
            self.data_label.text = preview
        except Exception as e:
            self.data_label.text = f"Error loading data: {e}"

    def go_ubuhinzi(self, instance):
        print("Ubuhinzi clicked!")

    def go_back(self, instance):
        # Direct user to the first screen
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
