# MOZMOSDataInterpreter
An interactive GUI for loading and analysing data collected from the MOZMOS Data Collection Module

## Legal
MOZMOS Data Interpreter, and accompanying software, documentation and files are products of the MOZMOS Entity, and the legal property of such. Any illicit use, such as pirating, cracking or otherwise unpermissed use of the software is illegal under copyright law and the EULA.

## Current Features
* Load data straight from SD Card into the program
* Filter the displayed data between each type, as well as toggle between each one

## Latest Update - Version 0.1.2
* Created algorithm to generate graphs based on data
    * _Uses time as the x-axis, and the actual data points for the y-axis_
* Embedded the graph into the TKinter software, so it will be manipulatable.
* Graph algorithm automatically discerns between data types, and will colour and label each line accordingly
* General Bug Fixes

## Future Features
- [] Settings Menu
    - [] _Change colours_
    - [] _Change graph colours_
    - [] _Change graph type_
    - [] _Disability/Inclusivity Settings_
        - [] _Audio sounds for buttons and text_
    - [] _Change Language_
- [x] Graph Creation (Framework built, just need to include
- [] Convert graph into image for exportation
- [] Visually appealing interface
    - [] _Backgrounds_
    - [] _Colours_
    - [] _Styles_
    

## Update List
#### Version 0.1.1
* Created the main GUI page
* Created the algorithm to import the file, and backup systems in case something goes wrong with the import (including if something goes wrong)
* Created stub buttons for data filtering
* Created algorithm to read the data, and filter out any excess data so it can be cleanly split into groups of 4 (1 array position per data), and added these groups into a multi-dimensional array

#### Version 0.1.2
* Created algorithm to generate graphs based on data
    * _Uses time as the x-axis, and the actual data points for the y-axis_
* Embedded the graph into the TKinter software, so it will be manipulatable.
* Graph algorithm automatically discerns between data types, and will colour and label each line accordingly
* General Bug Fixes
