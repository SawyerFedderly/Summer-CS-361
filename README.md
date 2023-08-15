My microservice is a python file that communicates with the main program through two different text files.

# How to programmatically REQUEST data:

1) open the text file named "timecomp.txt"

2) write the start and end time variables to the text file

### Example call:

textFile = open("timecomp.txt", "w")

starttime = ("4:25:40")

endtime = ("11:40:10")

textFile.write(starttime)

textFile.write("\n")

textFile.write(endtime)

textFile.close()

# How to programmatically RECEIVE data:

1) run the time_comparison_microservice_v2 file to compare the two times and write the difference into another text file

2) open the text file "timeresult.txt"

3) read the contents of the text file and print them to the console

### Example call:

textFile2 = open("timeresult.txt", "r")

difference = textFile2.read()

print(difference)

# UML Diagram

![image](https://github.com/SawyerFedderly/Summer-CS-361/assets/131832431/5e2a37fb-f443-4919-a033-6b2a854218e3)
