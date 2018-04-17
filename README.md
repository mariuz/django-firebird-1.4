# django-firebird #

This is a firebird backend implementation for django that enables Firebird (version 1.4) RDBMS support.

**The current master version just works with Django 1.4.x**


## django 1.5+ support ##

**If you need support for django >1.5.x then you must go to**

https://github.com/maxirobaina/django-firebird

---




For previous django version look at tagged repository versions:

**django 1.2:**
https://github.com/mariuz/django-firebird-1.4/tree/django-firebird-1.2

**django 1.3:**
https://github.com/mariuz/django-firebird-1.4/tree/django-firebird-1.3


Tested against Firebird 1.5.x, 2.1.x and 2.5.x

## Migrations ##
We have a first approach to support migrations using south. Check it out at https://bitbucket.org/maxirobaina/south

**Update 2012-03-13:** south with firebird support is now part of original project.
https://bitbucket.org/andrewgodwin/south



## Installation ##

Prerequisites
  1. KInterbasDB package (http://www.firebirdsql.org/en/python-driver/)
  1. Get django 1.4.x (http://www.djangoproject.com/download/)

  * Or install using pip:

> ` pip install django==1.4.x `

Go ahead...
Check out the latest development version anonymously with:
> `$ git clone git@github.com:mariuz/django-firebird-1.4.git`

Differences from other Django backends

  * TextField. Since large and very large VARCHARs work better than BLOBs with Firebird in most cases where Django uses TextField, Firebird backend uses VARCHAR columns for TextFields and BLOB columns for LargeTextField. For more info see http://www.volny.cz/iprenosil/interbase/ip_ib_strings.htm#_strings_blob_varchar.

  * With Firebird backend TextFields have max\_length and encoding attributes that are ignored by other backends.
 By default, TextFields have max\_length of 10921 (with default UNICODE\_FSS 3-byte charset), 8191 (with optional 4-byte UTF8 charset) or 32765 (with custom 1-byte encoding) -- maximum allowed. If there are multiple TextFields, their size could be adjusted to fit the 64k row limit and warning will be genererated. It's better to set explicit max\_length attribute in this situation.
 If you need to store more text you could use LargeTextField or split your text across multiple rows.

  * Index Limit. 252 bytes with Firebird < 2.0 and 1/4 of page size in later versions. You may need to add encoding="ascii" and/or adjust max\_length of CharFields used as indexes or unique/primary keys to work around these Firebird limitations. Current implementation adjusts these fields automagically and generates warnings during validation process. It's better to adjust these fields manually or switch to Firebird > 2.0 and/or increase the page size.

  * Foreign Key Constraints. FK constraint in Firebird are stricter - no forward references allowed, even inside transactions.


## Usage ##

Copy firebird package where you want. The only one condition is what is in your PYTHONPATH.
This is because since django 1.2 implements a separate compiler module. In this way you don't need put the django-firebird package into django/db/backend folder you just need have this in your python path.


In setting.py

```

DATABASES = {
  'default':  
      'ENGINE' = 'firebird',
      'NAME' = 'path_to_database', # Path to database or db alias
      'USER' = 'SYSDBA',           # Your db user
      'PASSWORD' = 'masterkey',    # db user password
      'HOST' = '127.0.0.1',        # Your host machine
      'PORT' = '3050',             # If is empty, use default 3050
      #'OPTIONS' = {'charset':'ISO8859_1'}  #If is not defined, use default UNICODE_FSS
}

```
