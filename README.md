# Project_AutoScout24


Module Project(AutoScout24 Application)
General Info
This project will be an Autoscout24 Application with a graphical
user interface. When the program starts, it will gather data of
BMW, MERCEDES, TOYOTA vehicles between 2018-2022 from the
website https://www.autoscout24.nl/. The gathering data will be
saved in a database. When the user selects one of the Brand-Model
data in the Interface, the official data of the Brand-model, KM,
price, year, province, car will be displayed on the same screen via
the graphical interface.There should be a search box where you
can search for licence plates and the user should be able to type the
licence plate in this field, then All vehicle information history
should be automatically searched on the website and the results
should be displayed on web browser.
When any vehicle is selected from the application, it will display 3-
day weather information of the vehicle's location.
Tools:
• Object Oriented Programming (OOP) and Graphical User
Interface (GUI) will be used in the project.
• PyQT5 will be used as GUI
• Scrapy will be used as Web Scrapping Tool.
• Selenium will be used as Plate search
• HTTP-Request and API will be used.
• PostgreSQL will be used as DBMS.
Each team will have 1 mentor.
GitHub will be used in the project.
There will be a 30 minutes meeting with teammates every day.
The content of the daily meeting is generally as follows:

1. What each person did
2. The general direction in the project
3. Task sharing until tomorrow
   A meeting will be held with the mentor on the specified dates
   Each person in the team will tell about the part he did to the
   mentor in the meeting. After each meeting, the mentor will
   make an assessment of whether each team member is
   working or not.
   After the project is completed, an online project presentation will
   be made.
   Meeting Schedule
4. Online Kick-off Meeting - 04/07/2022
5. Online Mentor Meeting - 06/07/2022
6. Online Mentor Meeting - 11/07/2022
7. Online Final Presentation - 13/07/2022
   Steps
   Suggestion:
   -Step 1 can be done together in the group.
   -Step 2, 3, and 4 can be done in parallel. Group members can share
   tasks.
   Step 1:
   • Design GUI for Autoscout App
   o Consider Web Scrapping Data Visualisation
   o Consider Web API Data Visualisation
   o Consider Plate search Visualization
   • UML Design (Making Plan)
   o You can use this tool to draw
   https://app.diagrams.net/
   o Use Case Diagram
   o Class Diagram
   • Design ERD for the current version of the Program. Add DB
   for the current version of the Program according to the ERD
   design. All information should be ordered and stored in DB No
   more file usage.
   Step 2:
   This project will be an Autoscout24 Application with a graphical
   user interface. When the program starts, it will pull data of BMW,
   MERCEDES, TOYOTA vehicles between 2018-2022 from the
   website https://www.autoscout24.nl/.
   a-Data will be gathered with SCRAPY.
   b-[Brand-model, KM, Plate, price, year, Image, state of residence]
   data will be retrieved
   It will show the data in the database in the table with the help of a
   start button.
   a-User can see how many data there are.
   b- When we click start button it will be displayed Brand Model,
   Plate, Year Information shown as a Grid view.
   c-When we select one of the Brand-Model data. Brand-model, KM,
   price, year, province, official data of the auto
   will display on the same screen via the graphical interface.
   There should be a search box.
8. User can search for license plates. When you type the license
   plate in this field.
   2.User should be selected where plate information from the Grid
   table.
   https://www.centraalbeheer.nl/verzekeringen/autoverzekeri
   ng/kentekencheck
   automatically search the website with the help of Selenium and
   show results on the Chrome Driver.
   All information should be ordered and stored in DB
   Step 3:
   • HTTP-Request and API will be used to pull real-time and
   two days weather forecast information from the website.
   • When the program is opened for the first time,
   Amsterdam's 3-day weather conditions will be shown with
   weather conditions icons, max and min temperatures will
   be shown on the GUI.
   • When any vehicle is selected from the table, it will show
   the 3-day weather conditions, max and min temperatures
   of the place where the vehicle is located on the GUI.
   Weather information of the selected cities is taken from
   https://openweathermap.org/api site.(You can choose other
   web sites)
   The icons and how to use the icons are explained in detail on the
   site given below, https://openweathermap.org/weatherconditions
   Step 4:
   Program Main page will contain the following components.
   • Total Count of Auto’s
   • Start Button
   • Plate Search
   • The Label which is shown of the City’s weather information.
   • 3-days weather conditions, max and min temperatures of the
   place where the vehicle is located
   • Auto Information Grid
   o Brand-model,
   o Plate,
   o Year.
   • When we select one of the Brand-Model data,
   o Brand-model,
   o KM,
   o price,
   o year,
   o city,
   o Image of the Auto.
   Step 5:
   Final presentation
   Bonus:
   GitHub Usage Requirements
   • Each team will have a GitHub repository and each team
   member will be added as a collaborator.
   • All tasks should be created as an issue on the issues page.
   • Each team member will get assigned issues.
   • Master will be protected. Branches and pull requests will be
   used for development.
   Database Deploying Free Hereko PostgreSQL(cloud)
   • Project Database can be deployed on cloud such as Heroku
   PostgreSQL
   • You can find detail information via this link:
   https://towardsdatascience.com/how-to-deploy-a-postgresdatabase-
   for-free-95cf1d8387bf...
