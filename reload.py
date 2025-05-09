import time
import logging
from hotreload import Loader


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    script = Loader("simulation.py")

    while True:
        # Check if script has been modified since last poll.
        if script.has_changed():
            # Execute a function from script if it has been modified.
            script.main()

        time.sleep(1)