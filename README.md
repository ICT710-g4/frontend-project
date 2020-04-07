
# Front-end project

This repository hosts the frontend components for Motion Detection project in **ICT710: Software Design for Embedded Systems**, which is developed by **Narusorn Srivaro(Crizyntch)** and **Menghorng Bun (Menghorng96)**.

## System Description


### Overview

This component receive query data from the database API through GET method, and display the movement status of each edge devices in a simple HTML page. The frontend HTML page is updated in real time automatically via SSE and Javascript. This repository is Heroku deployable with Procfile and requirements.txt included.

### Heroku

This project is currently hosted on Heroku cloud server which can be accessed via this link
- URL: https://taist2020-motion-detection.herokuapp.com/

### Flask

The frontend use Flask as a lightweight python framework. It handles the routing and SSE pushing of the system.


### Web Interface

The interface is implemented using HTML and JavaScripts. HTML is used for general formatting of the page, while JavaScripts handle real time SSE and display the informations.


