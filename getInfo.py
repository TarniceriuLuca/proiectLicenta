import platform, psutil, shutil, time, cpuinfo, os, datetime



total, used, free = shutil.disk_usage("/")

# print("Disk Used: %d GiB" % (used // (2**30)))

def updateInfo():
    # values reprezent in order: memory%, cpu%, cpu frequency, last reboot time, platform, cpuBrand, memCap, diskSize
    return (
            '[' +
            str(psutil.virtual_memory().percent) + ',' +
            str(psutil.cpu_percent()) + ',"' +
            str(datetime.datetime.fromtimestamp(psutil.boot_time())) + '","' +
            str(platform.system()) + '","' +
            str(cpuinfo.get_cpu_info()['brand_raw']) + '","' +
            str(round(psutil.virtual_memory().total / (1024.0 ** 3))) + '","' +
            str(total // (2 ** 30)) + '","' +
            str(used // (2**30)) +
            '"]'
            )
