import time
def QuickSort(l):
    ''' (list) -> list
    Sorts based around a pivot
    *Not in place, creates a new lists to hold elements temporarily
    *Does not change original list

    Sorts the list and then flattens into a new list.

    >>> QuickSort([4, 3, 1, 2])
    [1, 2, 3, 4]

    >>> QuickSort([5,2,4,7,3,56,7,8,3,2,67,23,67,34,67,45])
    [2, 2, 3, 3, 4, 5, 7, 7, 8, 23, 34, 45, 56, 67, 67, 67]
    
    '''
    #Sorting algorithm
    def qsort(l):
        left = []   #New list for items to left of pivot
        right = []  #New list for items to right of pivot
        equal = []  #New list for items equal to the pivot

        if len(l) == 1: return l    #Returns the only item in the list
        if len(l) == 0: return      #Exits if nothing in list
        else:
            pivot = l[int(len(l)/2)]        #The center item is the pivot
            for i in xrange(len(l)):        #Loops for each element in list
                place = cmp(l[i], pivot)    #Checks if element is smaller or greater than than the pivot
                if place == -1: left.append(l[i])       #Adds element to left list
                elif place == 1: right.append(l[i])     #Adds element to right list
                else: equal.append(l[i])                #Adds to left list if equal to pivot
            return [qsort(left), equal, qsort(right)] #Returns sorted list relative to pivot

    #Reformatting algorithm
    def x(l, newL):
        if type(l) == list:
            if len(l) == 0: return  #Exits if no items in list
            for i in xrange(len(l)):    #Loops for each item in list
                if l[i]:
                    if type(l[i]) == list: x(l[i], newL) #Runs method again through the inner list
                    else: newL.append(l[i])     #Adds items to new list
        else: newL.append(l)    #Adds item to new list    

    #Function Main
    newList = []
    x(qsort(l), newList) #Sorts the list using sorting algorithm, then reformats into new list
    return newList  #Returns the final sorted list

#Dictionary with each type of vehicle
vehicleDict = {"COMPACT":0,
               "FULL-SIZE":1,
               "MID-SIZE": 2,
               "MINICOMPACT": 3,
               "MINIVAN": 4,
               "PICKUP TRUCK - SMALL": 5,
               "PICKUP TRUCK - STANDARD": 6,
               "SPECIAL PURPOSE VEHICLE": 7,
               "STATION WAGON - MID-SIZE": 8,
               "STATION WAGON - SMALL": 9,
               "SUBCOMPACT": 10,
               "SUV - SMALL": 11,
               "SUV - STANDARD": 12,
               "TWO-SEATER": 13,
               "VAN - PASSENGER": 14}

class Car:
    def __init__(self, carList):
        self.make = carList[1]
        self.model = carList[2]
        self.vehicleClass = carList[3]
        self.fuelConsumption = float(carList[10])
    def getFuelConsumption(self):
        return self.fuelConsumption
    def getMake(self):
        return self.make
    def getModel(self):
        return self.model
    def getVehicleClass(self):
        return self.vehicleClass
    def __cmp__(self, other):
        return cmp(self.fuelConsumption, other.getFuelConsumption())
    def __str__(self):
        return self.make+" "+self.model+" with a fuel efficiency of "+str(self.fuelConsumption)+"L/100km.\n"

def ReadData(fileInName):
    fileIn = open(fileInName, "r")   #Open file with data in reading mode

    efficientList = []  #A master list of all top 10 lists for each type of car

    headings = fileIn.readline().split(",")[:15]    #Reads in the first line and changes to a list: sample car data
    headings[10] = "99999"      #Sets the sample car's efficiency to 99999 to be comparable with others
    sampleCar = Car(headings)   #Creates a sample car to populate list

    for i in xrange(len(vehicleDict)):          #Loops for each type of car
        efficientList.append([sampleCar]*10)    #Populates the list with the sample car

    fileIn.readline()   #Reads the next line, which isn't used

    '''Print heading to console
    s = "["+"1st".ljust(20, " ")+"\t"+"2nd".ljust(20, " ")+"\t"+"3rd".ljust(20, " ")+"\t"
    for i in xrange(4, 11):
        s += (str(i)+"th").ljust(20, " ")+"\t"
    s+="]"
    print s'''
    
    #Loops for each line in the file
    for line in fileIn:
        tempList = line.split(",")[:15] #Takes the first 15 columns, which have the data in each line
        if tempList[0] == "": break #Stops the loop if reached the end of data
        newCar = Car(tempList)      #Creates a new car with data
        
        carType = vehicleDict[newCar.getVehicleClass()] #Finds the number corresponding to the car type
        top10 = efficientList[carType]  #Retrieves the top 10 cars for the car type

        if cmp(top10[9], newCar) == 1:  #If the current car's efficiency is better than the 10th top car,
            top10[9] = newCar   #Set the 10th car as the new car
            efficientList[carType] = QuickSort(top10)   #Re-sort the list of top 11 cars

            '''Display top 10 list to console
            if carType == 0:
                s = "["
                for car in efficientList[carType]:
                    s+=(car.getMake()+" "+car.getModel()).ljust(20, " ")+"\t"
                print s+"]"
                time.sleep(1)'''
            
    fileIn.close()          #Closes the file
    return efficientList    #Returns the final list

def WriteSummary(efficientList, fileOutName):
    fileOut = open(fileOutName, "w")         #Open file to be written into

    #Writes a header for the summary to output file
    fileOut.write("Here are the top 10 cars for fuel consumption for each vehicle type:\n")

    for top10 in efficientList:     #Loops for each top 10 list, with the top 10 list as the looping variable
        fileOut.write("\nVehicle Class: "+top10[0].getVehicleClass()+"\n")    #Writes the heading for each car type
        for car in top10:   #Loop for each car in the top 10 list, with the car object as the looping variable
            if car.getMake() != "MAKE":        #Makes sure the car isn't a sample car
                fileOut.write(str(car)) #Writes the model, make, and fuel efficiency of the car
    fileOut.close()         #Closes the file
    return 0

#Main code
myList = ReadData("MY2018 Fuel Consumption Ratings.csv")
WriteSummary(myList, "Fuel_Consumption_Summary.txt")

