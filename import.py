# Prefer absolute imports to relative imports

## Harmful
from package import other_module

## Idiomatic
import package.other_module
import package.other_module as other


# Do not use * when importing module.

## Harmful
from foo import *

## Idiomatic
from foo import bar, baz, qux, quux, quuux
import foo   # or even better..



# Arrange import statements in a standard order.
# 1. STL Module
# 2. Third-party library modules installed in site-packages
# 3. modules local to the current project

import concurrent.futures
import os.path
import sys
from flask import (Flask, request, session, g, redirect, url_for, abort, render_template, flash, _app_ctx_stack)
import requests
import this_project.utilite.sentinent_network as skynet
import this_project.widgets