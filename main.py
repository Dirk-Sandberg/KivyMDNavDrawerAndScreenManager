from kivy.app import App
from kivymd.theming import ThemeManager


class MainApp(App):
    theme_cls = ThemeManager()


MainApp().run()
