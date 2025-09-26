# weather forecast for Rwanda
import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout   
from kivy.uix.button import Button
from plyer import notification
from kivy.clock import Clock


class weather(App):
    def build(self):
        layout = BoxLayout(orientation="vertical", padding=10, spacing=10)
        layout = BoxLayout()
        Clock.schedule_interval(self.auto_reminder, 30)  # every 30 sec (test)
        return layout
    def auto_reminder(self, dt):
        self.show_notification(imvura)
        layout = BoxLayout(orientation="vertical", padding=10, spacing=10)
        

        # button to trigger notification
        btn = Button(text="Iteganyagihe", size_hint=(1, 0.2), font_size=24)
        btn.bind(on_press=self.show_notification)       
        layout.add_widget(btn)
        return layout
    def show_notification(self, instance):
        notification.notify(
            title="Weather Update",
            message="uyu munsi hateganyijwe imvura muturere twose two mu gihugu!",
            app_name="WeatherApp",
            timeout=5
        )      

if __name__ == "__main__":
    weather().run() 

