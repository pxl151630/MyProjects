
# coding: utf-8

# In[106]:

# use csv module, in Chapter 8
import csv 

# first line of our file
csv_header = [['tail_number', 'origin', 'destination', 'departure_time', 'arrival_time']]
# file name
file_name = 'flight_schedule.csv'
# create file
fout = open(file_name, 'wt', newline='')
# create CSV format writter as csvout
csvout = csv.writer(fout)
# write csv_header to file, in CSV format
csvout.writerows(csv_header)


# In[107]:

AusDal_fly_time = 50
AusHou_fly_time = 45
HouDal_fly_time = 65


# In[108]:

Aus_ground_time = 25
Dal_ground_time = 30
Hou_ground_time = 35


# In[109]:

def findAvailableGate(location, arriveTime):
    for gate in Gates:
        if (gate.location is location and gate.availableTime <= arriveTime):
            return gate 
    return None


# In[110]:

def findGateAvailableTime(location1, location2):
    available_time = 1500
    for gate in Gates:
        if ((gate.location is location1 or gate.location is location2)
            and gate.availableTime < available_time): 
            available_time = gate.availableTime
    return available_time


# In[111]:

def updateGateAvailableTime(targetGate, new_available_time):
    for gate in Gates:
        if (gate.location is targetGate.location and gate.availableTime == targetGate.availableTime):
            gate.availableTime = new_available_time


# In[112]:

def swapToSecond(airplane):
    temp = Airplanes[0]
    Airplanes[0] = Airplanes[1]
    Airplanes[1] = temp


# In[113]:

def convertTime(number):
    hours = str(number // 60)
    mins = str(number % 60) 
    if len(mins) < 2 :
        mins= '0'+mins
    if len(hours) <2 :
        hours = '0'+hours
    return hours + mins


# In[114]:

def findGroundTimeByLocation(location):
    if location is AUS:
        return Aus_ground_time
    elif location is DAL:
        return Dal_ground_time
    elif location is HOU:
        return Hou_ground_time


# In[115]:

def reorderAirplanes():
    for i in range(0, len(Airplanes)):
        for j in range(1,len(Airplanes)-i):
            if Airplanes[j - 1].departure_time > Airplanes[j].departure_time:
            
                temp = Airplanes[j-1]
                Airplanes[j-1] = Airplanes[j]
                Airplanes[j] = temp


# In[116]:

def swapToSecond(airplane):
    temp = Airplanes[0]
    Airplanes[0] = Airplanes[1]
    Airplanes[1] = temp


# In[117]:

class Gate:
    def __init__(self,location, availableTime):
        self.location = location
        self.availableTime = availableTime

class Airplane:
    def __init__(self,tail_number,origin,departure_time):
        self.tail_number = tail_number
        self.origin = origin
        self.departure_time = departure_time


# In[118]:

AUS = 'AUS'
DAL = 'DAL'
HOU = 'HOU'

gate1 = Gate(AUS, 360) 
gate2 = Gate(DAL, 360)
gate3 = Gate(DAL, 360)
gate4 = Gate(HOU, 360)
gate5 = Gate(HOU, 360)
gate6 = Gate(HOU, 360)

Gates = [gate1, gate2, gate3, gate4, gate5, gate6] 

T1 = Airplane('T1', AUS, 360)
T2 = Airplane('T2', DAL, 360)
T3 = Airplane('T3', DAL, 360)
T4 = Airplane('T4', HOU, 360)
T5 = Airplane('T5', HOU, 360)
T6 = Airplane('T6', HOU, 360)

Airplanes=[T1,T2,T3,T4,T5,T6]


# In[119]:

#create new list
result_list = []

while True: 
    origin = Airplanes[0].origin
    departure_time = Airplanes[0].departure_time
    result_arrive_time = 0
        
    if origin is AUS : 
        dal_arrive_time = departure_time + AusDal_fly_time
        hou_arrive_time = departure_time + AusHou_fly_time
            
        targetGate = findAvailableGate(HOU, hou_arrive_time)
        result_arrive_time = hou_arrive_time
        
        if  targetGate is None:
            targetGate = findAvailableGate(DAL, dal_arrive_time)
            result_arrive_time = dal_arrive_time
        
            if targetGate is None:
                gate_available_time = findGateAvailableTime(HOU, DAL)
                new_departure_time = gate_available_time - AusHou_fly_time
                Airplanes[0].departure_time = new_departure_time
                reorderAirplanes()
                continue

                       
    elif origin is DAL:
            aus_arrive_time = departure_time + AusDal_fly_time
            hou_arrive_time = departure_time + HouDal_fly_time

            targetGate = findAvailableGate(AUS, aus_arrive_time)
            result_arrive_time = aus_arrive_time

            if targetGate is None :
                targetGate = findAvailableGate(HOU, hou_arrive_time)
                result_arrive_time = hou_arrive_time
                
                if targetGate is None:
                    gate_available_time = findGateAvailableTime(AUS, HOU)
                    new_departure_time = gate_available_time - AusHou_fly_time;
                    Airplanes[0].departure_time = new_departure_time
                    reorderAirplanes()
                    #swapToSecond()
                    continue
                    
    elif origin is HOU: 
        aus_arrive_time = departure_time + AusHou_fly_time
        dal_arrive_time = departure_time + HouDal_fly_time

        targetGate = findAvailableGate(AUS, aus_arrive_time)
        result_arrive_time = aus_arrive_time;

        if targetGate is None :
            targetGate = findAvailableGate(DAL, dal_arrive_time)
            result_arrive_time = dal_arrive_time

            if targetGate is None:
                gate_available_time = findGateAvailableTime(AUS,DAL)
                new_departure_time = gate_available_time - AusHou_fly_time
                Airplanes[0].departure_time = new_departure_time
                reorderAirplanes()
                continue
                   
    if result_arrive_time >= 1320:
        break
            
    #list
    create_flight = [Airplanes[0].tail_number, origin, targetGate.location, convertTime(departure_time), 
                     convertTime(result_arrive_time)]
    
  
    # append create_fligt to result_list
    result_list.append(create_flight)
    
    

    # update departure location and departure time 
    new_location = targetGate.location
    new_departure_time = result_arrive_time + findGroundTimeByLocation(new_location)
    Airplanes[0].origin = new_location
    Airplanes[0].departure_time = new_departure_time
    
    # update gate status
    updateGateAvailableTime(targetGate, new_departure_time + 1)

    #Use BubbleSort to update Airplanes order
    reorderAirplanes()

    
#import operator
result_list.sort(key= lambda x: (x[0], x[3]))

print(result_list)

#write the result into file
csvout.writerows(result_list)
    
    
# close file after loop
fout.close()
        


# In[ ]:




# In[ ]:



