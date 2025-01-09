# Agro-Data-Logger
# **Smart Soil Monitor**

A project to measure and log soil parameters using RS-485 Modbus sensors and Arduino. The collected data is sent to a serial port and logged into a CSV file for further analysis.

## **Features**
- Reads multiple soil parameters using Modbus RS-485 sensors:
  - Moisture (%)
  - Temperature (°C)
  - Electrical Conductivity (EC) (us/cm)
  - pH
  - Nitrogen (mg/kg)
  - Phosphorus (mg/kg)
  - Potassium (mg/kg)
- Logs data into a CSV file for analysis.
- Real-time serial data display on the connected computer.

## **Hardware Requirements**
- Arduino (or compatible microcontroller)
- RS-485 to TTL Converter
- Soil sensors supporting Modbus communication:
  - Moisture Sensor
  - Temperature Sensor
  - EC Sensor
  - pH Sensor
  - NPK Sensor
- Jumper wires and connectors
- Computer with a USB port

## **Software Requirements**
- Arduino IDE
- Python 3.x
- Required Python libraries:
  - `pyserial`
  - `csv`

## **How It Works**
1. **Arduino Setup**:  
   - The Arduino reads data from Modbus RS-485 soil sensors.
   - The data is structured and sent over the serial port.

2. **Python Script**:  
   - The Python script reads serial data from the Arduino.
   - Extracted data is logged into a CSV file (`sensor_data.csv`) in real-time.

3. **Data Analysis**:  
   - The CSV file can be imported into tools like Excel or MATLAB for further analysis.

## **Setup and Usage**

### **1. Hardware Connections**
- Connect the RS-485 soil sensors to the Arduino through the RS-485 to TTL converter.
- Use the `RE` and `DE` pins for switching between transmit and receive modes.

### **2. Arduino Code**
- Upload the provided Arduino sketch (`arduino_soil_monitor.ino`) to the Arduino using the Arduino IDE.

### **3. Python Script**
- Install the required Python libraries:
  ```bash
  pip install pyserial
