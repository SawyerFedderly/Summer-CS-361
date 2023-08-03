import time
from datetime import datetime

import time_comparison_microservice

# PROGRAM CODE
# PROGRAM CODE

# REPLACE WITH ACTUAL SOURCE OF START/END TIMES
starttime = datetime.strptime("4:25:40", "%H:%M:%S")
endtime = datetime.strptime("11:40:10", "%H:%M:%S")

# PROGRAM CODE
# PROGRAM CODE

# CALL TO MICROSERVICE
difference = time_comparison_microservice.diff(starttime, endtime)

time.sleep(1)
print("Time difference is:", difference, "(Hr:Min:Sec)")

# PROGRAM CODE
# PROGRAM CODE