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
        lines = file.readlines()
    for line in lines[1:]:  # to start from the line from the second line
        driver=line[:3]    #slicing in order trace  the drivers code
        lap_time=float(line[3:])         #slicing to access the lap time (non-string values need to be converted first)
        lap_times.append(lap_time)          #to store the added lap time to the list
        
          

    if lap_times:
        shortest_lap= min(lap_times)   
        longest_lap= max(lap_times)      
        avg_lap= sum(lap_times) / len(lap_times)

        print(f"The shortest lap was {shortest_lap:3f} by {driver}")
        print(f"The longest lap was {longest_lap:3f} by {driver}")
        print(f"The average lap was {avg_lap:3f}")
        

    else:
        print("None")
    
                 


def info_lap2():
   
    lap_times2=[]
    file=open("lap_times_2.txt",'r') 
    lines = file.readlines()
    for line in lines[1:]:  
        driver=line[:3]    
        lap_time=float(line[3:])         
        lap_times2.append(lap_time)        
    
      
    if lap_times2:
        shortest_lap= min(lap_times2)    
        longest_lap= max(lap_times2)      
        avg_lap= sum(lap_times2) / len(lap_times2)

        print(f"The shortest lap was {shortest_lap:3f} by {driver}")
        print(f"The longest lap was {longest_lap:3f} by {driver}")
        print(f"The average lap was {avg_lap:3f}\n")

    else:
        print("None")

    file.close()

def info_lap3():
   
    try:
        with open("lap_times_3.txt","r") as f:
            print(f"The location for the third lap is {f.readline()}")
        
    except:
        print("The location for the lap could not be traced")
    f.close()

    lap_times3= []

    file= open("lap_times_3.txt",'r')
    lines = file.readlines()
    for line in lines[1:]:  
        driver=line[:3]   
        lap_time=float(line[3:])        
        lap_times3.append(lap_time)         
        
          

    if lap_times3:
        shortest_lap= min(lap_times3)    
        longest_lap= max(lap_times3)      
        avg_lap= sum(lap_times3) / len(lap_times3)

        print(f"The shortest lap was {shortest_lap:3f} by {driver}")
        print(f"The longest lap was {longest_lap:3f} by {driver}")
        print(f"The average lap was {avg_lap:3f}\n")

    else:
        print("None")
    
    

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
        return

    
    name_input = input("Enter the driver's code: ")
    if name_input in info_of_drivers:
        print(f"The information for '{name_input}' is {info_of_drivers[name_input]}")
    else:
        print(f"No information found for the key '{name_input}'.")








   



f1_drivers()
info_lap1()
info_lap2()
info_lap3()
indi_drivers_info()



