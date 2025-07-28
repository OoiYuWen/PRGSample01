def celsius_to_farenheit(c):
    f = (c*9/5) + 32
    return f 
degree_celsius = float(input("Enter the temperature in degree Celsius: "))
fahrenheit = celsius_to_farenheit(degree_celsius)
print(f"The temperature is equivalent to {fahrenheit} Farenheit.")