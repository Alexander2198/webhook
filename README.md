# "Information" project in PYTHON ARCHITECTURE API-REST

This is a simple in  **PYTHON** project.The project consist in API REST with python and html.

## Requirements
- you clone this repository git clone https://github.com/Alexander2198/API-REST-E
Once the repository has been cloned, you need to create venv in python, which requires the following steps:
open the project in visual studio, go to the command console and create our venv with the following command:
- python -m venv venv then, if we are using windows, we must execute the following command:
- Set-ExecutionPolicy-Scope Process-ExecutionPolicy Bypass
then, to activate the virtual environment, we must execute
- .\venv\Scripts\activate
install the packages from my requirements.txt with the following command:
- pip install -r requirements.txt
and that's it, we can run our project.
the project consist in the server content some information
Client:

Sends an HTTP POST request with JSON data (e.g. payment details) to a server at http://localhost:5000/webhook.
Server:

Receives the data sent by the client, prints it to the console, and responds with a success message (200 OK).
