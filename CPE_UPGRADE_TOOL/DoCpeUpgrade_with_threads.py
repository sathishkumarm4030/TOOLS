#!/usr/bin/env python

"""
This Tool is designed for upgrading Versa CPE.
"""

__author__ = "Sathishkumar murugesan"
__copyright__ = "Copyright(c) 2018 Colt Technologies india pvt ltd."
__credits__ = ["Danny Pinto"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Sathishkumar Murugesan"
__email__ = "Sathishkumar.Murugesan@colt.net"
__status__ = "Developed"


from Utils.Commands_with_threads import *



def main():
    main_logger.info("Result Stored in " + logfile_dir + "/RESULT.csv")
    main_logger.info("LOG FILES Path: " + logfile_dir)


if __name__ == "__main__":
    main()
