# Jupyter Notebook with Cell Auditing

A Jupyter notebook fork with cell auditing capabilities.

Currently, auditing is done using a FileLogger (see `notebook/audit/loggers.py`). 

Notebook cell code and related metadata are logged to `/opt/jupyterhub/logs/audit.log` by default; however, this logging destination can be changed if necessary.

## Installation

The following steps explain how to add cell auditing to an existing JupyterHub installation.

1. Stop (Ctrl-C) your JupyterHub instance from running.
2. Remove your current jupyter notebook installation by running `/opt/jupyterhub/bin/python3 -m pip uninstall jupyter-core`
3. Install the jupyter notebook fork with cell auditing capabilities by downloading the .zip file for the repository and running `/opt/jupyterhub/bin/python3 -m pip install ~/Downloads/notebook-master.zip`
4. Restart your JupyterHub instance.

Notes: You may need to exit out of your old jupyter tabs and clear your browser cookies before restarting.

### Installing from wheel files.

Alternatively, you can install the jupyter notebook fork from wheel files.

1. Clone the repository `git clone git@github.com:mkearns-ccri/notebook.git`
2. 


## How to change the audit log path

coming soon...

## How to change what gets logged

coming soon...

## How to add a different auditor

coming soon...