#conf.py

#information

project='pasla'
copyright='2023'
author='Panji Satria Taqwa Putra Purnama'

#this is configuration--------------------
#add any Sphinx extension module
#coming with Sphinx (named'sphinx.ext.*')
extensions=[
'sphinx.ext.autodoc', 
'sphinx.ext.napoleon',
'sphinx.ext.viewcode',
]

#master-------------------------------------
master_doc='index'

#variable------------------------------------
project='pasla'
copyright='2023'
author='Panji Satria Taqwa Putra Purnama'

#theme---------------------------------------
html_theme='alabaster'

#path-theme---------------------------------
html_static_path=['_static']

#rest----------------------------------------
html-show_sourcelink = True

#sphinx-v-----------------------------------
#needs_sphinx='1.0'

#google-docstring--------------------------
napoleon_goole_docstring= True

#doc-page---------------------------------
viewcode_follow_imported_members= True
