My microservice is a python file that communicates with the main program through the built-in python library, or system calls.

# How to programmatically REQUEST data:

1) import the time_comparison_microservice file

2) input the start and end time variables

3) call the microservice function using the start and end times as parameters: 
time_comparison_microservice.diff(starttime, endtime)

### Example call:

import time_comparison_microservice

starttime = datetime.strptime("4:25:40", "%H:%M:%S")

endtime = datetime.strptime("11:40:10", "%H:%M:%S")

time_comparison_microservice.diff(starttime, endtime)

# How to programmatically RECEIVE data:

1) import the time_comparison_microservice file

2) input the start and end time variables

3) call the microservice function using the start and end times as parameters and save the data to a variable: 
difference = time_comparison_microservice.diff(starttime, endtime)

### Example call:

import time_comparison_microservice

starttime = datetime.strptime("4:25:40", "%H:%M:%S")

endtime = datetime.strptime("11:40:10", "%H:%M:%S")

difference = time_comparison_microservice.diff(starttime, endtime)

print(difference)

# UML Diagram

![image](https://github.com/SawyerFedderly/Summer-CS-361/assets/131832431/bbb92f8d-3475-46cb-ad4f-684207ea4d30)
