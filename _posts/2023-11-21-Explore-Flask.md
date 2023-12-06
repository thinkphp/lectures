---
layout: post
disqus: y
title: Let's explore Flask
---

Let's install Flask

```
$ sudo -H python3 -m pip install flask
```

Flask provides a collection of modules that help you build server-side web applications. It’s technically a micro web framework, in that it provides the minimum set of technologies needed for this task. This means Flask is not as feature-full as some of its competitors—such as Django, the mother of all Python web frameworks—but it is small, lightweight, and easy to use. As our requirements aren’t heavy (we only have two web pages), Flask is more
than enough web framework for us at this time.

Check that Flask is installed and working:

Here’s the code for the most basic of Flask webapps, which we are going to use to test that Flask is set up and ready to go. Use your favorite text editor to create a new file, and type the code shown below into the file, saving it is as hello_flask.py (you can save the file in its own folder, too, if you like—we called our folder webapp):

```
from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello() -> str:
return 'Hello world from Flask!'
app.run()
```
