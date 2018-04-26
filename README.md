README
======

**weeklyrev** is a pymol script which simplifies the task of
going every week looking for new hits of interesting research
in the main journals a researcher is interested in following.

For now the code is in a refactoring stage.

Setup & Installation
--------------------

1. Clone the repository

        git clone https://github.com/esguerra/weeklyrev.git


2. Install the python feedparser library

        pip install feedparser

 
Usage
-----

To run the program just call it from the prompt:

    bash-4.0$ ./weeklyrev.py


This will go to the list of news feeds you're following
and it will parse the xml files looking at the description
field and then it will parse the keywords you're interested in.

Enjoy,


The dev.
