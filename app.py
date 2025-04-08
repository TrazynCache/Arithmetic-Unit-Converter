from flask import Flask, render_template, request
from converters.converter_factory import ConverterFactory

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    # Initialize variables for the template
    categories = ['length', 'temperature']
    units = {}
    result = None
    reverse_result = None
    error = None
    warning = None  # New variable for same-unit warning

    if request.method == 'POST':
        # Get form data
        category = request.form.get('category')
        value_str = request.form.get('value', '')
        from_unit = request.form.get('from_unit')
        to_unit = request.form.get('to_unit')

        # Ensure category is selected
        if not category:
            error = "Please select a category."
        else:
            # Instantiate the converter and populate units
            converter = ConverterFactory.get_converter(category)
            units = {category: converter.get_units()}

            # Check if from_unit and to_unit are the same
            if from_unit and to_unit and from_unit == to_unit:
                warning = "Warning: 'From' and 'To' units are the same. Please select different units."

            # Validate inputs
            if not value_str:
                error = "Please enter a value to convert."
            elif from_unit not in units[category]:
                error = f"Invalid 'from' unit: {from_unit}"
            elif to_unit not in units[category]:
                error = f"Invalid 'to' unit: {to_unit}"
            else:
                try:
                    value = float(value_str)
                    # Perform conversion only if units are different
                    if not warning:  # Only convert if from_unit != to_unit
                        result = converter.convert(value, from_unit, to_unit)

                        # Handle reverse conversion if requested
                        if 'reverse' in request.form:
                            reverse_result = converter.convert(result, to_unit, from_unit)
                    # Clear error if all inputs are valid
                    error = None
                except ValueError:
                    error = "Please enter a valid number."

    return render_template('index.html',
                           categories=categories,
                           units=units,
                           result=result,
                           reverse_result=reverse_result,
                           error=error,
                           warning=warning)  # Pass warning to template

if __name__ == "__main__":
    app.run(debug=True)