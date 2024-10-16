Travel Application using Django Framework and Python

Standard Travel Template downloaded from website is used in the Project.
manage.py file manage the project files.
In this Project, we have the main Project directory(Master Branch) which control the whole project settings.
A Project is created, with addition apps seperately, so that it does not interfer with the main Project.
if we want to edit or update or delete a particular operation , it would be easy if we manage everything seperately .
Linking the apps with the main Project is done using manage.py with the files like views.py, urls.py.

Data Migration is managed by the migrations.py files. Using ORM features in Django Framework. It becomes easy for migration of files.
As there is no need to use SQL Query , it is done automatically by ORM.

Security is maintained in Django Framework. Where the default UI for user /admin authetication is done by Framework.

In the Template the Login , Register are done through the Framework.
We use the API POST to save the details in database(during Register).


Two Apps are created. Travel_APP AND Account_APP are integrated with Master Branch(Project).

Master Branch - Is the main Project , where the full project navigation urls , views are set. In settings.py ,where the full Project STATIC  , DYNAMIC actions and new Apps to the project are integrated here.

Travel_App - Travel application build in Django Framework using python, Static data  with Dynamic change of the travel desination,
its price , picture are done . Data is fetched from Mysql Database 

Templates - HTML files of the Project

Account_App - User Login , Register workflow is in Account_APP

Media_Files_APP - jPEG folder




                
