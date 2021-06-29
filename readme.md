# Weathercache

Weathercache is a simple flask app that fetches the weather in Portland and can serve cached results for up to 5 minutes. The Vagrantfile is currently only written to support Microsoft Hyper-V as the VM host provider. If you'd like to use a different provider, there are commented lines in ```Vagrantfile``` you can use to change this. 

To get started, you just need an openweathermap API key. You can get one here:
https://openweathermap.org/api. Once you have that, create a file at ```./weathercache/secrets.py``` with a line containg the key, as follows:

    openweatherkey = "<Put your key here>"

You can deploy the app using vagrant and puppet, by running the following command:

    vagrant up --provision

The Flask app listens on port 80 on the virtual machine's IP address, which can be observed in the output of vagrant up, so you will most likely be connecting to the machine over a virtual switch on you hyper-v host. 

Most application logic is in ```./weathercache/__init__.py```, except for database setup and connection management, which happen in ```./weathercache/db.py```
The database schema is defined in ```./weathercache/schema.sql```. If the database schema needs to be updated or changed, run ```flask init-db ``` while the in /vagrant on the vm, or from the application folder, if you already have flask 2.0 installed.
