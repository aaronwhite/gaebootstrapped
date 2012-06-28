Welcome to GAE-Bootstrapped
=============

Orientation
-----------

app.yaml: GAE's core app description	

controllers.py: Handles web traffic and translates into business logic
managers.py: Your business logic goes here!
models.py: Define the data-structures you'll be persisting here
settings.py: Application settings should go here

utils.py: Just in case you need to store functions that don't fit elsewhere
filters.py: Just in case you need to add power to your templates, ignore for now
index.yaml: App Engine uses this to make datastore queries fast, ignore for now

- views
	base.html: All pages/layouts derives from this template
	secure.html: Every secured (logged-in) page derives from this template
	index.html: The first thing your visitors will see
	dashboard.html: The first thing logged-in users will see

- static
	- css/style.css: Your custom CSS code goes her
	- js/main.js: Your custom JS code goes here
	- images: Place images you'd like to serve here
	- bootstrap: It's pre-loaded

- libs: Place different 3rd party Python libraries here

Getting started
---------------

First, clone this repository:

	git clone git@github.com:aaronwhite/gaebootstrapped.git

Open GoogleAppEngine Launcher, and in the File menu, choose "Add Existing Application" and select the gaebootstrapped folder.

Next, open the project and do a search on "changethis" to find places you should provide an updated value.

In particular:

 * Update the app name in app.yaml
 * In settings.py, provide a random guid for SECURE_COOKIE
 * In the templates, update the html titles accordingly
 * In base.html, provide a valid Google Analytics profile ID
 
Resources
---------
[App Engine Dashboard](https://appengine.google.com/)

[App Engine Overview and Docs](https://developers.google.com/appengine/docs/python/overview)

[Twitter Bootstrap Documentation](http://twitter.github.com/bootstrap/)