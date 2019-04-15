Winzog
---

This is a first stab at client code for Windows - to send information to ServiceNow as part of a laptop registration flow.

This is written in Python 3. You will need to install

* [Python 3](https://www.python.org/downloads/windows/)
* [Git for Windows](https://git-scm.com/download/win)

And actually work out how to get these things to play nicely together.

All of a sudden I can see why Devs love Mac and Linux... :)

### Getting started...

You'll want to setup a virtualenv - from PowerShell run

    python -m venv env

And to _activate_ that virtualenv

     .\venv\Scripts\Activate.ps1

now you can install some python requirements

    pip install -r requirements.txt