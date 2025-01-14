import sys
import matplotlib.pyplot as plt


def info_lap1():
    try:
        with open("lap_times_1.txt", 'r') as f:
            print(f"The location for the first lap is : {f.readline().strip()}")
    except:
        print("The location could not be traced")

    try:
        with open("lap_times_1.txt", 'r') as file:
            lines = file.readlines()
    except:
        print("The file could not be traced")
        return  # Exit the function if the file cannot be read


    lap_times = {}  # an empty dictionary to store lap times for each driver

    for line in lines[1:]:  # Loop through each line in the file, starting from the second line
        driver = line[:3].strip()  # Extract the driver code (first 3 characters)
        try:
            lap_time = float(line[3:].strip()) # Extract the lap time and convert it to a float
        except:
            print("Could not convert lap time to float")
            
        if driver not in lap_times:
            lap_times[driver] = []  # If the driver is not in the dictionary, add them with an empty list
        lap_times[driver].append(lap_time)  # Add the lap time to the driver's list

        drivers=[]
        shortest_laps=[]
        longest_laps=[]

    for driver, times in lap_times.items():  # For each driver, calculate the shortest, longest, and average lap times
        if not times:
            continue
        shortest_lap_1 = min(times)
        longest_lap_1= max(times)
        avg_lap_1 = sum(times) / len(times)


        print(f"The shortest lap time of {driver} for the first lap is : {shortest_lap_1:.3f}")
        print(f"The longest lap time of {driver} for the  first lap is : {longest_lap_1:.3f}")
        print(f"The average lap time of {driver} for the first lap is {avg_lap_1:.3f}\n")

        
        drivers.append(driver)
        shortest_laps.append(shortest_lap_1)
        longest_laps.append(longest_lap_1)
        

        x= range(len((drivers))) #x positions for the bars

    plt.figure(figsize=(10, 6))  # Increase figure size for better readability
    plt.bar(x, shortest_laps, width=0.4, label='Shortest Lap', color='yellow', align='edge')
    plt.bar([p + 0.4 for p in x], longest_laps, width=0.4, label='Longest Lap', color='lightgreen', align='edge')
    plt.xlabel("Drivers", fontsize=12)  # Increase font size for x-label
    plt.ylabel("Lap Times (in seconds)", fontsize=12)  # Increase font size for y-label
    plt.title("Lap 1 Analysis", fontsize=14)  # Increase font size for title
    plt.xticks([p + 0.2 for p in x], drivers,fontsize=10)  # Rotate x-tick labels
    plt.legend()
    #plt.grid(axis='both')
   # plt.tight_layout()  # Adjust layout to make room for rotated labels
    plt.show()


#rotation=45, ha='right', fontsize=10)
def info_lap2():
    try:
        with open("lap_times_2.txt",'r')as location:
            print(f"The location for the second lap is : {location.readline()}")
    except:
        print("The location could not be located") 

    try:
        with open("lap_times_2.txt",'r')as file:
            lines=file.readlines() 

    except:
        print("The file could not be traced.")

    lap_times1 = {}  

    for line in lines[1:]:
        driver = line[:3].strip() 
        try:
            lap_time = float(line[3:].strip()) 
        except:
            print("Could not convert lap time to float")
            

        if driver not in lap_times1:
            lap_times1[driver] = []  
        lap_times1[driver].append(lap_time) 

        drivers=[]
        shortest_laps=[]
        longest_laps=[]

    for driver, times in lap_times1.items():  
        if not times:
            continue
        shortest_lap_2 = min(times)
        longest_lap_2= max(times)
        avg_lap_2 = sum(times) / len(times)


        print(f"The shortest lap  time of {driver} for the second lap is : {shortest_lap_2:.3f}")
        print(f"The longest lap  time of {driver} for the second lap is : {longest_lap_2:.3f}")
        print(f"The average lap time of {driver} for the second lap is  {avg_lap_2}\n ")

        drivers.append(driver)
        shortest_laps.append(shortest_lap_2)
        longest_laps.append(longest_lap_2)

        x=range(len((drivers)))

    plt.figure(figsize=(10,6))
    plt.title(" Lap 2 Analysis")
    plt.bar(x,shortest_laps, width=0.4, label="shortest_time", color='yellow', align='center')
    plt.bar([p+0.4 for p in x], longest_laps, width=0.4, label='longest_time',color="lightgreen", align='center')
    plt.xlabel("Drivers", fontsize=12)
    plt.ylabel("Lap Times (in seconds)", fontsize=12)
    plt.xticks([p + 0.2 for p in x],drivers, fontsize=10)
    plt.legend()
    plt.show()



def info_lap3():
    try:
        with open("lap_times_3.txt",'r') as file:
            print(f"The location for the third lap is : {file.readline()}")
    except:
        print("The file could not be traced")
 

    try:
        with open("lap_times_3.txt", 'r') as file:
            lines = file.readlines()
    except:
        print(f"The file was not found.")
        return

    lap_times = {}  

    for line in lines[1:]: 
        driver = line[:3].strip() 
        try:
            lap_time = float(line[3:].strip()) 
        except:
            print("Could not convert lap time to float")
            

        if driver not in lap_times:
            lap_times[driver] = []  
        lap_times[driver].append(lap_time)  

        drivers=[]
        shortest_laps3=[]
        longest_laps3=[]

    for driver, times in lap_times.items():  
        if not times:
            continue
        shortest_lap_3 = min(times)
        longest_lap_3= max(times)
        avg_lap_3 = sum(times) / len(times)

        print(f"The shortest lap time of {driver} for the third lap is : {shortest_lap_3:.3f}")
        print(f"The longest lap time of {driver}  for the third lap is {longest_lap_3:.3f}")
        print(f"The average lap time of {driver} for the third lap is {avg_lap_3:.3f}\n")

        drivers.append(driver)
        shortest_laps3.append(shortest_lap_3)
        longest_laps3.append(longest_lap_3)

        x=range(len((drivers)))
    
    plt.figure(figsize=[10,6])
    plt.bar(x,shortest_laps3, width=0.4, label="Shortest Time", color='yellow', align='edge')
    plt.bar([p + 0.4 for p in x], longest_laps3, width=0.4, label="Longest Time", color='lightgreen', align='edge')
    plt.xlabel("Drivers", fontsize=12)
    plt.ylabel("Lap Time (in seconds)", fontsize=12)
    plt.title("Lap 3 Analysis")
    plt.xticks([p + 0.2 for p in x], drivers, fontsize=10)
    plt.legend()
    plt.show()

                 

def find_drivers_info():
    # Mapping the drivers' information from the text file by accessing keys and values
    try:
        with open("f1_drivers.txt", "r") as f:
            info_of_drivers = {}  # An empty dictionary for storing key-value pairs
            for line in f:
                line = line.strip()
                if line:
                    drivers_info = line.split(',')            #to diffrentiate the keys and value sperated by ,
                    key = drivers_info[1] 
                    value = f"{drivers_info[2]} ({drivers_info[3]})"  # Driver name and team
                    info_of_drivers[key] = value
    except:
        print("The file you are trying to access does not exist.")
        
    name_input = input("Enter the driver's code: ")
    if name_input in info_of_drivers:
        print(f"The information for '{name_input}' is {info_of_drivers[name_input]}")
    else:
        print(f"No information found for the key '{name_input}'.")


def main():
    if len(sys.argv) < 2:
        print("Usage: python script.py <option>")
        print("Options:")
        print("  lap1   - Analyze first lap data")
        print("  lap2   - Analyze second lap data")
        print("  lap3   - Analyze third lap data")
        print("  driver - Find driver information")
        sys.exit(1)

    option = sys.argv[1].lower()

    if option == "lap1":
        info_lap1()
    elif option == "lap2":
        info_lap2()
    elif option == "lap3":
        info_lap3()
    elif option == "driver":
        find_drivers_info()
    else:
        print(f"Unknown option: {option}")
        print("Available options: lap1, lap2, lap3, driver")
        sys.exit(1)


if __name__ == "__main__":
    main()


         







       


