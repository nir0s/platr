# -*- coding: utf-8 -*-
#
# Configuration file for Sphinx builds, created by
# sphinx-quickstart on Wed Mar  2 11:33:06 2016.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import os
import sys

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
sys.path.insert(0, os.path.abspath(".."))

import distro  # noqa: E402

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
needs_sphinx = "1.1"

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.intersphinx",
    "sphinx.ext.todo",
    "sphinx.ext.coverage",
    "sphinx.ext.viewcode",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
# source_suffix = ['.rst', '.md']
source_suffix = ".rst"

# The encoding of source files.
source_encoding = "utf-8"

# The master toctree document.
on_rtd = os.environ.get("READTHEDOCS", None) == "True"
if on_rtd:
    master_doc = "index"
else:
    master_doc = "docs/index"

# General information about the project.
project = u"distro"
copyright = u"2015,2016, Nir Cohen, Andreas Maier"
author = u"Nir Cohen, Andreas Maier"

# The short description of the package.
_short_description = u"Linux Distribution - a Linux OS platform information API"

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.

# The short X.Y version.
# Note: We use the full version in both cases.
version = distro.__version__

# The full version, including alpha/beta/rc tags.
release = version

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ["tests", ".tox", ".git", "build_docs", "ld.egg-info"]

# If true, '()' will be appended to :func: etc. cross-reference text.
add_function_parentheses = True

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.
# See http://www.sphinx-doc.org/en/stable/theming.html for built-in themes.
html_theme = "classic"

# Theme options are theme-specific and customize the look and feel of a theme
# further.
# See http://www.sphinx-doc.org/en/stable/theming.html for the options
# available for built-in themes.
html_theme_options = {}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["html_static"]

# Add any extra paths that contain custom files (such as robots.txt or
# .htaccess) here, relative to this directory. These files are copied
# directly to the root of the documentation.
html_extra_path = ["html_extra"]

# Output file base name for HTML help builder.
htmlhelp_basename = "distro_doc"

# -- Options for intersphinx extension ------------------------------------
# For documentation, see
# http://www.sphinx-doc.org/en/stable/ext/intersphinx.html

# Defines the prefixes for intersphinx links and the targets they resolve to.
# Use Python 3.7 as that is the last version to include
# platform.linux_distribution() and platform.dist(). Example RST source for
# 'py' prefix:
#     :py:func:`platform.dist`
intersphinx_mapping = {"py": ("https://docs.python.org/3.7", None)}

intersphinx_cache_limit = 5
