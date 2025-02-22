import tkinter as tk
from tkinter import ttk
import serial
import time

# Connect to the Arduino
arduino = serial.Serial('COM5', 9600)  # Replace 'COM3' with your Arduino's port

def turn_on_pump():
    arduino.write(b'1')

def turn_off_pump():
    arduino.write(b'0')

def set_auto_mode():
    arduino.write(b'2')

def quit_program():
    arduino.close()
    root.destroy()

def refresh():
    # You can add code here to refresh the GUI or read data from the Arduino
    pass

root = tk.Tk()
root.title("Automated Water Pump")

main_frame = ttk.Frame(root, padding="20")
main_frame.grid(row=0, column=0, sticky="nsew")

pump_button = ttk.Button(main_frame, text="Turn On Pump", command=turn_on_pump)
pump_button.grid(row=0, column=0, padx=10, pady=10)

off_button = ttk.Button(main_frame, text="Turn Off Pump", command=turn_off_pump)
off_button.grid(row=0, column=1, padx=10, pady=10)

auto_mode_button = ttk.Button(main_frame, text="Set Auto Mode", command=set_auto_mode)
auto_mode_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

quit_button = ttk.Button(main_frame, text="Quit", command=quit_program)
quit_button.grid(row=2, column=0, padx=10, pady=10)

refresh_button = ttk.Button(main_frame, text="Refresh", command=refresh)
refresh_button.grid(row=2, column=1, padx=10, pady=10)

root.mainloop()

