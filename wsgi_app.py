import sys
sys.path.append('/srv/http/')

from fileserve import fileserve
application = fileserve.create_app()
