import sys
import matplotlib.pyplot as plt


def info_lap1():
    try:
        with open("lap_times_1.txt",'r') as file:
            print(f"The first location of the lap is : {file.readline()}")
    except:
        print("The file could not be traced")
 

    try:
        with open("lap_times_1.txt", 'r') as file:
            lines = file.readlines()
    except:
        print(f"The file was not found.")
        return

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

    for driver, times in lap_times.items():  # For each driver, calculate the shortest, longest, and average lap times
        if not times:
            continue
        shortest_lap_1 = min(times)
        longest_lap_1= max(times)
        avg_lap_1 = sum(times) / len(times)

        print(f"The shortest lap time for {driver} in the first lap is : {shortest_lap_1:.3f}")
        print(f"The longest lap time for {driver}  in the first lap is {longest_lap_1:.3f}")
        print(f"The average lap time for {driver} in the first lap is {avg_lap_1:.3f}\n")

                 


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

    for driver, times in lap_times1.items():  
        if not times:
            continue
        shortest_lap_2 = min(times)
        longest_lap_2= max(times)
        avg_lap_2 = sum(times) / len(times)


        print(f"The shortes lap  time of {driver} in second lap is : {shortest_lap_2:.3f}")
        print(f"The longest lap  time of {driver} in second lap is : {longest_lap_2:.3f}")
        print(f"The average lap time is {avg_lap_2}\n ")


def info_lap3():
    try:
        with open("lap_times_1.txt",'r') as file:
            print(f"The first location of the lap is : {file.readline()}")
    except:
        print("The file could not be traced")
 

    try:
        with open("lap_times_1.txt", 'r') as file:
            lines = file.readlines()
    except:
        print(f"The file was not found.")
        return

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

    for driver, times in lap_times.items():  # For each driver, calculate the shortest, longest, and average lap times
        if not times:
            continue
        shortest_lap_1 = min(times)
        longest_lap_1= max(times)
        avg_lap_1 = sum(times) / len(times)

        print(f"The shortest lap time for {driver} in the first lap is : {shortest_lap_1:.3f}")
        print(f"The longest lap time for {driver}  in the first lap is {longest_lap_1:.3f}")
        print(f"The average lap time for {driver} in the first lap is {avg_lap_1:.3f}\n")

                 


def info_lap2():
    try:
        with open("lap_times_3.txt",'r')as location:
            print(f"The location for the third lap is : {location.readline()}")
    except:
        print("The location could not be located") 

    try:
        with open("lap_times_3.txt",'r')as file:
            lines=file.readlines() 

    except:
        print("The file could not be traced.")

    lap_times2 = {}  

    for line in lines[1:]:
        driver = line[:3].strip() 
        try:
            lap_time = float(line[3:].strip()) 
        except:
            print("Could not convert lap time to float")
            

        if driver not in lap_times2:
            lap_times2[driver] = []  
        lap_times2[driver].append(lap_time) 

    for driver, times in lap_times2.items():  
        if not times:
            continue
        shortest_lap_3 = min(times)
        longest_lap_3= max(times)
        avg_lap_3 = sum(times) / len(times)


        print(f"The shortes lap  time of {driver} in second lap is : {shortest_lap_3:.3f}")
        print(f"The longest lap  time of {driver} in second lap is : {longest_lap_3:.3f}")
        print(f"The average lap time is {avg_lap_3}\n ")


    
def indi_drivers_info():
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






   




info_lap1()
info_lap2()
info_lap3()
indi_drivers_info()



