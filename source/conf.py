project = 'RB-DCU i.MX 6UL'
copyright = '2025, PHYTEC'
author = 'PHYTEC'
release = '0.1'

extensions = [
    'sphinx.ext.autodoc',
    # 'myst_parser',  # Enable if using Markdown
]

templates_path = ['_templates']
exclude_patterns = []

html_theme = 'sphinx_rtd_theme'

html_static_path = ['_static']
html_css_files = ['custom.css']

# Optional: for better navigation
html_theme_options = {
    'collapse_navigation': False,
    'navigation_depth': 4,
    'style_external_links': True,
}

# Optional: better handling of raw HTML (like Flask-injected blocks)
rst_prolog = """
.. role:: raw-html(raw)
   :format: html
"""

# Optional: for external image folders
# html_extra_path = ['../images']

