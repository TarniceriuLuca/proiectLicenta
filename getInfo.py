import platform, psutil, shutil, time, cpuinfo, os



total, used, free = shutil.disk_usage("/")

# print("Disk Used: %d GiB" % (used // (2**30)))


def systemInfo():
    return (
            "System:" + str(platform.system()) +
            ";cpuBrand:" + str(cpuinfo.get_cpu_info()['brand_raw']) +
            ";memCap:" + str(round(psutil.virtual_memory().total / (1024.0 ** 3))) +
            ";diskSize" + str(total // (2 ** 30)))
def updateInfo():
    # values reprezent in order: memory%, cpu%, cpu frequency, active users
    return (
            '[' +
            str(psutil.virtual_memory().percent) + ',' +
            str(psutil.cpu_percent()) + ']'
            # ";cpuFreq:" + "{:.2f}".format(psutil.cpu_freq().current) +
            # ";users:" + str(psutil.users())
            )
