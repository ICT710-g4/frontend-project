
# Front-end project

This repository hosts the frontend components for the Motion Detection project in **ICT710: Software Design for Embedded Systems**, which is developed by **Narusorn Srivaro(Crizyntch)** and **Menghorng Bun (Menghorng96)**.

## System Description


### Overview

This component receives query data from PostgreSQL database API via GET method and displays the movement status of each edge device in a simple HTML page. The frontend HTML page is updated in real-time via SSE and Javascript. This repository is Heroku deployable with Procfile and requirements.txt included.

### Heroku

This project is currently hosted on Heroku cloud server which can be accessed via this link
- URL: https://taist2020-motion-detection.herokuapp.com/

### Flask

The frontend use Flask as a lightweight python framework. It handles the routing and SSE pushing of the system.


### Web Interface

The interface is implemented using HTML and JavaScripts. HTML is used for the general formatting of the page, while JavaScripts handle real-time SSE and display the information.

## Prerequisite

1. Python 3.7
2. Flask Library

## Installation

compile `git clone https://github.com/ICT710-g4/frontent-project.git`
no further installation is required for hosting on the local device
for Heroku deployment, please read here
- https://devcenter.heroku.com/categories/deployment

## Getting Started

`$ cd frontent-project`\
`$ pip install -r requirements.txt`\
`$ export FLASK_APP=app.py`\
`$ flask run`
- running port can be configured in app.py
