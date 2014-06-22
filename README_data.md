General guidelines
==================

* Don't version data.
* To avoid excess sharing of processed data (which changes often), it is preferable to share raw data and the scripts and notebooks that transform *raw* into *processed*.  
* Contents of any *raw* folder should never be modified or deleted.  This way, your script will create the same output as everyone else's script.


Personal directories
--------------------
/data/username/projectname
* Example: /data/projectname


Shell scripts
-------------
Will set variables to direct certain input/output from/to personal and production directories.

Example 1:  Inside a shell script

    DATA=$DATA/projectname

Shell variables
---------------
### The `DATA` variable points to the top-level data location

Example 1: On server, in your `.bashrc`

    export DATA=/data

Example 2: On laptop, in your `.bashrc`

    export DATA=$HOME/servername/data


Source code scheme
==================

Locations
---------
Each user maintains his own sourcecode somewhere in $HOME.

Example 1 (Clone repo on the server)

    git clone https://github.com/jrl-labs/jrl_utils.git  $HOME/lib/jrl_utils

Example 2 (Develop locally and copy)

    scp -r  ~/lib/my-local-repo  servername:~/lib/my-remote-copy

Example 3 (Develop locally, copy diff, print progress, don't copy the repo)
(Make sure to use the trailing slash)

    rsync -az --progress --exclude=".git"  ~/lib/my-local-repo/  servername:~/lib/my-remote-copy/

Example 4 (set an alias in .bashrc to send every repo to server)

    alias syncrepos='rsync -az --progress --exclude=".git" ~/lib/ servername:~/lib/'

Shell variables
---------------
Add your sourcecode directory to your PYTHONPATH

    export PYTHONPATH=$HOME/lib

For each repo, add a shell variable pointing to the repo directory.  It should be an ALL CAPS version of the repo name.

    export TEXT_LEARN=$HOME/Text_Learn

Note:  You can always use aliases or other shell variables to make short names or other links.


Configuration files
-------------------
Keep configuration files in the repo under REPONAME/conf/.
* Version files before using them in a production run
* Keep a personal copy that you do not version (e.g. features_ian.conf)


Transferring files
==================

Using the internets
-------------------
On your laptop, tar the directory, split it into chunks of size 50MB, then rsync the (many many) files to the server's `raw-archives` directory:

    tar -czvf - mydir | split --bytes=50M - mydir.tar.gz.split_
    rsync -a --progress mydir.tar.gz.split_*  servername:/data/raw-archives/

On your server, reconstruct the directory

    cat mydir.tar.gz.split_* | tar -xzvf -




