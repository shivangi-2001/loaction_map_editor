# Layout Designer 

## Introduction

Welcome to the Layout Designer! This is used to design the Map of the warehouse, here you can create the different type of zones for your warehouse on the map and able to edit it.

## Requirements

Before you can run the application, you need to have the following libraries installed:

PySide2: PySide2 is a Python binding for the Qt library that provides a set of Python bindings for the Qt GUI and application framework.

SQLite3: SQLite3 is a software library that provides a relational database management system. It is used to store the data used by the Fleet Tracking System.

cv2: cv2 is a Python library for computer vision.

yaml: yaml is a human-readable data serialization format.

other libraries are numpy, random, string, math, sys etc.

## Getting started

To use the Picture Editor, you will need to have the following installed on your computer and follow the guildines:

## Guildlines

1. To create the new Map for layout_designer you need to go Menu bar Menu> File> New Layout (Ctrl + N)
2. To Edit on the Saved Worked layout_designer map you go Menu>File>Edit Layout (ctrl + O)
3. To zoom in and zoom out go to Menu>View>Zoom in/Zoom out
4. To remove the previous steps undo button Menu>Edit>undo
5. To Rotate the loaded map you have to go Menu>Edit>Rotate , the get the prefect angle with horizontal bar and click on rotate button to save the rotated map.
6. To Crop the map you have to go Menu>Edit>crop and get the ratio (size:width,height) using mouse and click on the crop button.
7. To remove the unnecessary black part on the map you go to Menu>View>clean map , first select the area using mouse and click the clean map from menubar. 

## File structure
The repository contains the following files:

starting_screen.py: This is the main file that sets up the GUI and implements the functions for visualizing data. The code in this file sets up the main window of the application and connects the various elements of the user interface to the functions that visualize the data. 

layout_deisgner.py: This file contains the code for GUI page for layout deisgner which have the feature connected.

login_application.py: This file contains the code for the login page of the application.

database.db : This is the SQLite database containing the data used by the application. The data in this database is used to store the all coordinates of different shapes in the Layout Designer. 

Various .ui files: These are the Qt Designer files used to generate the user interface code. Qt Designer is a tool for designing and building graphical user interfaces (GUIs) with the Qt application framework. 


## Conclusion

The Layout Designer is a comprehensive solution for managing and monitoring a fleet of vehicles. It provides a user-friendly interface and able to edit previous saved map and also able to genrates images. If you are in need of a layout designer, consider using this solution as a starting point for your project.
