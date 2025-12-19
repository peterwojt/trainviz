# Trainviz
Trainviz is a python package for easily visualizing live AI training data in the browser.

![Alt text](example.png)

## Quickstart
First we must install the required dependancies by running 
```bash
bash setup.sh
```

Next we can execute the example by running
```bash
python3 example.py
```
This will start a Trainviz server. We can view it by navigating to ```localhost:8000``` in the browser.

## Usage
Below is a guide to use the Trainviz python package with your AI training tech stack. First, install the python package by running
```bash
pip install trainviz
```
Import the package by running 
```bash
import trainviz as tv
``` 
To initialize the server run 
```bash
tv.start()
``` 
You can begin updating values on the website by running 
```bash
tv.update_value("loss", loss_value)
```

View full documentation  
[here](https://peterwojt.github.io/trainviz/)  
