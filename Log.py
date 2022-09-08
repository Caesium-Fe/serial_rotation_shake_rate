import logging
import datetime
import os


class Log(object):
    fmt = "%(asctime)s - %(name)s - %(filename)s - Line:%(lineno)d - %(levelname)s - %(message)s"
    datafmt = "%Y-%m-%d %H:%M:%S"
    log_name = datetime.datetime.now()

    logger = logging.getLogger('SerialPort')
    logger.setLevel(logging.DEBUG)

    log_dir = "./Report_Log"
    if os.path.exists(log_dir):
        pass
    else:
        os.mkdir(log_dir)

    logfile = logging.FileHandler("./Report_Log/port_serial " + log_name.strftime("%Y%m%d_%H%M%S") + '.log', encoding='utf-8')
    logfile.setLevel(logging.DEBUG)
    logfile.setFormatter(logging.Formatter(fmt, datafmt))

    logger.addHandler(logfile)


if __name__ == '__main__':
    Log.logger.info('www')
