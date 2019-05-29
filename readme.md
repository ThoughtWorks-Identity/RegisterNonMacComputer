RegisterNonMacComputer
---

Has code that will go to either wmic on a windows computer or dmidecode for a linux computer
and get the below information about the laptop:
* Serial Number
* Mac Address
* Model
* Manufacturer

It will then open up the browser pointing to a registration web app. 
The above info is added as query parameters to the URL. 

The code also logs the above info to any log URL provided.   

This is written in Python 3. You will need to install

* [Python 3](https://www.python.org/downloads/windows/)


For Linux there's a separate requirements file - requirements-linux.txt  
For Window there's a separate requirements file - requirements-windows.txt

The code makes use of pyinstaller to package up everything into a binary. 

## Notes:  
The Linux binary needs to sudo privileges to call dmidecode. The binary is meant 
to be executed on the terminal. So you go:

```bash
chmod +x ./RegisterLinuxComputer
./RegisterLinuxComputer
<you will now be prompted for your credentials>
``` 

For Windows, you get an exe that you double click to run.

You need to run pyinstaller on the respective OS to get the binary.   

For Linux,   
there's a docker file which is used for building - LinuxBuildDockerfile. Create an image with 
the Dockerfile and then run ./makeInstaller.sh. Else use the docker image I built for this - 
regsethu/linux-ubuntu-python3:14.04_0.0.4  
You need to build this in the lowest possible Ubuntu version out there for it to work on all
versions of Ubuntu / Debian from 14.04 onwards.

For Windows,  
Run the makeInstaller.bat on Windows. The exe is signed with sign tool with a certificate. 


All of this is running on a pipeline on Azure. 
 
 
Released under the Apache 2 License  
