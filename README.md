# Senior Project - Olive Ripeness Detection

## Advisor: Dr. Akhan Almagambetov
## Group 38

1. Nurbol Bizhigit
2. [Smagulkassym Arslanov](https://www.linkedin.com/in/smagulkassym/)
3. Akmal Shadiyev
3. Alisher Dunenov
4. Sarvar Khavazmatov

## Description

The "Olive Ripeness Detection System" is a comprehensive project that integrates both hardware and software components to automate the process of determining the ripeness of olives. This system is designed to address the challenges of labor shortages and the need for specialized expertise in the olive industry, particularly in the Mediterranean region.

The hardware components of the system include an Adafruit Sharp Memory display with a resolution of 400x240 for visual output, an A9G GPS/GPRS module for location tracking and data transmission, and a Nodemcu 1.0 or ESP32 Dev Module for controlling the system. The system also includes a custom-built "Olivometer" sensor, which uses a 74hc595 shift register, an Adafruit ADS1115 ADC, and various diodes, photosensors, resistors, and transistors to measure the ripeness of the olives.

On the software side, the system uses Python as the primary programming language. Image processing is handled by OpenCV, a powerful open-source library for computer vision tasks. The machine learning component, which classifies the olives based on their ripeness, is built using TensorFlow, a popular library for developing and training ML models.

The project is managed and version-controlled using Git and GitHub, which allows for efficient collaboration among team members and ensures that changes to the codebase are tracked and managed effectively.

## Stack of Technologies 

### Hardware

 - Adafruit Sharp Memory display 400x240
 - A9G GPS/GPRS module
 - Nodemcu 1.0 or ESP32 Dev Module
 - Olivometer sensor:
     - 74hc595 shift register
     - Adafruit ADS1115 ADC
     - Diods, photosensors, resistors, and transistors

### Backend

 - Python 3.9.13
 - Flask 3.0.3
 - SQLAlchemy 2.0.29

### Algorithm

 - OpenCV 4.8.0.74
 - Ultralitics 8.2.2

### Frontend

 - HTML5
 - JavaScript
 - Google Heatmap API
 - Google Maps API

## Installation

### `Step 1:` Install Python3
### `Step 2:` Install Pip3
### `Step 3:` Install Flask
```
    pip3 install Flask
```
### `Step 4:` Install SQLAlchemy
```
    pip3 install sqlalchemy
```
### `Step 5:` Install OpenCV
```
    pip3 install ultralitics
```
### `Step 6:` Run the project
```
    python3 main.py
```