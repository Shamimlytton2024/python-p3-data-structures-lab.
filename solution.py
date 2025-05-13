def convert_to_celsius(temperature):
    """
    Convert Fahrenheit to Celsius using the formula:
    celsius = (temperature - 32) * 5/9
    """
    celsius = (temperature - 32) * 5 / 9
    return celsius

def weather_info(temp):
    """
    Convert the given temperature from Fahrenheit to Celsius and return a string
    indicating if it is freezing or above freezing temperature.
    """
    c = convert_to_celsius(temp)
    if c <= 0:
        return f"{c:.1f} is freezing temperature"
    else:
        return f"{c:.1f} is above freezing temperature"
