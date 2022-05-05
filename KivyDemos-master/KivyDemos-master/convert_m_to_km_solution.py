"""
CP1404 Week 11 Workshop - GUI program to convert miles to kilometres
Lindsay Ward, IT@JCU
06/10/2015
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_TO_KM = 1.60934


class ConvertMilesApp(App):
    """ConvertMilesApp is a kivy app that converts miles to km's."""
    message = StringProperty()

    def build(self):
        """Build Kivy app from kv file."""
        self.title = "Convert Miles to Kilometers"
        self.root = Builder.load_file("convert_miles_km.kv")
        return self.root

    def handle_conversion(self):
        """handle_conversion executes the conversion form miles to km's."""
        value = self.validate_input()
        result = float(value) * MILES_TO_KM
        self.root.ids.output_label.text = str(result)

    def validate_input(self):
        """Validates if the input was a number"""
        try:
            value = float(self.root.ids.input_number.text)
            return value
        except ValueError:
            return 0

    def handle_increment(self, increment):
        """Increments input up by 1."""
        value = self.validate_input() + increment
        self.root.ids.input_number.text = str(value)
        self.handle_conversion()


ConvertMilesApp().run()
