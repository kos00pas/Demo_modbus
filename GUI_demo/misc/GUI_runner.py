import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from matplotlib import gridspec
import threading

import csv
import os
import random
import time

class Database:
    def __init__(self, main_window, filename='data_log.csv'):
        self.data = []
        self.main_window = main_window
        self.filename = filename
        self.fields = ['id', 'date', 'timestamp', 'lat', 'lng', 'temperature', 'pressure', 'altitude', 'humidity', 'rssi', 'snr']
        self.initialize_csv()

    def initialize_csv(self):
        # Check if file exists to avoid overwriting existing data
        if not os.path.exists(self.filename):
            with open(self.filename, 'w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=self.fields)
                writer.writeheader()

    def append_data(self, id=None, date=None, timestamp=None, lat=None, lng=None, temperature=None, pressure=None, altitude=None, humidity=None, rssi=None, snr=None):
        # Create a new data instance as a dictionary
        new_data_instance = {
            'id': id,
            'date': date,
            'timestamp': timestamp,
            'lat': lat,
            'lng': lng,
            'temperature': temperature,
            'pressure': pressure,
            'altitude': altitude,
            'humidity': humidity,
            'rssi': rssi,
            'snr': snr
        }
        print(f'append {new_data_instance["id"]}')
        self.data.append(new_data_instance)
        self.append_to_csv(new_data_instance)

    def append_to_csv(self, data_instance):
        with open(self.filename, 'a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=self.fields)
            writer.writerow(data_instance)
class MainWindow(tk.Tk):
    def __init__(self, gui_manager,database):
        super().__init__()
        self.gui_manager = gui_manager
        self.database=database
        self.title('the_window')
        self.state('zoomed')
        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.set_the_window()
        threading.Thread(target=self.get_now_data).start()

    def on_closing(self):
        self.destroy()
        #sys.exit() to clodse the program
    def set_the_window(self):
        # Create a frame to contain the button
        self.button_frame = tk.Frame(self)
        self.button_frame.pack(side=tk.TOP, pady=10)  # Place the frame at the top with some padding

        self.fig = plt.figure(figsize=(10, 8))
        gs = gridspec.GridSpec(4, 2, height_ratios=[1, 1, 1, 1])

        # Create subplots
        self.ax00 = self.fig.add_subplot(gs[0, 0])  # 3D plot
        self.ax01 = self.fig.add_subplot(gs[0, 1])  # Polar plot
        self.ax10 = self.fig.add_subplot(gs[1, 0])  # Second row, first column
        self.ax11 = self.fig.add_subplot(gs[1, 1])  # Second row, second column
        self.ax20 = self.fig.add_subplot(gs[2, 0])  # Third row, first column
        self.ax21 = self.fig.add_subplot(gs[2, 1])  # Third row, second column
        self.ax30 = self.fig.add_subplot(gs[3, 0])  # Fourth row, first column
        self.ax31 = self.fig.add_subplot(gs[3, 1])  # Fourth row, second column

        self.canvas = FigureCanvasTkAgg(self.fig, master=self.master)  # Create a canvas widget
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
    def refresh_window(self):
        # Ensure there are at least five data points
        if len(self.database.data) < 5:
            print("Not enough data to refresh plots.")
            return

        # Extract the last five entries
        last_five_data = self.database.data[-5:]

        # Clear existing data on the plots
        self.ax00.clear()  # Clear for timestamps over indices
        self.ax01.clear()  # Clear for timestamps over indices
        self.ax10.clear()  # Clear for lat over indices
        self.ax11.clear()  # Clear for lng over indices
        self.ax20.clear()  # Clear for temperatures over indices
        self.ax21.clear()  # Clear for pressures over indices
        self.ax30.clear()  # Clear for altitudes over indices
        self.ax31.clear()  # Clear for humidities over indices

        # Indices for x-axis (0, 1, 2, 3, 4)
        indices = list(range(5))

        # Get data for plotting
        lat = [float(data['lat']) for data in last_five_data]
        lng = [float(data['lng']) for data in last_five_data]
        temperatures = [float(data['temperature']) for data in last_five_data]
        pressures = [float(data['pressure']) for data in last_five_data]
        altitudes = [float(data['altitude']) for data in last_five_data]
        humidities = [float(data['humidity']) for data in last_five_data]

        # Plot new data over indices
        self.ax00.plot(indices, indices, 'ro-')  # Plot example index
        self.ax01.plot(indices, indices, 'ro-')  # Plot example index

        self.ax10.plot(indices, lat, 'bo-')  # Plot latitude over indices
        self.ax11.plot(indices, lng, 'bo-')  # Plot longitude over indices

        self.ax20.plot(indices, temperatures, 'go-')  # Plot temperatures over indices
        self.ax21.plot(indices, pressures, 'mo-')  # Plot pressures over indices

        self.ax30.plot(indices, altitudes, 'co-')  # Plot altitudes over indices
        self.ax31.plot(indices, humidities, 'yo-')  # Plot humidities over indices

        # Set plot titles and labels
        self.ax00.set_xlabel('Index')
        self.ax01.set_xlabel('Index')
        self.ax10.set_xlabel('Index')
        self.ax11.set_xlabel('Index')
        self.ax20.set_xlabel('Index')
        self.ax21.set_xlabel('Index')
        self.ax30.set_xlabel('Index')
        self.ax31.set_xlabel('Index')

        self.ax00.set_ylabel('Example Data')
        self.ax01.set_ylabel('Example Data')
        self.ax10.set_ylabel('Latitude')
        self.ax11.set_ylabel('Longitude')
        self.ax20.set_ylabel('Temperature')
        self.ax21.set_ylabel('Pressure')
        self.ax30.set_ylabel('Altitude')
        self.ax31.set_ylabel('Humidity')

        # Redraw the canvas
        self.canvas.draw()

    def get_now_data(self):
        """code to simulate new data reception with random values"""
        while True:
            # Simulate a delay as if reading from a serial port
            time.sleep(1)  # Adjust the sleep time as needed for your testing

            # Generate random data
            ids = str(random.randint(100, 999))
            date = time.strftime('%Y-%m-%d')
            timestamp = time.strftime('%H:%M:%S')
            lat = random.uniform(-90, 90)
            lng = random.uniform(-180, 180)
            temperature = random.uniform(-20, 40)  # Temperature range
            pressure = random.uniform(980, 1050)  # Pressure in hPa
            altitude = random.uniform(0, 4000)  # Altitude in meters
            humidity = random.randint(0, 100)  # Humidity percentage

            # Log the simulated data (optional, for debug purposes)
            print(f"Simulated Data: id={ids}, date={date}, timestamp={timestamp}, lat={lat:.2f}, lng={lng:.2f}, temperature={temperature:.2f}, pressure={pressure:.2f}, altitude={altitude:.2f}, humidity={humidity}")

            # Append the data to the database and refresh the window
            self.database.append_data(id=ids, date=date, timestamp=timestamp, lat=lat, lng=lng, temperature=temperature, pressure=pressure, altitude=altitude, humidity=humidity)

            # Start a new thread to refresh the window
            threading.Thread(target=self.refresh_window).start()


class GUIManager:
     def __init__(self):
         self.database=Database(self)
         self.main_window=MainWindow(self,self.database)

         self.main_window.mainloop()

the_gui_manager = GUIManager()