# Analyzing-and-plotting-rate-changes-in-counters-by-using-SNMP

This project is about to know the change in rate of different counters and to know difference between their performance under different conditions like when network elements restart, wrapping in different counter types etc. such the obtained data from the script (prober.py) is sent to InfluxDB database and to plot the rates in Grafana by using the script(backend.py). 
  
How to use this project: 
  
  1. To use the above scripts first of all you should install grafana, InfluxDB in your system.
  2. first execute the script prober.py, if it runs and give you raw data.
  3. Then in the next step you need to take this raw data and to plot it in grafana, for this purpose you need to configure InfluxDB to take the data and to send instantaneously to grafana to plot them, for that purpose you need to execute backend.py file.
  
