# octo

Running the Project
=====================================
This example is designed to run in Google AppEngine, so there are a couple
of steps to get it running. You can download the Google AppEngine Python
development environment at http://code.google.com/appengine/downloads.html.

1. Link or copy the tornado code directory into this directory:

   ln -s ../../tornado tornado

   AppEngine doesn't use the Python modules installed on this machine.
   You need to have the 'tornado' module copied or linked for AppEngine
   to find it.

3. Install and run dev_appserver

   If you don't already have the App Engine SDK, download it from
   http://code.google.com/appengine/downloads.html

   To start the tornado demo, run the dev server on this directory:

   dev_appserver.py .

4. Visit http://localhost:8080/ in your browser

   If you sign in as an administrator, you will be able to create and
   edit blog posts. If you sign in as anybody else, you will only see
   the existing blog posts.


If you want to deploy the blog in production:

1. Register a new appengine application and put its id in app.yaml

   First register a new application at http://appengine.google.com/.
   Then edit app.yaml in this directory and change the "application"
   setting from "tornado-appenginge" to your new application id.

2. Deploy to App Engine

   If you registered an application id, you can now upload your new
   Tornado blog by running this command:

   appcfg update .

   After that, visit application_id.appspot.com, where application_id
   is the application you registered.

