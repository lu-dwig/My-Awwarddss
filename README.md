# My-Awwarddss

[Ludwig-Murimi](https://github.com/lu-dwig)

# Description  
This project allows users to post their projects for other users to rate according to design, usability and content 
##  Live Link  
 Click [View Site]()  to visit the site
  

## User Story  
  
* A user can view posted projects and their details.  
* A user can post a project to be rated/reviewed. 
* A user can rate/ review other users' projects.  
* Search for projects.  
* View projects overall score.
* A user can view their profile page.  
  
## Setup and Installation  
To get the project .......  
  
##### Cloning the repository:  
 ```bash 
  https://github.com/lu-dwig/My-Awwarddss.git 
```
##### Navigate into the folder and install requirements  
 ```bash 
cd My-Awwarddss pip install -r requirements.txt 
```
##### Install and activate Virtual  
 ```bash 
- python3 -m venv virtual - source virtual/bin/activate  
```  
##### Install Dependencies  
 ```bash 
 pip install -r requirements.txt 
```  
 ##### Setup Database  
  SetUp your database User,Password, Host then make migrate  
 ```bash 
python manage.py makemigrations instagram
 ``` 
 Now Migrate  
 ```bash 
 python manage.py migrate 
```
##### Run the application  
 ```bash 
 python manage.py runserver 
``` 
##### Testing the application  
 ```bash 
 python manage.py test 
```
Open the application on your browser `127.0.0.1:8000`. 

### Api Endpoints
 * https://dry-coast-64447.herokuapp.com/api/postList/
 * https://dry-coast-64447.herokuapp.com/api/postDetail/{pk}/
 * https://dry-coast-64447.herokuapp.com/api/postDelete/{pk}/
 * https://dry-coast-64447.herokuapp.com/api/postCreate/
  
## Technology used  
  
* [Python3.9.7](https://www.python.org/)  
* [Django 4.0.5](https://docs.djangoproject.com/en/2.2/)  
* [Heroku](https://heroku.com)  
  

## Known Bugs  
* There are no known bugs currently but pull requests are allowed incase you spot a bug  
  
## Contact Information   
If you have any question or contributions, please email me at [murimiludwig@gmail.com]

## License 

MIT License

Copyright (c) 2022 ludwig murimi

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


  