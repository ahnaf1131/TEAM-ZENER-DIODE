import time

#max distance for car 

maxFrontDistance=25     #in cm
minLeftSideDistance=50
minRightSideDistance=50

# sonar sensor inputs
leftDistance=0
rightDistance=0
frontDistance=0

lapCount=0
colorSensorInGround=False


def turnRight():
    #write code for turning wheel right
    print('turned right')

def turnLeft():
    #write code for turning wheel left
    print('turned left')


def adjustCarInMiddle():

    if leftDistance>rightDistance:
        #turn a bit left
        print("turned a little left")
    if rightDistance>leftDistance:
        #turn a bit right
        print("turned a little right")


while lapCount<24:
    
    #write code for accelarating car
    if rightDistance>minRightSideDistance:
        if frontDistance<maxFrontDistance: #to be modified
            turnRight()
            startTime=time.time()
            while time.time()-startTime<2: #to be modified
                adjustCarInMiddle()

        
    if leftDistance>minLeftSideDistance:
        if frontDistance<maxFrontDistance:
            turnLeft()
            startTime=time.time()
            while time.time()-startTime<2:
                adjustCarInMiddle()

    if colorSensorInGround :#if the color sensor from the ground is true we will increment lapCount
        lapCount+=1
    #the car could move unparrally after turning, so we will run a function to fix it in 2 seconds


