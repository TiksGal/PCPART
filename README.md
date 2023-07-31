# PCPART
App written by OOP principles.

<!-- Phase 1:  -->
Create a class that would represent pc parts. It should contain basic methods to retreive items name, price, colour (if applicable).PC part list can be found here: https://pcpartpicker.com/list/The every separate part should have at least 3-4 methods to gather this part specific data (example: CPU - brand , speed, power usuage etc.)At this stage, dictionary data structures can work as Database. OOP abstraction, inheritance and encapsulation must be presented in a code base. Unit tests must be written for the methods.

<!-- Phase 2:  -->
Add logging to all necessary functionality to see the data flow (with logger config.).
Add exception handling , describe your own exceptions if necessary. 
Create functions that would update current datasets (database).
Add functions that would parse durrent datasets(database) by specific parameters (CPU name = 'AMD')
Use  List, Dict comprehentions to get parsed data.

Prerequisites
Python 3.7 or newer
Project Structure
The application consists of the following files:

pc_part.py: Contains class definitions and method implementations for different PC parts.
database.py: Acts as database. Contains functions to add, update, and retrieve parts from the database.
logger_config.py: Contains the logging configuration.
pc_builder_test.py: Contains unit tests for the methods in pcpart.py.
main.py: Entry point of the application.
Setup and Execution
Clone the repository or download the source code.
Install Python if not already installed.
Navigate to the project directory in terminal/command prompt.
To run the unit tests, execute the following command: python pc_builder_test.py.
To run the application, execute the following command: python main.py.

