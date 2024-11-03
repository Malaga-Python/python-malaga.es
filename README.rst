
Python Málaga Website
#####################

This is the source code of the `Python Málaga website`_, a static website built with `Pelican`_ and hosted on
`GitHub Pages`_. As a Python community, we use Python to build our website.

.. _Python Málaga website: https://www.python-malaga.es/
.. _Pelican: https://getpelican.com/
.. _GitHub Pages: https://pages.github.com/

Installation
============

To install the website locally, you need to have Python 3.12 or higher installed. Then, you can install the required
dependencies with the following command::

    pip install -r requirements.txt

We recommend using a virtual environment to avoid conflicts with other Python projects. You can create a virtual
environment with the following command::

    python -m venv venv

Then, you can activate the virtual environment with the following command::

    source venv/bin/activate

Usage
=====

To build the website, you can use the following command::

    make html

To serve the website locally, you can use the following command::

    make serve

Deployment to GitHub pages is done automatically with a GitHub Action. You can check the GitHub Action configuration in
the `.github/workflows/build.yml` file.

Contributing
============

If you want to contribute to the website, you can fork the repository and create a `pull request`_. We will review your
changes and merge them. We will try to help you if we find any issues with your pull request. We are open to any kind
of contribution, from fixing typos to adding new features.

You can also `open an issue`_ if you find any bug or have any suggestion. For any other question, you can contact us at
`Telegram`_ or `Twitter`_.

.. _pull request: https://github.com/Malaga-Python/python-malaga.es/pulls
.. _open an issue: https://github.com/Malaga-Python/python-malaga.es/issues
.. _Telegram: https://t.me/python_malaga
.. _Twitter: https://twitter.com/python_malaga

License
=======

This project uses these licenses:

* **Theme:** Based on the `pelican-semantic-ui`_ theme by `ellisonleao`_. Without license.
* **Semantic UI:** Licensed under the `MIT License`_.
* **Content:** Licensed under the `Creative Commons Attribution 4.0 International License`_.
* **Social network icons:** Linkedin (from `Material Design Icons`_), Twitter, Telegram, Meetup & Github
  (from `Pixel Perfect`_), Bluesky (from `Rakib Hassan Rahim`_) & Mastodon (from `Us and Up`_).
* **Company logos:** The logos in the "companies" section belong to their respective companies. Python Málaga has
  received permission to use them in this section to promote them. You can request its deletion by `contacting us`_.

.. _pelican-semantic-ui: https://github.com/ellisonleao/pelican-semantic-ui
.. _ellisonleao: https://github.com/ellisonleao/
.. _MIT License: https://opensource.org/licenses/MIT
.. _Creative Commons Attribution 4.0 International License: https://creativecommons.org/licenses/by/4.0/
.. _Material Design Icons: https://materialdesignicons.com/
.. _Pixel Perfect: https://www.flaticon.com/authors/pixel-perfect
.. _Rakib Hassan Rahim: https://www.flaticon.com/authors/rakib-hassan-rahim
.. _Us and Up: https://www.flaticon.com/authors/us-and-up
.. _contacting us: https://t.me/python_malaga
