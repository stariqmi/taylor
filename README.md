# Taylor-Scraper

This is a two part program.

## Part A
**Python Script**, utilizes the **selenium** module and needs to be run on a GUI like Windows or Ubuntu. It creates a **TCP Socket** connection with a remote or local **NodJS** server. This script only interacts with the form, helping in the extraction of the URL that contains the relevant data.

The command to run this script is **python2.7 main.py**. The **NodeJS** server needs to be running before starting this script.

## Part B
**NodeJS** TCP server, excepts remote or local TCP connections. This server script listens for the **data**, which is in the form of
**ADDRESS<=>URL**. It uses the npm **request** module to extract the relevant HTML and then uses the **cheerio** module to extract the required information. The result of each data received from the **Python TCP connection** is of the following format in **JSON**:


- **query**: The address used as a query,
- **name**: Owner's name,
- **address**: Owner's address,
- **state**: State,
- **zip**: zipcode 

