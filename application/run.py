from src.app_pkg import app
import sys
from src.config import flags


if __name__ == "__main__":
    flags = sys.argv
    # app.run(host='0.0.0.0')
    app.run()
