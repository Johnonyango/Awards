# AWARDS
###### By **[JOHN ONYANGO](https://github.com/Johnonyango/Awards)**


## Description
[AWARD]()application allows users to view previous projects of others and post theirs as well


## Setup/Installation Requirements
1. Live site at 
2. Copy  and  Paste the clone button the link on your terminal
3. cd to the clone folder
4. Install requirements e.g:
_*pip install django==1.11 -- to install django _*
_*pip intsall django-bootstrap3._*
5. Run the app on server by command python3.6 manage.py runserver.

## Specifications
1. Users can view different projects posted by others.
2. Users can post their own projects for others to see.
3. Users can rate others' projects
4. Users can edit their bio information.


## Activate virtual environment
Activate virtual environment using python3.6 as the default handler

virtualenv -p /usr/bin/python3.6 venv && source venv/bin/activate

## Create the Database
1. Run psql command
2. CREATE DATABASE award;
3. \c gallery to connect to your database

##Run initial Migration
python3.6 manage.py makemigrations instagram
python3.6 manage.py migrate

# Running Tests
* python3.6 manage.py test

## Run the app
python3.6 manage.py runserver
Open terminal on localhost:8000
copy paste to your preffered browser



## Known Bugs 
LOgout and rating functions still not implemented. Working round the clock tp achieve that.

##BDD
<table>
    <tr>
      <th>Behavior</th> 
      <th>Input</th> 
      <th>Output</th>   
    </tr>
    <tr>
        <td>Enter your name</td>
        <td>['Calvince']</td>
        <td>name = 'calvince'</td>
    </tr>
    <tr>
        <td>Enter Email && Message</td>
        <td>['Email','Message']</td>
        <td>Email && Message</td>
    </tr>
    <tr>
        <td>Submit</td>
        <td>Email && Message</td>
        <td>Thank you Calvince, details received</td>
    </tr>
    <tr>
        <td>Sum of two values<= third value </td>
        <td>[1,2,5]</td>
        <td>No triangle</td>
    </tr>    
</table>

## Technologies & Resources/Tools Used
Technologies used include:
* Python3.6(Django==1.11) 
* HTML
* CSS
* Bootstrap
* Postgres Database
* Heroku - for app hosting live
* Git - for app details


## Contact for support:
For more info or assistance(If there is a bug in my code), please contact:
j.yayah7@gmail.com

## MIT License
Copyright (c) 2019 John Onyango

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Copyright (c) 2019 JOHN ONYANGO