import csv
import random
import re

# Input torque function
def inputTorque():
    count = 0
    while count < 2:
        user_input = random.randint(41, 45) # For conveinience's sake, choose a random number instead of manual input
        if float(user_input) >= 42 and float(user_input) <= 45:
            # Return tuple containing torque value and number of attempts taken
            final_value = (user_input, count+1)
            return final_value
            break
        elif float(user_input) < 42 or float(user_input) > 45:
            # Give 2 attempts to get correct value
            print("ERROR: Incorrect value\n")
            count += 1
        if count >= 2:
            # Automatically set value to NG for "No Good" if max attemtps exceeded
            print("ERROR: Max attempts exceeded\n")
            user_input = "NG"
            return user_input

# Function to check that the correct part is being installed
def getpartID():
    #Format for part code
    part_format = r'^LFS-\d{4}$'
    part = input('Enter part ID: ')
    if bool(re.match(part_format, part)) == False:
        print('Error: incorrect part')
        next_action = input()
        if next_action == "REPAIR":
            # Manual override
            part = part
            return part
    else:
        return part

# Open file which has vins for this production run
with open("vins.txt") as vins_file:
    vins = vins_file.read().split()

# Compile information
with open("production_report.csv", "w", newline = '') as report:
        # Set up csv
        report_writer = csv.writer(report)
        report_writer.writerow(['sequence', 'vin', 'partID', 't1', 't2', 't3', 't4'])
        # Set starting sequence
        af_sequence = 1
        for vin in vins:
            # Verify frame being scanned is correct frame
            expected_vin = int(input("Enter frame sequence: "))
            
            if expected_vin != af_sequence:
                # Provide a way to correct out of sequence scans
                print("ERROR: OSS")
                next_action = input()
                if next_action == "REPAIR":
                    # Manual override 
                    af_sequence = expected_vin
                    continue
            else:
                 # Check that correct part is being installed
                 part = getpartID()
            
                 # Get tourques of bolts
                 print("Please input torques:")
                 t1 = inputTorque()
                 t2 = inputTorque()
                 t3 = inputTorque()
                 t4 = inputTorque()
                 
                 # Enter values into csv file
                 print("Process complete")
                 report_writer.writerow([f'{af_sequence}', f'{vin}', f'{part}', f'{t1}', f'{t2}', f'{t3}', f'{t4}'])
            
                 # Move on to next sequence number
                 af_sequence += 1
            
               


    



    

