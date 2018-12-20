__version__ = 1.0
import os

class GPU_Info(object):
    """Gets GPU information\n From: https://github.com/Forhad95000/Python-GPU-benchmark"""

    def Get_GPU_Info(info_type):
        """Sends request to system for GPU information\n
           info_type values:\n
           name: Gets GPU name\n
           description: Gets GPU description\n
           driverversion: Gets GPU driver version\n
           adapterram: Gets adapter RAM information\n
           pnpdeviceid: Gets PNP device ID
           """
        Type = info_type

        command = "wmic PATH Win32_videocontroller GET" + " " + Type
        os.system(command)