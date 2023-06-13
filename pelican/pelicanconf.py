#!/usr/bin/env python
# -*- coding: utf-8 -*- #



# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None



import os,sys
# DOCs: https://docs.getpelican.com/en/latest/settings.html
# $ pip install ghp-import pelican pelican-liquid-tags typogrify
# $ pelican-quickstart
# $ git submodule add git@github.com:getpelican/pelican.git pelican
# $ git submodule add git@github.com:getpelican/pelican-themes.git themes
# $ git submodule add git@github.com:getpelican/pelican-plugins.git plugins
# $ git clone git://github.com/danielfrg/pelican-ipynb.git plugins/ipynb
PLCDIR=os.path.dirname(os.path.abspath(__file__))
PLUGIN_PATHS = [os.path.join(PLCDIR, 'plugins')]
PLUGINS = ['assets', 'sitemap', 'gravatar', 'tag_cloud']
# use global independently installed PYPI package: "pelican-liquid-tags",
# which of import path "pelican.plugins.liquid_tags": 
PLUGINS +=['pelican.plugins.liquid_tags',
           'pelican.plugins.liquid_tags.img',
           'pelican.plugins.liquid_tags.video',
           'pelican.plugins.liquid_tags.include_code',
           'pelican.plugins.liquid_tags.notebook',
           ]
THEME = 'themes/notebook'
PATH = 'content'

DEFAULT_LANG = 'en'
TIMEZONE = 'Asia/Shanghai'
AUTHOR = 'Abael He<abaelhe@icloud.com>'
SITENAME = "Abael He's Site"
SITEURL = 'https://abaelhe.github.io'

#Jupyter Notebook Integration
MARKUP = ("md",) 
NOTEBOOK_DIR='docs' # see "pelican.plugins.liquid_tags"/notebook.py
IGNORE_FILES = [".ipynb_checkpoints"]
IPYNB_USE_METACELL = True
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
SOCIAL = (
        ('Github', 'https://github.com/abaelhe'),
          )

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

