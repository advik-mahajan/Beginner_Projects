UNIT CONVERTER
A terminal-based Python CLI tool to convert values across multiple physical quantities. Built as a part of self-study

FEATURES:

1) Convert between 6 units of physical quantities
   - Length (metres, kilometres, centimetres, miles, feet, inches)
   - Mass (grams, kilograms, tonne, milligrams, ounces, pounds)
   - Temperature (celcius, fahrenheit, kelvin)
   - Volume (litres, cubic metres, cubic centimetres, millilitres, fluid ounces)
   - Speed (m/s, kmph, mph)
   - Pressure (Pascal, atmosphere, torricelli, mmHg)
2) Runs continuously via outer loop until the user chooses to exit
3) Input validation on every user selection with re-input on providing invalid input
4) Results rounded upto 2 decimal places

HOW IT WORKS:

Each category converts through a base unit rather than hardcoding every pairwise combination
Length - metres
Mass - grams
Volume - litres
Speed - metres/second
Pressure - pascal

REQUIREMENTS - Python 3
