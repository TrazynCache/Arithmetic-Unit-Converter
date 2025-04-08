from re import I
from .length_converter import LengthConverter
from .temperature_converter import TemperatureConverter

class ConverterFactory:
    @staticmethod
    def get_converter(category):
        """Return a converter object based on category."""
        #Match the category to the right converter class
        if category == 'length':
            return LengthConverter()
        elif category == 'temperature':
            return TemperatureConverter()
        else:
            raise ValueError("Invalid category")