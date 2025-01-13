import serial
import csv
import time
from datetime import datetime  # Import datetime for timestamp

# Set up the serial connection (adjust 'COM5' to your Arduino's port)
ser = serial.Serial('COM5', 9600, timeout=1)  # Adjust COM port as needed
time.sleep(2)  # Wait for the connection to establish

# Open or create a CSV file to store data
with open('SENSOR2.csv', mode='a', newline='') as file:
    writer = csv.writer(file)
   
    # Check if the CSV file is empty to add the header
    if file.tell() == 0:
        writer.writerow(['Timestamp', 'Moisture (%)', 'Temperature (°C)', 'EC (us/cm)', 'pH', 'Nitrogen (mg/kg)', 'Phosphorous (mg/kg)', 'Potassium (mg/kg)'])

    while True:
        # Read a line of data from Arduino (you should format the output on Arduino)
        line = ser.readline().decode('utf-8').strip()
       
        if line:
            # Uncomment the following line if you want to debug received data
            # print(f"Received data: {line}")
           
            try:
                # Split the line into individual components using ',' as the delimiter
                data_values = line.split(',')

                # Extract each value based on the format "Parameter: value"
                moisture = float(data_values[0].split(':')[1].strip())
                temperature = float(data_values[1].split(':')[1].strip())
                ec = float(data_values[2].split(':')[1].strip())
                ph = float(data_values[3].split(':')[1].strip())
                nitrogen = float(data_values[4].split(':')[1].strip())
                phosphorous = float(data_values[5].split(':')[1].strip())
                potassium = float(data_values[6].split(':')[1].strip())

                # Get the current timestamp
                timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

                # Write the timestamp and sensor values to the CSV file
                writer.writerow([timestamp, moisture, temperature, ec, ph, nitrogen, phosphorous, potassium])

                # Print the timestamp and values for debugging
                print(f"{timestamp}, {moisture}, {temperature}, {ec}, {ph}, {nitrogen}, {phosphorous}, {potassium}")

            except Exception as e:
                print(f"Error parsing data: {e}")

        time.sleep(1)  # Adjust delay as needed (1 second in this case)
