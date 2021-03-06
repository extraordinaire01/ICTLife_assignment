# ICTLife_assignment
Mini app to track stock prices in the USA

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Python3+ 

```
https://www.python.org/downloads/
```

### Installing

```bash
# clone repo
git pull https://github.com/extraordinaire01/ICTLife_assignment.git
# install virtualenv
pip install virtualenv
# Create vitual env for project
cd to project folder and run
virtualenv ICTLife_assignmentenv
#Activate vitual env
source ICTLife_assignmentenv/bin/activate
# install requirements
pip install -r requirements.txt
# Run google scrap query
python stocktrack.py

# Expected input
aapl
#Expected output
{'name': 'aapl', 'current_price': '241.41 USD'}

#To run second assignment

#Install additional packages inside virtual environment
pip install -r requirements.txt
#From project directory
cd FocusMobileAssignment
#Run second assignment
python stocktrack.py

# Expected input
Enter stock symbol (kindly note only USA Stocks eg aapl or msft) :MSFT
What is your preferred language(leave blank for english-en):pt
What is your preferred currency(leave blank for USD):UGX
#Expected output
O preço atual para MSFT é 621396.1909325599UGX


#To view third assignment

#From project directory
cd systemDesign
#Download file
file name : System design solution - PeterChencha.pdf
```

* [Python3](https://www.python.org/) - Python is a programming language that lets you work quickly
and integrate systems more effectively.
* [Pip](https://pip.pypa.io/en/stable/) - The Python Package Installer
* [Requests](https://requests.readthedocs.io/en/master/) - HTTP for Humans
* [Beautiful Soup](https://requests.readthedocs.io/en/master/) - a Python library for pulling data out of HTML and XML files
