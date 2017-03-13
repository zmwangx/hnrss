import os
import sys

HERE = os.path.dirname(__file__)
VENVLIB = os.path.join(HERE, 'venv/lib/python2.7/site-packages')
sys.path.insert(0, VENVLIB)
sys.path.insert(0, HERE)

from hnrss import app as application

# Local Variables:
# mode: python
# End:
