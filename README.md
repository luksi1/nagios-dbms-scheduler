Description
======
A simple Python script to monitor a DBMS Scheduled job in Oracle.

Dependencies
======
Python 2.x
cx_oracle

Notes
=====
- There are two scripts: a python script and a bash wrapper script to set LD_LIBRARY_PATH. You will need to run the bash script, which will, in-turn, call the python script.
- Your DBMS_SCHEDULER job needs to be in the same schema as the user that you are logging in with. In other words, if you create a job in the schema "foo", you need to run this script as the user "foo".
- The scripts, as is, will only work on Linux/Unix systems. You would need to create your own wrapper script for this to work on Windows. 

Author
=====
Luke Simmons

Version
=====
1.0
