# django-firebird-1.4
===============================================

This is a firebird backend implementation for django that enables
Firebird (version 1.5 and later) RDBMS support.

**The current master version just works with Django 1.4.x**

Django 1.5+ support
----------------------------------------------------------

**If you need support for django 1.5 then you must go to**

<https://github.com/maxirobaina/django-firebird>

------------------------------------------------------------------------

For previous django version look at tagged repository versions:

**django 1.2:**
<http://code.google.com/p/django-firebird/source/browse/#svn%2Ftags%2Fdjango-firebird-1.2>

**django 1.3:**
<http://code.google.com/p/django-firebird/source/browse/#svn%2Ftags%2Fdjango-firebird-1.3>

Tested against Firebird 1.5.6, 2.1.x and 2.5.x


Migrations
----------------------------------------

We have a first approach to support migrations using south. Check it out
at <https://bitbucket.org/maxirobaina/south>

**Update 2012-03-13:** south with firebird support is now part of
original project. <https://bitbucket.org/andrewgodwin/south>


Installation
--------------------------------------------

Prerequisites

1.  KInterbasDB package (<http://www.firebirdsql.org/en/python-driver/>)
2.  Get django 1.4 (<http://www.djangoproject.com/download/>)

-   Or install using pip:

> ` pip install django==1.4 `

Go ahead… Check out the latest development version anonymously with:

> \$ svn checkout http://django-firebird.googlecode.com/svn/trunk/django-firebird
