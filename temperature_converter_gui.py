import tkinter as tk
from tkinter import ttk

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    celsius = fahrenheit_to_celsius(fahrenheit)
    return celsius_to_kelvin(celsius)

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    celsius = kelvin_to_celsius(kelvin)
    return celsius_to_fahrenheit(celsius)

class TemperatureConverterApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Temperature Converter")

        ttk.Label(self.master, text="WELCOME", font=('Arial', 18, 'bold')).grid(row=0, column=0, columnspan=2, pady=10)
        ttk.Label(self.master, text="TEMPERATURE CONVERTER USING PYTHON AND TKINTER", font=('Arial', 14)).grid(row=1, column=0, columnspan=2, pady=10)

        self.choice_var = tk.StringVar()

        ttk.Label(self.master, text="Choose conversion:").grid(row=2, column=0, columnspan=2, pady=10)

        choices = ["Celsius to Fahrenheit", "Celsius to Kelvin", "Fahrenheit to Celsius", "Fahrenheit to Kelvin", "Kelvin to Celsius", "Kelvin to Fahrenheit"]
        self.choice_menu = ttk.Combobox(self.master, textvariable=self.choice_var, values=choices, state="readonly")
        self.choice_menu.grid(row=3, column=0, columnspan=2, pady=10)
        self.choice_menu.set(choices[0])

        ttk.Label(self.master, text="Enter temperature:").grid(row=4, column=0, columnspan=2)

        self.temperature_entry = ttk.Entry(self.master)
        self.temperature_entry.grid(row=5, column=0, columnspan=2, pady=10)

        ttk.Button(self.master, text="Convert", command=self.convert_temperature).grid(row=6, column=0, columnspan=2, pady=10)

        self.result_label = ttk.Label(self.master, text="")
        self.result_label.grid(row=7, column=0, columnspan=2, pady=10)

    def convert_temperature(self):
        conversion_type = self.choice_var.get()
        temperature_str = self.temperature_entry.get()

        try:
            temperature = float(temperature_str)
        except ValueError:
            self.result_label.config(text="Invalid input. Please enter a numeric value.")
            return

        if conversion_type == "Celsius to Fahrenheit":
            result = round(celsius_to_fahrenheit(temperature), 2)
            result_text = f"{temperature}°C is equal to {result}°F"
        elif conversion_type == "Celsius to Kelvin":
            result = round(celsius_to_kelvin(temperature), 2)
            result_text = f"{temperature}°C is equal to {result} K"
        elif conversion_type == "Fahrenheit to Celsius":
            result = round(fahrenheit_to_celsius(temperature), 2)
            result_text = f"{temperature}°F is equal to {result}°C"
        elif conversion_type == "Fahrenheit to Kelvin":
            result = round(fahrenheit_to_kelvin(temperature), 2)
            result_text = f"{temperature}°F is equal to {result} K"
        elif conversion_type == "Kelvin to Celsius":
            result = round(kelvin_to_celsius(temperature), 2)
            result_text = f"{temperature} K is equal to {result}°C"
        elif conversion_type == "Kelvin to Fahrenheit":
            result = round(kelvin_to_fahrenheit(temperature), 2)
            result_text = f"{temperature} K is equal to {result}°F"
        else:
            result_text = "Invalid conversion type."

        self.result_label.config(text=result_text)


def main():
    root = tk.Tk()
    app = TemperatureConverterApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
