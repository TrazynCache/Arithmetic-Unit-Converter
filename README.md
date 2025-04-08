# Arithmetic Unit Converter

A modular, Python-based tool for converting units like length and temperature with ease. Built for flexibility and real-world utility—great for global operations, freelancers, or quick conversions.

## Features
- **Supported Conversions**: Length (meters, feet, inches) and temperature (Celsius, Fahrenheit).  
- **Reverse Conversion**: Flip conversions instantly (e.g., meters to feet, then back).  
- **Extensible Design**: Add new unit types with the Factory Pattern.

## How to Run
1. Clone the repo.  
2. Ensure Python 3.x is installed.  
3. Navigate to the project folder.  
4. Run `python main.py`.  
5. Follow the prompts (e.g., "length", "10", "meter", "foot").

## Structure
- `main.py`: Entry point coordinating UI and logic.  
- `ui.py`: User interaction module.  
- `converters/`: Conversion logic package.  
  - `converter_factory.py`: Creates converters using the Factory Pattern.  
  - `length_converter.py`: Handles length units.  
  - `temperature_converter.py`: Manages temperature units.  
- `data/length_units.json`: Length conversion factors.

## Why It’s Cool
- **Modular**: Each piece (UI, converters) is reusable elsewhere.  
- **Scalable**: Add new categories (e.g., currency) easily.  
- **Practical**: Supports real-world needs like international measurements.

## Requirements
- Python 3.x

## Try It Out
Convert 10 meters to feet, then reverse it—see how simple it is!