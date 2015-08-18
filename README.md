# ViewYourData

Welcome to View Your Data project
=======================

View Your Data is a tool that imports data of BigData platforms, and based on them create any presentation data layer to display in the Liquid Galaxy. 
For do it, VYD provides a web application for manage the KML and configure the size of the differents figures and layers created.

Wiki
------------

We would love your help expanding our [wiki](https://github.com/freecodecamp/freecodecamp/wiki) with more information about learning to code and getting a coding job.

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

# Run Django application
python manage.py runserver

```

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
  
