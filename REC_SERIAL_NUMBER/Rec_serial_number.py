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


from Utils.Commands import *


def main():
    start_time = datetime.now()
    main_logger.info("SCRIPT Started")
    Rec_ser_num()
    main_logger.info("SCRIPT Ended")
    main_logger.info("Time elapsed: {}\n".format(datetime.now() - start_time))
    main_logger.info("LOG FILE Path: " + logfile_dir)
    main_logger.info("RECORD File: " + rec_book)


if __name__ == "__main__":
    main()

