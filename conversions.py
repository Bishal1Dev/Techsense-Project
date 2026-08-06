# ==============================
# Conversion Engine
# ==============================


length = {
    "Meter": 1,
    "Kilometer": 1000,
    "Centimeter": 0.01,
    "Millimeter": 0.001,
    "Foot": 0.3048,
    "Inch": 0.0254,
    "Yard": 0.9144,
    "Mile": 1609.344
}


weight = {
    "Kilogram": 1,
    "Gram": 0.001,
    "Milligram": 0.000001,
    "Pound": 0.45359237,
    "Ounce": 0.0283495,
    "Ton": 1000
}


volume = {
    "Liter": 1,
    "Milliliter": 0.001,
    "Gallon": 3.78541,
    "Cup": 0.236588
}


storage = {
    "Byte": 1,
    "KB": 1024,
    "MB": 1024**2,
    "GB": 1024**3,
    "TB": 1024**4
}


time = {
    "Second": 1,
    "Minute": 60,
    "Hour": 3600,
    "Day": 86400
}


speed = {
    "m/s": 1,
    "km/h": 0.277778,
    "mph": 0.44704
}


currency = {
    "USD": 1,
    "NPR": 138,
    "EUR": 1.17,
    "GBP": 1.34
}


def normal_convert(table, from_unit, to_unit, value):
    base = value * table[from_unit]
    return round(base / table[to_unit], 6)


def temperature(from_unit, to_unit, value):

    if from_unit == to_unit:
        return value

    if from_unit == "Celsius":

        if to_unit == "Fahrenheit":
            return round(value * 9 / 5 + 32, 2)

        if to_unit == "Kelvin":
            return round(value + 273.15, 2)

    elif from_unit == "Fahrenheit":

        if to_unit == "Celsius":
            return round((value - 32) * 5 / 9, 2)

        if to_unit == "Kelvin":
            return round((value - 32) * 5 / 9 + 273.15, 2)

    elif from_unit == "Kelvin":

        if to_unit == "Celsius":
            return round(value - 273.15, 2)

        if to_unit == "Fahrenheit":
            return round((value - 273.15) * 9 / 5 + 32, 2)

    raise Exception("Temperature conversion not supported.")


def convert(category, from_unit, to_unit, value):

    if category == "Length":
        return normal_convert(length, from_unit, to_unit, value)

    elif category == "Weight":
        return normal_convert(weight, from_unit, to_unit, value)

    elif category == "Volume":
        return normal_convert(volume, from_unit, to_unit, value)

    elif category == "Storage":
        return normal_convert(storage, from_unit, to_unit, value)

    elif category == "Time":
        return normal_convert(time, from_unit, to_unit, value)

    elif category == "Speed":
        return normal_convert(speed, from_unit, to_unit, value)

    elif category == "Currency":
        return normal_convert(currency, from_unit, to_unit, value)

    elif category == "Temperature":
        return temperature(from_unit, to_unit, value)

    raise Exception("Invalid category.")