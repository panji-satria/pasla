#conf.py

# Information
project = 'pasla'
copyright = '2023'
author = 'Panji Satria Taqwa Putra Purnama'

# This is configuration--------------------
# Add any Sphinx extension module
# coming with Sphinx (named 'sphinx.ext.*')
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
]

# Master-------------------------------------
master_doc = 'index'

# Variable------------------------------------
project = 'pasla'
copyright = '2023'
author = 'Panji Satria Taqwa Putra Purnama'

# Theme---------------------------------------
html_theme = 'alabaster'

# Path-theme---------------------------------
html_static_path = ['_static']

# Rest----------------------------------------
html_show_sourcelink = True

# Sphinx-v-----------------------------------
# needs_sphinx='1.0'

# Google-docstring--------------------------
napoleon_google_docstring = True

# Doc-page---------------------------------
viewcode_follow_imported_members = True
