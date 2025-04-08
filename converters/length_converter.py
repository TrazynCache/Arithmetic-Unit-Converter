#Converts between length units using meters as the base unit.

import json

class LengthConverter:
    def __init__(self):
        # Not for production
        with open('data/length_units.json', 'r') as f:
            self.factors = json.load(f)

    def convert(self, value, from_unit, to_unit):
        """Convert a value from one length unit to another."""
        if from_unit not in self.factors or to_unit not in self.factors:
            raise ValueError("Invalid unit")
        
        factor_from = self.factors[from_unit]
        factor_to = self.factors[to_unit]
        result = (value * factor_from) / factor_to
        return result

    def get_units(self):
        """Return the list of supported length units."""
        return list(self.factors.keys())