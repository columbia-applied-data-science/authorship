General guidelines
==================

* Don't version data.
* Avoid excess sharing of processed data (which changes often) by sharing raw
  data and the scripts and notebooks that transform the raw data into processed
  data.

Data Scheme
-----------

Somewhere on your computer you should have a 'data' folder. On mine it is
located at '/home/thomas/Projects/declass/data'. Set an environment variable
called 'DATA' pointing to the base data directory. For example, I might add the
line 'export DATA=/home/thomas/Projects/declass/data' to my .bashrc file. Set
an environment variable called 'ME' to use to differentiate your data in your
scripts from others. For example, I might put 'export ME=thomas' in my .bashrc
file.

When working on a project I call 'authorship_federalist', I would use the
following directory structure:

```
data/
└── thomas/
    └── authorship_federalist/
        ├── processed/
        └── raw/
```

Contents of any raw/ folder should never be modified or deleted. This way,
your script will create the same output as everyone else's script.

Example
-------

To enforce this data scheme, the top of a script might start with the following
lines:

```
>>> import os

>>> DATA = os.environ['DATA']
>>> ME = 'thomas'
>>> MYDATA = os.path.join(DATA, ME, 'authorship_federalist')
>>> PROCESSED = os.path.join(MYDATA, 'processed')
>>> RAW = os.path.join(MYDATA, 'raw')

>>> for directory in [RAW, PROCESSED]:
>>>     try:
>>>         os.makedirs(directory)
>>>     except OSError: # In case directory already exists.
>>>         pass
```
