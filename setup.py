import os
from setuptools import setup, find_packages
from firebird import VERSION

file_name = os.path.join('firebird', 'README')

f = open(file_name)
try:
    readme = f.read()
finally:
    f.close()

# Provided as an attribute, so you can append to these instead
# of replicating them:
standard_exclude = ('*.py', '*.pyc', '*$py.class', '*~', '.*', '*.bak')
standard_exclude_directories = ('.*', 'CVS', '_darcs', './build',
                                        './dist', 'EGG-INFO', '*.egg-info')

setup(
    name='django-firebird',
    version=".".join(map(str, VERSION)),
    description='Firebird backend for Django 1.4+.',
    long_description=readme,
    author='Maximiliano Robaina',
    author_email='maxirobaina@gmail.com',
    url='http://code.google.com/p/django-firebird/',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Databases',
        'Topic :: Internet :: WWW/HTTP',
    ],
    zip_safe=False,
    install_requires=[],
)



