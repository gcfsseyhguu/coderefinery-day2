import os
import sys

sys.path.insert(0, os.path.abspath(".."))

project = "example"

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
]

exclude_patterns = ["_build"]
root_doc = "index"
html_theme = "nature"
