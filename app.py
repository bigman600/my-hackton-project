# my weather app
import kivy 
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.utils import platform



#first screen

class Firstscreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        main_layout = BoxLayout(orientation="vertical", padding=10, spacing=10)

        # to add grid in put fields
        grid = GridLayout(cols=1, padding=10, spacing=10)
        grid.bind(minimum_height=grid.setter('height'))

        # add input fields
        grid.add_widget(Label(text="Enter your location details:", font_size=24))

        # input fields for location details
        row = BoxLayout(orientation='horizontal', size_hint_y=None, height=60)
        row.add_widget(Label(text="country: ", size_hint_x=0.3, halign='right', valign='middle'))
        self.country_name = TextInput(multiline=False, halign='left', size_hint_x=0.7, height=60)
        row.add_widget(self.country_name)
        grid.add_widget(row)

        row = BoxLayout(orientation='horizontal', size_hint_y=None, height=60)
        row.add_widget(Label(text="province: ", size_hint_x=0.3, halign='right', valign='middle'))
        self.province_name = TextInput(multiline=False, halign='left', size_hint_x=0.7, height=60)
        row.add_widget(self.province_name)
        grid.add_widget(row)

        row = BoxLayout(orientation='horizontal', size_hint_y=None, height=60)
        row.add_widget(Label(text="district: ", size_hint_x=0.3, halign='right', valign='middle'))
        self.district_name = TextInput(multiline=False, halign='left', size_hint_x=0.7, height=60)
        row.add_widget(self.district_name)
        grid.add_widget(row)

        row = BoxLayout(orientation='horizontal', size_hint_y=None, height=60)
        row.add_widget(Label(text="sector: ", size_hint_x=0.3, halign='right', valign='middle'))
        self.sector_name = TextInput(multiline=False, halign='left', size_hint_x=0.7, height=60)
        row.add_widget(self.sector_name)
        grid.add_widget(row)

        row = BoxLayout(orientation='horizontal', size_hint_y=None, height=60)
        row.add_widget(Label(text="cell: ", size_hint_x=0.3, halign='right', valign='middle'))
        self.cell_name = TextInput(multiline=False,halign='left', size_hint_x=0.7, height=60)
        row.add_widget(self.cell_name)
        grid.add_widget(row)

        # button to the next screen
        self.submit = Button(text="NEXT", font_size=32)
        self.submit.bind(on_press=self.pressed)
        grid.add_widget(self.submit)
        self.add_widget(grid)

    def pressed(self, instance): 
        """go to the next screen"""
        self.manager.current = "second"
      
              
        # button to close app
        exit_btn = Button(text="Exit", font_size=24)
        exit_btn.bind(on_press=self.exit_app)
        self.add_widget(exit_btn)
    def exit_app(self, instance):
        """close app completely"""
        App.get_running_app().stop()

        minimize_btn = Button(text="Minimize", font_size=24)
        minimize_btn.bind(on_press=self.minimize_app)
        self.add_widget(minimize_btn)
    def minimize_app(self, instance):
        if platform == 'android':
            from jnius import autoclass
            PythonActivity = autoclass('org.kivy.android.PythonActivity')
            intent = autoclass('android.content.Intent')
            activity = PythonActivity.mActivity
            activity.moveTaskToBack(True)
            # to minimize app on other platforms, you can implement similar functionality
            intent = intent.Intent(activity, activity.getClass())
            intent.addCategory(intent.CATEGORY_HOME)
            intent.setFlags(intent.FLAG_ACTIVITY_NEW_TASK)
            activity.startActivity(intent)
        else:
            print("Minimize functionality is only implemented for Android platform.")

# second screen
class Secondscreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 1
        self.add_widget(Label(text="This is the second screen"))
        back_btn = Button(text="Back", font_size=32)
        back_btn.bind(on_press=self.go_back)
        self.add_widget(back_btn)

    def go_back(self, instance):
        """go back to the first screen"""
        self.manager.current = "first"



#to run my app
class WeatherApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(Firstscreen(name="first"))
        sm.add_widget(Secondscreen(name="second"))
        return sm

if __name__ == "__main__":
    WeatherApp().run()



