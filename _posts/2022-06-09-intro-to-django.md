---
layout: post
disqus: n
title: Introduction to Django
---

1. Introduction

Django is a Python Framework that make it easier to create web sites using Python. Django take care of
the difficult stuff so you can concentrate on building
your web applications. Django emphasizes reusability
of components, also refereed to as DRY (Do not repeat yourself) and comes with ready-to-use features like
login system, database connections and CRUD operations.
(Create Read Update Delete). Django is especially helpul for database driven websites.

Django follows the MVT design pattern (Model View Template):
- Model (the data you want to present, usally the data from a database)
- View (a request handler that returns the relevant template and content - based on the request from the user)
- Template (a text file like an HTML file) containing the layout of the web page, with logic on how to display the data.

## Model

The model provides data from the databases.

In Django, the data is delivered as an Object Relational Mapping (ORM)
which is a technique designed to make it easier to work with databases. The most common way to extract data from a database is SQL.
One problem with SQL is that you have to have a pretty good understanding of the database structure to be able to work with it.

Django, with ORM, makes it easier to communicate to the databases,
without to write complex SQL statements.

The models are usually located in a file called models.py

## View

A view is a function or method that takes http requests as arguments, import the relevant models and finds out what data to send to the template and retuns the final result.

## Template

A template is a file where you describe how the result should represented. Templates are often .html files, with HTML code
describing the layout of the webpage, but can also be in other
file formats to present other results, but we will concentrate
on .html files.

```html
<h1>My Homepage</h1>

<p>My name is {{ firstname }}.</p>
```

## URLs

Django also provides a way to navigate around the different pages
in a website.

When a user requests a URL, Django decides what view it will send it to.

This is done in a file called urls.py

## So, what is going on?

When you have installed Django and created you first Django web application, and the browser requests the URL, this is basically
what happens:
