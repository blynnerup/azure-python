# azure-python
Trying out python with Azure

Use virtual environments when doing Python development -> `py -m venv .venv`

Useful tutorial:\
https://www.youtube.com/watch?v=I-kodc4bs4I \
https://www.youtube.com/watch?v=7tEx8C6iW2I \
https://www.youtube.com/watch?v=MF-nvoTUouk

Useful guide regarding Cosmos:
[Comsmos DB](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference-python?tabs=asgi%2Capplication-level&pivots=python-mode-decorators#development-options) \
Guide for SignalR and Python: [SignalR and Python](https://learn.microsoft.com/en-us/azure/azure-signalr/signalr-quickstart-azure-functions-python)\
https://stackoverflow.com/questions/66364050/azure-signal-r-and-azure-function-python\

Go to guide atm:\
https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-signalr-service-trigger?tabs=isolated-process%2Cnodejs-v4&pivots=programming-language-python

Use requirements.txt for python packages, then run `pip install -r requirements.txt` to install packages. Use `pip list` to get a full list of all modules installed.

## Creating functions in the function app 
In order to create functions in Python we use decorators. In order to have functions outside the main file use [Blueprints](https://learn.microsoft.com/en-us/azure/azure-signalr/signalr-quickstart-azure-functions-python).