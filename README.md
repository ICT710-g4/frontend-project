
# Front-end project

This repository hosts the frontend components for Motion Detection project in **ICT710: Software Design for Embedded Systems**, which is developed by **Narusorn Srivaro(Crizyntch)** and **Menghorng Bun (Menghorng96)**.

## System Description


### Overview

This component receive query data from PostgreSQL database API via GET method, and display the movement status of each edge devices in a simple HTML page. The frontend HTML page is updated in real time via SSE and Javascript. This repository is Heroku deployable with Procfile and requirements.txt included.

### Heroku

This project is currently hosted on Heroku cloud server which can be accessed via this link
- URL: https://taist2020-motion-detection.herokuapp.com/

### Flask

The frontend use Flask as a lightweight python framework. It handles the routing and SSE pushing of the system.


### Web Interface

The interface is implemented using HTML and JavaScripts. HTML is used for general formatting of the page, while JavaScripts handle real time SSE and display the informations.

### API

Query: ``
- `devide_id` is brah brah
- `type` is brah brah
- `limit` is brah brah

Payload
- example: ``

## Test-case

Frontend-TC-001

Description: Frontend page can issue POST request and recieve POST response from API server

Test Procedure:

1. access the webpage
2. read and note the device status
3. send POST request for device status to API server via Postman
4. confirm the reading with the webpage

Test Data/Device: API POST response

Expected Result: Webpage have the same response as Postman method

## Prerequsite

1. python
2. falsk
3. library1

## Installation

compile `git clone https://github.com/ICT710-g4/frontent-project.git`

- for download this repo

## Getting Started

`$ cd frontent-project`

- connect to directory frontent-project

`$ pip install -r requirements.txt`

- explain

`$ export FLASK_APP=app.py`

- explain

`$ flask run`

- explain

## Deploy to Heroku

`$ git push heroku:master`

- explain

---


