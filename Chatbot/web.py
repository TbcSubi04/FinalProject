import tkinter as tk
from tkinter import messagebox
import sys
import matplotlib.pyplot as plt

def f1_drivers():
    try:
        with open("lap_times_1.txt", 'r') as file:
            location = file.readline()
            messagebox.showinfo("Lap 1 Location", f"The first location of the lap is: {location}")
    except ValueError:
        messagebox.showerror("Error", "The file could not be traced.")

def info_lap1():
    lap_times = []
    try:
        with open("lap_times_1.txt", 'r') as file:
            lines = file.readlines()
        for line in lines[1:]:
            driver = line[:3]
            lap_time = float(line[3:])
            lap_times.append((driver, lap_time))

        if lap_times:
            shortest_lap = min(lap_times, key= lambda x:x[1])
            longest_lap = max(lap_times, key=lambda x:x[1])

            messagebox.showinfo("Lap 1 Analysis",
                                f"Shortest lap: {shortest_lap[1]:.3f} by {shortest_lap[0]}\n"
                                f"Longest lap: {longest_lap[1]:.3f} by {longest_lap[0]}")
        else:
            messagebox.showinfo("Lap 1 Analysis", "No lap times available.")
    except FileNotFoundError:
        messagebox.showerror("Error", "The file lap_times_1.txt could not be found.")

def info_lap2():
    lap_times = []
    try:
        with open("lap_times_2.txt", 'r') as file:
            lines = file.readlines()
        for line in lines[1:]:
            driver = line[:3]
            lap_time = float(line[3:])
            lap_times.append((driver, lap_time))

        if lap_times:
            shortest_lap = min(lap_times, key=lambda x: x[1])
            longest_lap = max(lap_times, key=lambda x: x[1])
            

            messagebox.showinfo("Lap 2 Analysis",
                                f"Shortest lap: {shortest_lap[1]:.3f} by {shortest_lap[0]}\n"
                                f"Longest lap: {longest_lap[1]:.3f} by {longest_lap[0]}\n")
        else:
            messagebox.showinfo("Lap 2 Analysis", "No lap times available.")
    except FileNotFoundError:
        messagebox.showerror("Error", "The file lap_times_2.txt could not be found.")

def info_lap3():
    lap_times = []
    try:
        with open("lap_times_3.txt", 'r') as file:
            location = file.readline().strip()
            lines = file.readlines()

        for line in lines:
            driver = line[:3]
            lap_time = float(line[3:])
            lap_times.append((driver, lap_time))

        if lap_times:
            shortest_lap = min(lap_times, key=lambda x: x[1])
            longest_lap = max(lap_times, key=lambda x: x[1])
            

            messagebox.showinfo("Lap 3 Analysis",
                                f"Location: {location}\n"
                                f"Shortest lap: {shortest_lap[1]:.3f} by {shortest_lap[0]}\n"
                                f"Longest lap: {longest_lap[1]:.3f} by {longest_lap[0]}\n")
                               
        else:
            messagebox.showinfo("Lap 3 Analysis", "No lap times available.")
    except FileNotFoundError:
        messagebox.showerror("Error", "The file lap_times_3.txt could not be found.")

def indi_drivers_info():
    try:
        with open("f1_drivers.txt", "r") as file:
            drivers_info = {}
            for line in file:
                line = line.strip()
                if line:
                    parts = line.split(',')
                    drivers_info[parts[1]] = f"{parts[2]} ({parts[3]})"
    except FileNotFoundError:
        messagebox.showerror("Error", "The file f1_drivers.txt could not be found.")
        return

    def get_driver_info():
        code = driver_code_entry.get().strip()
        if code in drivers_info:
            messagebox.showinfo("Driver Info", f"{code}: {drivers_info[code]}")
        else:
            messagebox.showerror("Error", f"No information found for code {code}.")

    driver_window = tk.Toplevel()
    driver_window.title("Driver Info")

    tk.Label(driver_window, text="Enter Driver Code:").pack(pady=125)
    driver_code_entry = tk.Entry(driver_window)
    driver_code_entry.pack(pady=55)
    tk.Button(driver_window, text="Search", command=get_driver_info).pack(pady=45)

def lap_times_comparison():
    # Mock data; replace with actual calculations
    
    lap_data = {
        "Lap 1": {"drivers": ["DR1", "DR2", "DR3"], "avg": [80.5, 82.1, 79.8], "min": [79.1, 81.0, 78.3], "max": [82.0, 83.5, 81.2]},
        "Lap 2": {"drivers": ["DR1", "DR2", "DR3"], "avg": [81.0, 83.2, 80.1], "min": [80.0, 82.0, 79.0], "max": [83.0, 84.0, 81.5]},
        "Lap 3": {"drivers": ["DR1", "DR2", "DR3"], "avg": [82.0, 84.5, 81.3], "min": [81.0, 83.0, 80.0], "max": [84.0, 85.0, 82.0]}
    }

    for lap_name, stats in lap_data.items():
        drivers = stats['drivers']
        avg_times = stats['avg']
        min_times = stats['min']
        max_times = stats['max']

        x = range(len(drivers))
        width = 0.25

        plt.bar([pos - width for pos in x], min_times, width, label='Min Times', color='green')
        plt.bar(x, avg_times, width, label='Avg Times', color='yellow')
        plt.bar([pos + width for pos in x], max_times, width, label='Max Times', color='red')

        plt.xlabel('Drivers')
        plt.ylabel('Lap Times (s)')
        plt.title(f'Lap Statistics for {lap_name}')
        plt.xticks(x, drivers)
        plt.legend()
        plt.tight_layout()
        plt.show()

def main():
    root = tk.Tk()
    root.title("F1 Lap Analysis")

    tk.Button(root, text="Lap 1 Info", command=info_lap1, width=55).pack(pady=10)
    tk.Button(root, text="Lap 2 Info", command=info_lap2, width=95).pack(pady=25)
    tk.Button(root, text="Lap 3 Info", command=info_lap3, width=115).pack(pady=35)
    tk.Button(root, text="Driver Info", command=indi_drivers_info, width=135).pack(pady=45)
    tk.Button(root, text="Compare Lap Times", command=lap_times_comparison, width=165).pack(pady=55)

    root.mainloop()

if __name__ == "__main__":
    main()
