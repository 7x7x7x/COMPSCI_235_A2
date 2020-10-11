A flask server should be configured with the script target set to: "wsgi.py" and not "app.py"
All dependencies used are stored in the requirements.txt file.
The test configurations must be setup prior to running the pytests, in conftest.py the TEST_DATA_PATH and TEST_DATA_PATH2
must be set to the  "tests/data/Data1000Movies.csv" file and "tests/data/Data" folder respectively.

The pytest is configured the same as in the covid website example given, where the user just needs to add a custom pytest configuration
in pycharm to run it.

Note: A user can log in with the credentials given in the user.csv, and only logged in users are able to write reviews, as the review
box will only be shown if the user is logged in.