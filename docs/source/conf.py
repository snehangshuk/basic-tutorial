# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Some Project'
copyright = '2025, Snehangshu'
author = 'Snehangshu'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx_termynal',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

html_css_files = [
    'css/custom.css',
    'css/termynal.css',
]

html_js_files = [
    'js/custom.js',
    'js/termynal.js',
]

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'
