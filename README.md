# pyGlialo
our solution to spread the goodies


### How to use
#### this use Python 3 and Flask

_(tested on Python 3.4+ and flask 0.10+)_

 1. checkout the project, if you want to contribute use the `flask` branch

 1. Create a file named `secrets.py` with the string `meetup_api_key` inside, use this to assign
[your personal api key from meetup](https://secure.meetup.com/it/meetup_api/key/),  
it should look like something like this (31 char long, this one is fake):```meetup_api_key = '781a5b2c2d7e332f803f325625361e9'```

 1. Install `flask` using either `pip3` or `venv`

To run the application use  

`python3 flask_pyGlialo.py`

###Branches
 - master: stable branch (I hope so :P)
 - flask: branch for the latest development, if you want to contribute this is the one for you
 - winners: for uploading the file generated by pyGlialo during the actual MeetUp
 - readme: for update this readme

### Bad Things
__Next MeetUp__
Right now the meetUp id is hardcoded in `get_event_id()` (still hardcoded) 

### Credits
- the Python Milano logo is found [here](https://github.com/PythonMilano/logo)
- winning banana is from [clker](http://www.clker.com/clipart-52027.html)
- sad banana is from [DeviantArt user rollingjennyh](http://rollingjennyh.deviantart.com/art/Sad-Banana-352394110)
