# Entry point for the application.
from . import app    # For application discovery by the 'flask' command.
from . import views  # For import side-effects of setting up routes.
from hello_app.routes import test
from . import backend
