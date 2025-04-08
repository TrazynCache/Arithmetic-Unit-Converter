from ui import get_category, get_value, get_unit, display_result, ask_reverse
from converters.converter_factory import ConverterFactory

def main():
    category = get_category() # Gets category from the user (e.g. 'length' or 'temperature')
    converter = ConverterFactory.get_converter(category)
    units = converter.get_units() # Gets list of units supported by this converter

    # Collect user inputs: Value and units to convert between 
    value = get_value()
    from_unit = get_unit("Enter from_unit: ", units)
    to_unit = get_unit("Enter to_unit: ", units)

    # Perform the conversion and display the results
    result = converter.convert(value, from_unit, to_unit)
    display_result(value, from_unit, to_unit, result)

    if ask_reverse():
        reversed_result = converter.convert(result, to_unit, from_unit)
        display_result(result, to_unit, from_unit, reversed_result)

if __name__ == "__main__":
    main()