
# my weather app

import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.scrollview import ScrollView
from kivy.utils import platform
import pandas as pd


# First Screen
class FirstScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(orientation="vertical", padding=10, spacing=10)

        grid = GridLayout(cols=1, padding=10, spacing=10, size_hint_y=None)
        grid.bind(minimum_height=grid.setter("height"))

        grid.add_widget(Label(text="Enter your location details:", font_size=24))

        # Helper to create input rows
        def add_input_row(label_text):
            row = BoxLayout(orientation="horizontal", size_hint_y=None, height=50)
            row.add_widget(Label(text=label_text, size_hint_x=0.3))
            text_input = TextInput(multiline=False, size_hint_x=0.7)
            row.add_widget(text_input)
            grid.add_widget(row)
            return text_input

        # Input fields
        self.country_name = add_input_row("Country:")
        self.province_name = add_input_row("Province:")
        self.district_name = add_input_row("District:")
        self.sector_name = add_input_row("Sector:")
        self.cell_name = add_input_row("Cell:")

        # Next Button
        submit_btn = Button(text="NEXT", font_size=20, size_hint_y=None, height=60)
        submit_btn.bind(on_press=self.go_next)
        grid.add_widget(submit_btn)

        # Exit Button
        exit_btn = Button(text="Exit", font_size=20, size_hint_y=None, height=60)
        exit_btn.bind(on_press=self.exit_app)
        grid.add_widget(exit_btn)

        # Minimize Button
        minimize_btn = Button(text="Minimize", font_size=20, size_hint_y=None, height=60)
        minimize_btn.bind(on_press=self.minimize_app)
        grid.add_widget(minimize_btn)

        layout.add_widget(grid)
        self.add_widget(layout)

    def go_next(self, instance):
        self.manager.current = "second"

    def exit_app(self, instance):
        App.get_running_app().stop()

    def minimize_app(self, instance):
        if platform == "android":
            from jnius import autoclass
            PythonActivity = autoclass("org.kivy.android.PythonActivity")
            Intent = autoclass("android.content.Intent")
            activity = PythonActivity.mActivity
            activity.moveTaskToBack(True)

            intent = Intent(activity, activity.getClass())
            intent.addCategory(Intent.CATEGORY_HOME)
            intent.setFlags(Intent.FLAG_ACTIVITY_NEW_TASK)
            activity.startActivity(intent)
        else:
            print("Minimize works only on Android.")


# Second Screen
class SecondScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(orientation="vertical")

        try:
            # Load datasets (replace paths with valid files on your system)
            data = pd.read_spss(r"D:\note\BIT\hackton\Microdata_SAS2021\SPSS\rwa-sas-seasonA_Crop production.sav")
            preview = data.head(20).to_string(index=False)
        except Exception as e:
            preview = f"Error loading dataset: {e}"

        scroll = ScrollView(size_hint=(1, 1))
        label = Label(text=preview, font_size=14, size_hint_y=None)
        label.bind(texture_size=label.setter("size"))
        scroll.add_widget(label)

        # Back Button
        back_btn = Button(text="Go Back", size_hint_y=None, height=50)
        back_btn.bind(on_press=self.go_back)

        layout.add_widget(scroll)
        layout.add_widget(back_btn)
        self.add_widget(layout)

    def go_back(self, instance):
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
