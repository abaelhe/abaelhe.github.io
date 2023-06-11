#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'Abael He<abaelhe@icloud.com>'
SITENAME = "Abael He's Site"
SITEURL = 'https://blog.bits.army'
THEME = 'pelican-themes/pelican-elegant'

PATH = 'content'

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None


#Jupyter Notebook Integration
# pip install pelican pelican-jupyter
MARKUP = ("md", "ipynb")
from pelican_jupyter import markup as nb_markup
PLUGINS = [nb_markup]
IGNORE_FILES = [".ipynb_checkpoints"]
IPYNB_SKIP_CSS=True


# Blogroll
LINKS = (('CMake', 'https://cmake.org/cmake/help/latest'),
         ('Python', 'https://docs.python.org/3'),
         ('Swift', 'https://www.swift.org'),
         ('LLVM', 'https://llvm.org/docs'),
         ('C++', 'https://en.cppreference.com/w'),
         ('Qt', 'https://doc.qt.io/qtforpython'),
         ('NumPy', 'https://numpy.org/doc/stable'),
         ('Pandas', 'https://pandas.pydata.org/docs'),
         ('Scikit-learn', 'https://scikit-learn.org/stable'),
         ('Matplotlib', 'https://matplotlib.org/stable'),
         ('Tensorflow', 'https://tensorflow.google.cn'),
         ('Tensorflow/US', 'https://tensorflow.google.com'),
         ('LaTeX', 'https://tug.org/texlive/doc/texlive-en/texlive-en.html'),
         ('Kaggle', 'https://www.kaggle.com'),
         ('ACM', 'https://dl.acm.org/doi/10.1145/2835857.2835860'),
         ('Science', 'https://www.science.org'),
         ('Nature', 'https://www.nature.org/en-us'),
         ('Statistic', 'https://seeing-theory.brown.edu'),
         ('Dev@Apple', 'https://developer.apple.com'),
         ('Dev@Android', 'https://developer.android.com'),
         ('Dev@IBM', 'https://developer.ibm.com'),
         )

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
        ('Github', 'https://github.com/abaelhe'),
          )

DEFAULT_PAGINATION = 50

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

