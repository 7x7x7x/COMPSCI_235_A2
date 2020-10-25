Name: Michael Kang
UPI: mkan588

A flask server should be configured with the script target set to: "wsgi.py" and not "app.py"
All dependencies used are stored in the requirements.txt file.
The test configurations must be setup prior to running the pytests, in conftest.py the TEST_DATA_PATH and TEST_DATA_PATH2
must be set to the "tests/data/Data1000Movies.csv" file and "tests/data/" folder respectively if not done so already, in the rare event
that the test data cannot be found then an absolute path should be used.

The pytest is configured the same as in the covid website example given, where the user just needs to add a custom pytest configuration
in pycharm to run it. Make sure the python interpreter in configurations is set to python.exe in venv/Scripts/python.exe 

If running in a terminal window then the following command was used to run pytest:
"venv/Scripts/python -m pytest"

And the following command can be used to run the flask app:
"venv/Scripts/flask.exe run"

users must be in the root directory when executing these commands
alternatively this command can also be run within the pycharm terminal

Note: A user can log in with the credentials given in the user.csv, and only logged in users are able to write reviews, as the review
box will only be shown if the user is logged in. 3 movie trailer id's have already been added in the trailers.csv file, all other movies
will show the placeholder video.

This website was constructed using the free W3.CSS framework.

Alternatively this project can also be downloaded at:
https://mega.nz/file/KOxmRYQT#26PD_MFlvh3qYSxlXmGUDUWs-1kJ9w3-LTIwgbBJodI

md5 checksum: D0C8BE4E4FD957585F9D97A74BAC3296