import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

def plot_graph(drivers, shortest_laps, longest_laps, title):
    # Create a new figure for the graph
    figure = plt.Figure(figsize=(8, 5), dpi=100)
    ax = figure.add_subplot(111)

    x = range(len(drivers))
    ax.bar(x, shortest_laps, width=0.4, label='Shortest Lap', color='yellow', align='edge')
    ax.bar([p + 0.4 for p in x], longest_laps, width=0.4, label='Longest Lap', color='lightgreen', align='edge')

    ax.set_xlabel("Drivers", fontsize=12)
    ax.set_ylabel("Lap Times (in seconds)", fontsize=12)
    ax.set_title(title, fontsize=14)
    ax.set_xticks([p + 0.2 for p in x])
    ax.set_xticklabels(drivers, fontsize=10)
    ax.legend()

    return figure

def info_lap(filename, title):
    # Clear main frame
    clear_frame()

    # Create the back button
    ttk.Button(main_frame, text="Go Back", command=show_main_menu).pack(anchor="nw", pady=10)

    try:
        with open(filename, 'r') as file:
            location = file.readline().strip()
            result_label = tk.Label(main_frame, text=f"Location of the lap: {location}\n\n", font=("Arial", 10), anchor="nw", justify="left")
            result_label.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
    except:
        result_label = tk.Label(main_frame, text="The file could not be traced.\n", font=("Arial", 10), anchor="nw", justify="left")
        result_label.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        return

    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
    except:
        result_label["text"] += "The file was not found.\n"
        return

    lap_times = {}
    for line in lines[1:]:
        driver = line[:3].strip()
        try:
            lap_time = float(line[3:].strip())
        except:
            result_label["text"] += f"Could not convert lap time for driver {driver}.\n"
            continue
        if driver not in lap_times:
            lap_times[driver] = []
        lap_times[driver].append(lap_time)

    drivers = []
    shortest_laps = []
    longest_laps = []

    for driver, times in lap_times.items():
        if not times:
            continue
        shortest_lap = min(times)
        longest_lap = max(times)
        drivers.append(driver)
        shortest_laps.append(shortest_lap)
        longest_laps.append(longest_lap)

        # Append driver lap times to result_label
        result_label["text"] += f"{driver}: Shortest Lap = {shortest_lap:.3f}, Longest Lap = {longest_lap:.3f}\n"

    # Plot the graph
    figure = plot_graph(drivers, shortest_laps, longest_laps, title)

    # Embed the graph in Tkinter
    canvas = FigureCanvasTkAgg(figure, master=main_frame)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack()

def show_main_menu():
    # Clear main frame
    clear_frame()

    # Add the buttons back to the main frame
    ttk.Button(main_frame, text="Analyze Lap 1", command=lambda: info_lap("lap_times_1.txt", "Lap 1 Analysis")).pack(side=tk.LEFT, padx=5)
    ttk.Button(main_frame, text="Analyze Lap 2", command=lambda: info_lap("lap_times_2.txt", "Lap 2 Analysis")).pack(side=tk.LEFT, padx=5)
    ttk.Button(main_frame, text="Analyze Lap 3", command=lambda: info_lap("lap_times_3.txt", "Lap 3 Analysis")).pack(side=tk.LEFT, padx=5)
    ttk.Button(main_frame, text="Exit", command=root.quit).pack(side=tk.RIGHT, padx=5)

def clear_frame():
    for widget in main_frame.winfo_children():
        widget.destroy()

# GUI Setup
root = tk.Tk()
root.title("Lap Analysis")
root.geometry("900x700")

main_frame = ttk.Frame(root, padding=10)
main_frame.pack(fill=tk.BOTH, expand=True)

# Show the main menu initially
show_main_menu()

root.mainloop()
