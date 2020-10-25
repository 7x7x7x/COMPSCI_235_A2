Name: Michael Kang
UPI: mkan588

If running in PyCharm:
A flask server should be configured with the script target set to: "wsgi.py" and not "app.py"
All dependencies used are stored in the requirements.txt file.
The test configurations must be setup prior to running the pytests, in conftest.py the TEST_DATA_PATH and TEST_DATA_PATH2
must be set to the "tests/data/Data1000Movies.csv" file and "tests/data/" folder respectively if not done so already, in the rare event
that the test data cannot be found then an absolute path should be used. The same applies for 'data_path' and 'data_path2' in __init__.py.

The pytest is configured the same as in the covid website example given, where the user just needs to add a custom pytest configuration
in pycharm to run it.

If running from terminal then the following commands should be executed to create the venv (same as covid web app):

$ cd COMPSCI_235_A2

$ py -3 -m venv venv

$ venv\Scripts\activate

$ pip install -r requirements.txt


Note: A user can log in with the credentials given in the user.csv, and only logged in users are able to write reviews, as the review
box will only be shown if the user is logged in. 3 movie trailer id's have already been added in the trailers.csv file, all other movies
will show the placeholder video.

This website was constructed using the free W3.CSS framework.