from father.app_pkg import app
import sys
from father.config import flags


if __name__ == "__main__":
    flags = sys.argv
    # app.run(host='0.0.0.0')
    app.run()
