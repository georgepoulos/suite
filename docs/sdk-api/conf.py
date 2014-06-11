# -*- coding: utf-8 -*-
#
# GXP documentation build configuration file, created by
# sphinx-quickstart on Mon Jul 20 20:19:58 2009.
#
# This file is execfile()d with the current directory set to its containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys, os, string
from xml.dom import minidom

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#sys.path.append(os.path.abspath('.'))

# -- General configuration -----------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = ['sphinx.ext.intersphinx', 'sphinx.ext.todo', 'sphinx.ext.coverage', 'sphinx.ext.autodoc', 'sphinx.ext.viewcode']

# Add any paths that contain templates here, relative to this directory.
#templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'Boundless SDK API'
copyright = u' 2014 Boundless'

# The default replacements for |version| and |release|, also used in various
# other places throughout the built documents.
#
# The short X.Y version.
version = minidom.parse(
        "../pom.xml"
    ).getElementsByTagName(
        "parent"
    )[0].getElementsByTagName(
        "version"
    )[0].firstChild.nodeValue

# The full version, including alpha/beta/rc tags.
release = version

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# List of documents that shouldn't be included in the build.
#unused_docs = []

# List of directories, relative to source directory, that shouldn't be searched
# for source files.
exclude_trees = ['_build']

# The reST default role (used for this markup: `text`) to use for all documents.
#default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []


# -- Options for HTML output ---------------------------------------------------

# The style sheet to use for HTML and HTML Help pages. A file of that name
# must exist either in Sphinx' static/ path, or in one of the custom paths
# given in html_static_path.
html_style = 'css/theme.css'

# The theme to use for HTML and HTML Help pages.  Major themes that come with
# Sphinx are currently 'default' and 'sphinxdoc'.
html_theme = 'suite_rtd_theme'

# Add any paths that contain custom themes here, relative to this directory.
html_theme_path = ["../themes"]

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
html_theme_options = {
  #'sticky_navigation' : True  # Set to False to disable the sticky nav while scrolling.
  'is_community': True, # Community Docs flag for Suite component docs
  'display_zendesk': True, # Display link to report doc bugs to Suite Zendesk
  'display_version': True,  # Whether to show version number
  'suite_url': 'sdk-api' # the url path within Suite e.g. sdk-api for opengeo-docs/sdk-api
}

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
html_title = 'Boundless SDK v%s' % (version,)

# A shorter title for the navigation bar.  Default is the same as html_title.
html_short_title = "Boundless SDK"

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
#html_logo = None

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
html_favicon = '../themes/suite_rtd_theme/static/img/boundlesssdk.ico'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
#html_static_path = ['_static']

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
#html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
#html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
html_use_modindex = False

# If false, no index is generated.
html_use_index = False

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, the reST sources are included in the HTML build as _sources/<name>.
html_copy_source = True

# If true, links to the reST sources are added to the pages.
html_show_sourcelink = False

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# If nonempty, this is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = ''

# Output file base name for HTML help builder.
htmlhelp_basename = 'SDKdoc'


# -- Options for LaTeX output --------------------------------------------------

# The paper size ('letter' or 'a4').
#latex_paper_size = 'letter'

# The font size ('10pt', '11pt' or '12pt').
#latex_font_size = '10pt'

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
latex_documents = [
  ('index', 'BoundlessSDK.tex', u'Boundless SDK Documentation',
   u'Boundless', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#latex_use_parts = False

# Additional stuff for the LaTeX preamble.
#latex_preamble = ''

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_use_modindex = True

latex_preamble = """


\\usepackage{ifthen}
\\setlength\\fboxsep{0pt}
\\setlength\\fboxrule{1pt}

\\let\\OLDincludegraphics\\includegraphics
\\newlength{\\somewidth}
\\renewcommand{\\includegraphics}[1]{
  \\settowidth{\\somewidth}{\\OLDincludegraphics{#1}}
  \\ifthenelse{\\lengthtest{\\somewidth>4in}}{
    \\shadowbox{\\OLDincludegraphics[width=4in]{#1}}}{
    \\shadowbox{\\OLDincludegraphics{#1}}}
}

\\usepackage{float}

\\let\\origfigure=\\figure
\\renewenvironment{figure}[6]{
  \\origfigure[H]}
{\\endlist}


\setcounter{secnumdepth}{3}
\setcounter{tocdepth}{2}

"""


# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {'http://docs.python.org/': None}
intersphinx_mapping = {'http://suite.opengeo.org/opengeo-docs/geoexplorer/': None}
intersphinx_mapping = {'http://suite.opengeo.org/opengeo-docs/geoserver/': None}
intersphinx_mapping = {'http://suite.opengeo.org/opengeo-docs/geowebcache/': None}
intersphinx_mapping = {'http://suite.opengeo.org/opengeo-docs/postgis/': None}
intersphinx_mapping = {'http://suite.opengeo.org/opengeo-docs/sdk-api/': None}
