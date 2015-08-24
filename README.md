# ViewYourData

Welcome to View Your Data project
=======================
<p align="center">
  <img src="https://github.com/LiquidGalaxyLAB/ViewYourData/blob/master/VYD_Project/VYD/static/images/logo_VYD.png">

</p>

View Your Data is a tool that imports data of BigData platforms, and based on them create any presentation data layer to display in the Liquid Galaxy. 
For do it, VYD provides a web application for manage the KML and configure the size of the differents figures and layers created.




Google Summer Of Code
------------
<img src="https://1.bp.blogspot.com/-vIaQK-is11M/VC2kGKZ3udI/AAAAAAAAYzY/aZ63pTa5h6U/s1600/image01.jpg">

This project is developed in a context of a scolarship in the program Google Summer Of Code 2015.

Wiki
------------

We would love your help expanding our [wiki](https://github.com/LiquidGalaxyLAB/ViewYourData/wiki) with more information about learning to code and getting a coding job.

Prerequisites
-------------

- [Pip](https://pypi.python.org/pypi/pip)
- [Python 2.7.9](https://www.python.org/downloads/release/python-279/)

Getting Started
---------------

The easiest way to get started is to clone the repository:

```bash
# Get the latest snapshot
git clone --depth=1 https://github.com/LiquidGalaxyLAB/ViewYourData.git VYD

cd VYD

# Install python
wget https://www.python.org/ftp/python/2.7.9/Python-2.7.9.tgz
tar xfz Python-2.7.9.tgz
cd Python-2.7.9/
./configure --prefix /usr/local/lib/python2.7.9 --enable-ipv6
make
make install

# Install pip
python get-pip.py

# Install requirements
pip install -r requirements.txt

# Execute Setup
sh setup.sh

# Go to the folder of project
cd VYD_Project

# Run Django application
python manage.py runserver

# Open one browser and go to this URL
localhost:8000


```

Software Architecture
-------
<img src="https://github.com/LiquidGalaxyLAB/ViewYourData/blob/master/VYD_Project/VYD/static/images/SoftwareArchitecture.png">

The project is divided into two modules:

<ul style="list-style-type:disc">
  <li>Layer Generator</li>
    <ul style="list-style-type:disc">
      <li>Parser Manager</li>
          <ul style="list-style-type:disc">
            <li>Its responsibility is to download the file, parse it and convert it to standard data</li>
          </ul> 
      <li>Presentation Manager</li>
      <ul style="list-style-type:disc">
            <li>Its responsibility is to display the data and the available presentation models, in order for the user to select the data and match them with the presentation models.</li>
          </ul> 
    </ul> 
  <li>Layer Manager</li>
    <ul style="list-style-type:disc">
            <li>Manager store, display, delete and refresh the layers of liquid Galaxy.</li>
          </ul> 
    </ul> 
</ul> 

Screenshots
-------
<img src="https://github.com/LiquidGalaxyLAB/ViewYourData/blob/master/VYD_Project/VYD/static/images/submit_url.jpg">

License
-------

  View Your Data is a tool that imports data of BigData platforms, and based on
  them create any presentation data layer to display in the Liquid Galaxy.

  Copyright (C) 2015  Marc Solé Farré

  This program is free software: you can redistribute it and/or modify
  it under the terms of the GNU General Public License as published by
  the Free Software Foundation, either version 3 of the License, or
  (at your option) any later version.

  This program is distributed in the hope that it will be useful,
  but WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
  GNU General Public License for more details.

  You should have received a copy of the GNU General Public License
  along with this program.  If not, see <http://www.gnu.org/licenses/>.

  Author contact: [Linkedin](https://www.linkedin.com/pub/marc-sol%C3%A9-farr%C3%A9/6a/55b/9b3) 
  
