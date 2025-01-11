import sys
import matplotlib.pyplot as plt

def f1_drivers():
    try:
        with open("lap_times_1.txt",'r') as file:
            print(f"The first location of the lap is : {file.readline()}")
    except:
        print("The file could not be traced")

    
def info_lap1():
    lap_times= []     #to store the lap times

    with open ("lap_times_1.txt",'r')as file:
        line= file.readlines()
    for line in line[1:]:  # to start from the line from the second line
        lap_time=float(line[3:])         #slicing to access the lap time (non-string values need to be converted first)
        lap_times.append(lap_time)          #to store the added lap time to the list
        
          

    if lap_times:
        shortest_lap= min(lap_times)   
        longest_lap= max(lap_times)
        avg_lap= sum(lap_times) / len(lap_times)      
        

        print(f"The shortest lap was {shortest_lap:3f}")
        print(f"The longest lap was {longest_lap:3f}")
        print(f"The average lap was {avg_lap:3f}")
        

    else:
        print("None")   

    
def info_lap2():
    try:
        with open("lap_times_2.txt",'r') as file:
            print(f"The location for the second lap is : {file.readline()}")
    except:
        print("Second location could not be traced")        
   
    lap_times2=[]
    file=open("lap_times_2.txt",'r') 
    lines = file.readlines()
    for line in lines[1:]:  
        lap_time=float(line[3:])         
        lap_times2.append(lap_time)        
    
      
    if lap_times2:
        shortest_lap= min(lap_times2)    
        longest_lap= max(lap_times2)      


        print(f"The shortest lap was {shortest_lap:3f}")
        print(f"The longest lap was {longest_lap:3f}")
        
    else:
        print("None")

    file.close()

def info_lap3():
   
    try:
        with open("lap_times_3.txt","r") as f:
            print(f"The location for the third lap is {f.readline()}")
        
    except:
        print("The location for the lap could not be traced")
    

    lap_times3= []

    file= open("lap_times_3.txt",'r')
    lines = file.readlines()
    for line in lines[1:]:  
        lap_time=float(line[3:])        
        lap_times3.append(lap_time)         
        
          

    if lap_times3:
        shortest_lap= min(lap_times3)    
        longest_lap= max(lap_times3)      
        avg_lap= sum(lap_times3) / len(lap_times3)

        print(f"The shortest lap was {shortest_lap:3f}" )
        print(f"The longest lap was {longest_lap:3f}")
        print(f"The average lap was {avg_lap:3f}\n")



    
    

def indi_drivers_info():
    # Mapping the driver's information from the text file by accessing keys and values
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
        return

    
    name_input = input("Enter the driver's code: ")
    if name_input in info_of_drivers:
        print(f"The information for '{name_input}' is {info_of_drivers[name_input]}")
    else:
        print(f"No information found for the key '{name_input}'.")



def plot_lap_times():
    drivers = ["Driver 1", "Driver 2", "Driver 3"]
    shortest_laps = []
    longest_laps = []

    # Gather lap data
    lap1 = info_lap1()
    lap2 = info_lap2()
    lap3 = info_lap3()

    for lap in [lap1, lap2, lap3]:
        if lap:
            shortest_laps.append(lap[0])
            longest_laps.append(lap[1])
        else:
            shortest_laps.append(0)
            longest_laps.append(0)

    # Plotting
    x = range(len(drivers))
    width = 0.4

    plt.bar(x, shortest_laps, width=width, label="Shortest Lap", color="green")
    plt.bar([p + width for p in x], longest_laps, width=width, label="Longest Lap", color="red")

    plt.xlabel("Drivers")
    plt.ylabel("Lap Time (seconds)")
    plt.title("Shortest and Longest Lap Times of Drivers")
    plt.xticks([p + width / 2 for p in x], drivers)
    plt.legend()
    plt.tight_layout()
    plt.show()

# Call the plot function
plot_lap_times()