# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Turck fischerTechnik'
copyright = '2023, Martijn Bakker'
author = 'Martijn Bakker (Mail@Martijn-Bakker.com)'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'piccolo_theme'
html_static_path = ['_static']
html_css_files = ["Root.css"]

html_logo = './_static/Logo.jpg'


#html_theme_options = {
#    "banner_text": 'this site is not yet finished, not all information is present or (completely) correct!',
#    "banner_hiding": "temporary"
#}