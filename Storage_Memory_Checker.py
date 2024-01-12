# Get Storage Information
import subprocess
from datetime import date
result = subprocess.run(["df --total -hl | tail -n 1 | awk \'{print $5}\'"], shell=True, capture_output=True, text=True)
result2 = str(result.stdout)
result_value = result2[:-2]
print(result_value)

# Compare to threshold

System_Data = int(result_value)
Threshold = 5

if System_Data < Threshold:
    print("Available storage space is high")
else:
    print("Available storage space is low”)
    file1 = open('security.log', 'a')
    alert = 'Available storage space is low '
    today = date.today()
    str_date = str(today) + '\n'
    file1.write(alert)
    file1.write(str_date)
    file1.close()


# Memory Section

free_space = subprocess.run(["free | sed -n \'2 p\' | awk \'{print $4}\'"], shell=True, capture_output=True, text=True)
print(free_space.stdout)
total_space = subprocess.run(["free | sed -n \'2 p\' | awk \'{print $2}\'"], shell=True, capture_output=True, text=True)
print(total_space.stdout)

free_memory = int(free_space.stdout)
total_memory = int(total_space.stdout)

Memory_utilization = free_memory/total_memory
print(Memory_utilization)

if Memory_utilization > 0.01:
	print("Memory Utilization is high")
    file1 = open('security.log', 'a')
    alert = 'Memory Utilization is high '
    today = date.today()
    str_date = str(today) + '\n'
    file1.write(alert)
    file1.write(str_date)
    file1.close()
else:
	print("Memory Utilization is low”)