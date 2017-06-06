# cuscript.py

## Authors

#### Isaac DeMello, Junior, Computer Science

#### Jie Zhou, Senior, Electrical Engineering

#### Wendy Chong, Senior, Computer Engineering

## Table of Contents

* [Purpose](#purpose)
* [Installation](#installation)
* [Run](#run)

## Purpose

cuscript is a python 3.6.1 script designed to scrape information from various Hawaii credit union website. The script scrapes the following information from each credit union: 

* Branch Name
* Number of Branches
* Address
* Phone #
* Assets
* Loans
* Net Worth
* Number of Members
* Number of Full Time Employees
* Number of Part Time Employees 

## Installation

*note: current version is only mac compatible, Linux and Windows compatibility to be implemented soon*

This script requires python 3 to run, if this is not installed on your machine install [here](https://www.python.org/downloads/)

To install the lxml module go into the terminal and type:
   
```pip3 install lxml```

To install the lxml module globally append sudo to the beginning of the command as follows:

```sudo pip3 install lxml```

Next install the requests module. This is done by typing the following command into the terminal:

```pip3 install requests```

Once both modules are installed clone or download this script into the desired directory.

## Run

To run the script enter the directory and type the following command:

```python3 cuscript.py```

The script will then traverse the pages pulling the afforementioned information.

The information will be stored in a file called CreditUnionData.csv

This file can be opened in excel for easy viewing.




