# See-It Visualizer
## Summary
**See-It** is a visualizer that converts users data to charts. 
Users sign-up to the application and then login.
The users information is stored in the database.
MySQL is used as the database.
The application opens with pop-up window that I created with _**tkinter**_ library.
Tkinter provides a GUI for Python.


You can create 3 types of charts with **See-It** App. 
1. Scatter Chart
2. Bar Chart
3. Pie Chart


## Installation of Required Packages
**requirements.txt** file includes all the required library.
You can download all packages with this `pip install -r requirements.txt` shell script after downloading requirements.txt file.

Required Libraries:
1. **_Numpy_**
2. **_Matplotlib_**
3. **_MySQL Python Connector_**
4. **_Tkinter_**


## How to Run the Application
Firstly you need to install required packages.
Then you can run the python script `See-It.py` on any IDE.
You will see a sign up window. If you have already an account you can click to the login button.

After you login with email and password the upload page will be opened.
You should write a valid path like that: `C:/Users/User/Desktop/file.csv`
Then write columns that you will use its datas with a space. For example: `2 0`.
And finally select a chart type click on the `Create Chart` button.
On chart pop-up you should see save button. 
If you want to download the chart click on the save button and select a type that you want to download.
