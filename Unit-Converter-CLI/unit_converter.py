while True:
    print("===== UNIT CONVERTER =====")
    print("Select a Physical Quantity to Convert: ")
    print("1. Length")
    print("2. Mass")
    print("3. Temperature")
    print("4. Volume")
    print("5. Speed")
    print("6. Pressure")
    print("7. Exit")
    print("NOTE - All conversions are rounded off to 2-digits")
    while True:
        choice = int(input("Enter the Number to Convert (1-7): "))
        if choice not in [1, 2, 3, 4, 5, 6, 7]:
            print("Enter a Valid Option (1-7)")
            continue
        else:
            break
    if choice == 7:
        print("Exiting Unit Converter. Bye!")
        break

    if choice == 1:
        print("1. Metres")
        print("2. Kilometres")
        print("3. Centimetres")
        print("4. Miles")
        print("5. Feet")
        print("6. Inches")
        while True:
            from_unit = int(input("Convert from (1-6): "))
            if from_unit in [1, 2, 3, 4, 5, 6]:
                break
            else:
                print("Enter a Number between 1 and 6")
                continue
        while True:
            to_unit = int(input("Convert to (1-6): "))
            if to_unit in [1, 2, 3, 4, 5, 6]:
                break
            else:
                print("Enter a Number between 1 and 6")
                continue
        while True:
            value = float(input("Enter the Value: "))
            if value > 0:
                break
            else:
                print("Enter a Value greater than 0")
                continue

        length_units = {1:1,
                    2:1000,
                    3:0.01,
                    4: 1609.34,
                    5:0.3048,
                    6:0.0254}
        val_in_metres = value * length_units[from_unit]
        result = val_in_metres / length_units[to_unit]

        print(f"Result: {result:.2f}")

    elif choice == 2:
        print("1. Grams(g)")
        print("2. Kilogram(kg)")
        print("3. Tonne")
        print("4. Milligram(mg)")
        print("5. Pounds(lbs)")
        print("6. Ounce(oz)")
        while True:
            from_unit = int(input("Convert from (1-6): "))
            if from_unit in [1, 2, 3, 4, 5, 6]:
                break
            else:
                print("Enter a Number between 1 and 6")
                continue
        while True:
            to_unit = int(input("Convert to (1-6): "))
            if to_unit in [1, 2, 3, 4, 5, 6]:
                break
            else:
                print("Enter a Number between 1 and 6")
                continue
        while True:
            value = float(input("Enter the Value: "))
            if value > 0:
                break
            else:
                print("Enter a Value greater than 0")
                continue

        mass_units = {1:1,
                  2:1000,
                  3:1000000,
                  4:0.001,
                  5:453.592,
                  6:28.3495}
        val_in_grams = value * mass_units[from_unit]
        result = val_in_grams / mass_units[to_unit]
        print(f"Result: {result:.2f}")

    elif choice == 3:
        print("1. Celcius")
        print("2. Fahrenheit")
        print("3. Kelvin")
        while True:
            from_unit = int(input("Convert from (1-3): "))
            if from_unit in [1, 2, 3]:
                break
            else:
                print("Enter a Number between 1 and 3")
                continue
        while True:
            to_unit = int(input("Convert to (1-3): "))
            if to_unit in [1, 2, 3]:
                break
            else:
                print("Enter a Number between 1 and 3")
                continue
        while True:
            value = float(input("Enter the Value: "))
            if value >= -273.15:
                break
            else:
                print("Enter a Value >= -273.15 (absolute zero in Celsius)")
                continue

        def to_celcius(value, unit):
            if unit == 1:
                return value
            elif unit == 2:
                return (value - 32) * 5/9
            elif unit == 3:
                return value - 273.15
        def from_celcius(value, unit):
            if unit == 1:
                return value
            elif unit == 2:
                return (value*9/5) + 32
            elif unit == 3:
                return value + 273.15
        celcius_val = to_celcius(value, from_unit)
        result = from_celcius(celcius_val, to_unit)
        print(f"Result: {result:.2f}")

    elif choice == 4:
        print("1. Litre(L)")
        print("2. Millilitre(mL)")
        print("3. Cubic Metre")
        print("4. Cubic Centimetre")
        print("5. Fluid Ounce")
        while True:
            from_unit = int(input("Convert from (1-5): "))
            if from_unit in [1, 2, 3, 4, 5]:
                break
            else:
                print("Invalid Input. Enter a Number between 1 and 5")
                continue
        while True:
            to_unit = int(input("Convert to (1-5): "))
            if to_unit in [1, 2, 3, 4, 5]:
                break
            else:
                print("Invalid Input. Enter a Number between 1 and 5")
                continue
        while True:
            value = float(input("Enter the Value: "))
            if value > 0:
                break
            else:
                print("Enter a Value greater than 0")
                continue

        volume_units = {1:1,
                        2:0.001,
                        3:1000,
                        4:0.001,
                        5:0.0295735}
        val_in_litres = value * volume_units[from_unit]
        result = val_in_litres / volume_units[to_unit]
        print(f"Result: {result:.2f}")

    elif choice == 5:
        print("1. Miles per hour (mph)")
        print("2. Metres per second (m/s)")
        print("3. Kilometres per hour (kmph)")
        while True:
            from_unit = int(input("Convert from (1-3): "))
            to_unit = int(input("Convert to (1-3): "))
            value = float(input("Enter the Value: "))
            if from_unit in [1, 2, 3] and to_unit in [1, 2, 3] and value > 0:
                break
            else:
                print("Enter a Number between 1 and 3, and a Value greater than 0")
                continue

        speed_units = {1: 0.44704,
                       2: 1,
                       3: 0.277778}
        val_in_mps = value * speed_units[from_unit]
        result = val_in_mps / speed_units[to_unit]
        print(f"Result: {result:.2f}")

    elif choice == 6:
        print("1. Pascal (Pa)")
        print("2. Atmosphere (atm)")
        print("3. Torr")
        print("4. mmHg")
        while True:
            from_unit = int(input("Convert from (1-4): "))
            to_unit = int(input("Convert to (1-4): "))
            value = float(input("Enter the Value: "))
            if from_unit in [1, 2, 3, 4] and to_unit in [1, 2, 3, 4] and value > 0:
                break
            else:
                print("Enter a Number between 1 and 4, and a Value greater than 0")
                continue

        pressure_units = {1: 1,
                           2: 101325,
                           3: 133.322,
                           4: 133.322}
        val_in_pascal = value * pressure_units[from_unit]
        result = val_in_pascal / pressure_units[to_unit]
        print(f"Result: {result:.2f}")

    print()
