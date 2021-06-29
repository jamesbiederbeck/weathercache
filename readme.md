# Weathercache

A simple flask app that fetches the weather in portland with caching.

To deploy the app using vagrant and puppet, run

    vagrant up --provision

Flask app listens on port 80 in vm and exposed on the host machine port 80 using vagrant

Most application logic is in ./weathercache/__init__.py.
The database schema is defined in schema.sql. If the database schema needs to be updated or changed, run 

    flask init-db 
    
while in /vagrant on the vm, or from the folder on a system with flask 2.0.1 installed.
