# Converts between temperature units using Kelvin as the base.

class TemperatureConverter:
    def __init__(self):
        self.conversions = {
            'celsius': {
                'to_kelvin': lambda c: c + 273.15, # C to K: add offset
                'from_kelvin': lambda k: k - 273.15 # K to C: subtract offset
            },
            'fahrenheit': {
                'to_kelvin': lambda f: (f - 32) * 5/9 + 273.15, # C to K: add offset
                'from_kelvin': lambda k: (k - 273.15) * 9/5 + 32 # K to C: subtract offset
            }
        }

    def convert(self, value, from_unit, to_unit):
        """Convert a value from one temperature unit to another."""
        if from_unit not in self.conversions or to_unit not in self.conversions:
            raise ValueError("Invalid unit")

        kelvin = self.conversions[from_unit]['to_kelvin'](value)
        result = self.conversions[to_unit]['from_kelvin'](kelvin)
        return result

    def get_units(self):
        """Return the list of supported temperature units."""
        return list(self.conversions.keys())