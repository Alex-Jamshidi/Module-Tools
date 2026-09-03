# Laptop Allocation Program

## About
A program that assigns laptops to people based on a list of operating system preferences, it includes a simulation that can be re-run to simulate different scenarios.

## Specification

Create a program that alllocate laptops to people based on a list of preferred operating systems. Every person should be allocated exactly one laptop.

If we define "sadness" as the number of places down in someone's ranking the operating system the ended up with (i.e. if your preferences were [UBUNTU, ARCH, MACOS] and you were allocated a MACOS machine your sadness would be 2), we want to minimise the total sadness of all people. If we allocate someone a laptop with an operating system not in their preferred list, treat them as having a sadness of 100.
 
## To run code
python3 -m venv .venv  
. .venv/bin/activate  
pip install -r requirements.txt  
python3 simulate.py 

## About Allocation
Allocation of laptops works using the Hungarian algorithm.
This is achieved using the linear_sum_assignment function in scipy which acts on a cost matrix constructed from the possible combinations between each person and laptop.

## About Simulation
To test the code for different scenarios, a simulation was created, which simulates:
- A random laptop to person ratio between 0.5 and 2
- A random number of people between 10 and 100
- Therefore a theoretical random number of laptops between 5 and 200
- Random percentage chances a person will be created with 1, 2 or 3 preferred operating systems (randomly assigned)

When the simulation is run the statistics and output data are logged to a log.txt file and partially to the terminal.
An example of a simulation is shown in this repo in log.txt.
