# Arithmetic Unit Converter

A sleek, web-based tool for converting units like length and temperature, built with Flask and Python. Designed for global operations, freelancers, or anyone needing quick, reliable conversions with a modern, user-friendly interface.

## Features
- **Supported Conversions**: Length (meters, feet, inches) and temperature (Celsius, Fahrenheit).  
- **Reverse Conversion**: Flip conversions instantly (e.g., meters to feet, then back).  
- **Smart Validation**: Automatically clears error messages once valid input is provided.  
- **Same-Unit Warning**: Alerts users if they select the same unit for conversion (e.g., Celsius to Celsius).  
- **Modern Design**: Gradient background, glassmorphism container, and responsive layout.  
- **Extensible**: Add new unit types easily with the Factory Pattern.

## How to Run
1. Clone the repo.  
2. Ensure Python 3.x is installed.  
3. Install dependencies: `pip install flask`.  
4. Navigate to the project folder.  
5. Run `python app.py`.  
6. Open `http://127.0.0.1:5000` in your browser.

## Structure
- `app.py`: Flask app entry point.  
- `converters/`: Conversion logic package.  
  - `converter_factory.py`: Creates converters using the Factory Pattern.  
  - `length_converter.py`: Handles length units.  
  - `temperature_converter.py`: Manages temperature units.  
- `data/length_units.json`: Length conversion factors.  
- `static/style.css`: Styling for the web interface.  
- `templates/index.html`: Web interface template.

## Why It’s Cool
- **Modular**: Each component (UI, converters) is reusable in other projects.  
- **Scalable**: Add new categories (e.g., currency) by extending the factory.  
- **Practical**: Supports real-world needs like international measurements.  
- **User-Friendly**: Intuitive interface with instant feedback and warnings.

## Requirements
- Python 3.x  
- Flask (`pip install flask`)

## Try It Out
Convert 32°F to Celsius, then reverse it—experience the seamless design and smart features!

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.