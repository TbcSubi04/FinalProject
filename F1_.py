import sys
import matplotlib.pyplot as plt

print("WELCOME TO THE 2024 GRAND PRIX \n")


def info_lap1():
    try:
        with open("lap_times_1.txt", 'r') as f:
            print(f"The location for the first lap is : {f.readline().strip()}\n")    
    except:
        print("The location could not be traced")

    try:
        with open("lap_times_1.txt", 'r') as file:
            lines = file.readlines()    
    except:
        print("The file could not be traced")
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
        shortest_laps=[] 
        longest_laps=[]  
        avg_laps= []

    for driver, times in lap_times.items():  
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
        avg_laps.append(avg_lap_1)
        

        x= range(len((drivers))) # positions all the drivers name in x axis
    plt.figure(figsize=(10, 6)) 
    plt.bar(x, shortest_laps, width=0.3, label='Shortest Lap', color='yellow', align='edge')
    plt.bar([p + 0.3 for p in x], longest_laps, width=0.4, label='Longest Lap', color='lightgreen', align='edge')
    plt.bar([p + 0.6 for p in x], longest_laps, width=0.4, label='Average Lap', color='pink', align='edge')
    plt.xlabel("Drivers", fontsize=12) 
    plt.ylabel("Lap Times (in seconds)", fontsize=12)  
    plt.title("Lap 1 Analysis", fontsize=14)  
    plt.xticks([p + 0.3 for p in x], drivers,fontsize=10)  
    plt.legend()   
    plt.show()


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
        avg_laps= []

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
        avg_laps.append(avg_lap_2)

        x=range(len((drivers)))
    plt.figure(figsize=(10,6))
    plt.title(" Lap 2 Analysis")
    plt.bar(x,shortest_laps, width=0.3, label="Shortest time", color='yellow', align='center')
    plt.bar([p+0.6 for p in x], longest_laps, width=0.4, label='Longest time',color="lightgreen", align='center')
    plt.bar([p+0.3 for p in x], avg_laps, width=0.4, label='Average time',color="pink", align='center')
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
        shortest_laps=[]
        longest_laps=[]
        avg_laps=[]

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
        shortest_laps.append(shortest_lap_3)
        longest_laps.append(longest_lap_3)
        avg_laps.append(avg_lap_3)

        x=range(len((drivers)))
    plt.figure(figsize=[10,6])
    plt.bar(x,shortest_laps, width=0.3, label="Shortest Time", color='yellow', align='edge')
    plt.bar([p + 0.3 for p in x], longest_laps, width=0.4, label="Longest Time", color='lightgreen', align='edge')
    plt.bar([p + 0.6 for p in x], avg_laps, width=0.4, label="LAverage Time", color='pink', align='edge')
    plt.xlabel("Drivers", fontsize=12)
    plt.ylabel("Lap Time (in seconds)", fontsize=12)
    plt.title("Lap 3 Analysis")
    plt.xticks([p + 0.2 for p in x], drivers, fontsize=10)
    plt.legend()
    plt.show()


def all_lap_time():
    total_times = {} 

    all_files = ["lap_times_1.txt", "lap_times_2.txt", "lap_times_3.txt"] 

    for lap_file in all_files:
        try:
            with open(lap_file, 'r') as file:
                lines = file.readlines()
        except:
            print(f"Could not access to any of the files")
            continue

        for line in lines[1:]: 
            driver = line[:3].strip()
            try:
                lap_time = float(line[3:].strip())
            except:
                print(f"Could not convert lap time to float for {driver}")
                continue
            
            if driver not in total_times:
                total_times[driver] = 0  
            total_times[driver] += lap_time

    print("\nTotal lap times across all laps:")
    for driver, total_time in total_times.items():
        print(f"{driver}: {total_time:.3f} seconds")

   
    drivers = list(total_times.keys())  
    times = list(total_times.values()) 

    plt.figure(figsize=(10, 6))
    plt.plot(drivers, times, marker='o', color='b', linestyle='-', linewidth=2, markersize=8, label='Total Time')
    plt.xlabel('Drivers')
    plt.ylabel('Total Lap Time (seconds)')
    plt.title('Total Lap Times Across All Laps')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.legend()
    plt.tight_layout() 
    plt.show()

def find_drivers_info():
   try:
        with open("f1_drivers.txt", "r") as f:
            info_of_drivers = {}  
            for line in f:   
                line = line.strip()     
                if line:     
                    drivers_info = line.split(',')             
                    key = drivers_info[1]     
                    value = f"{drivers_info[2]} ({drivers_info[3]})"  
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
       print("Options:")
       print("  FIRST LAP (lap1)  = Get to see the first lap's result along with the graph")
       print("  SECOND LAP (lap2) = Get to see the second lap's result along with the graph")
       print("  THIRD LAP (lap3)  = Get to see the third lap's result along with  the graph")
       print("  TOTAL-TIME (total_time) = Get to see total lap time across all laps for each driver with graph")
       print("  F1-DRIVERS (driver ) = To find the about the driver's full name and team name")
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
    elif option == "total_time":
        all_lap_time()
    else:
       print(f"Unknown option: {option}")
       print("The only available options: lap1, lap2, lap3, driver, total_time")
       sys.exit(1)

if __name__ == "__main__":
   main()
