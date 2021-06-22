#!/usr/bin/env python3
# -*- coding: utf8 -*-

from view import View
from programmer import Programmer

import threading


def main():
    """Main function for the project.
    """

    # global threadLock

    # threadLock = threading.Lock()

    # Call Programmer class.
    # configure = Programmer()

    # Call View() and Programmer() classes.
    gui = View(Programmer())

    # Call method to read the config file.
    # read_config = configure.read_config()

    # Call method to create the GUI.
    # create_gui = gui.create_gui()

if __name__ == "__main__":
    main()
