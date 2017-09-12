This Django project is for the CS5600 class for Missouri S&T. Homeworks should be separated as seen through the branches. Python 3.x.x is required to run the project.

On a clean computer, free of python, first download Python 3.x.x from https://www.python.org/
Make sure to add Python to path when installing. After installation, check if python 3.x.x was successfully installed.
Open your command line or terminal and check you python version: "python -V"  or  "python3 -V"
Knowing which python call return a 3.x.x is key. Take note if "python" or "python3" returns a 3.x.x python version.

Now to install (dependencies) and run the server.
On a terminal/command line, use "pip install Django" if your python call is "python"  or  "pip3 install Django" if your python call is "python3"

Once Django is installed, you need to add you ipaddress to "settings.py" under Website-CS5600/CS5600/CS5600/settings.py
Add you ipaddress inside the ALLOWED_HOST container.

Once your ipaddress is contained inside the ALLOWED_HOST container, you can start the server.
To start the server, navigate to Website-CS5600/CS5600/
Here, you can find manage.py
To run the file, on the terminal/command line, run this line: 

python manage.py runserver ipaddress:port
or
python3 manage.py runserver ipaddress:port


**NOTE: change <ipaddress> to your ipaddress (also visible in ALLOWED_HOST) and <port> to a desired port (a typical HTTP port is 8080)


When ran, you should see something like:

Performing system checks...

System check identified no issues (0 silenced).
September 11, 2017 - 23:04:49
Django version 1.11.4, using settings 'CS5600.settings'
Starting development server at http://ipaddress:port/
Quit the server with CTRL-BREAK.


Since the server is running, we can checkout the website.
Navigate your browser to "ipaddress:port" i.e. "127.0.0.1:8080"
HW1 can be seen at: "ipaddress:port/hw1" i.e. "127.0.0.1:8080/hw1"

You can see that the the tags are the same when the same page is reloaded, hence, the persistent HTTP connection
