from enum import Enum
from datetime import datetime
from colorama import Fore, Back, Style

class LogLevel(Enum):
    ERROR = 0,
    INFO = 1,
    DEBUG = 2,

class Logger:
    def __init__(self, log_level: LogLevel, log_format = None):
        self.log_level = log_level
        
        if log_format is None: 
            self.log_format = self.default_log_format
        else:
            self.log_format = log_format
    
    def log(self, log_level: LogLevel, message, obj):
        if(self.log_level.value < log_level.value): return

        formatted_log = self.log_format(log_level, message, obj)
        print(formatted_log)

    def default_log_format(self, log_level: LogLevel, message, obj):
        colors = {
            LogLevel.ERROR: Fore.RED,
            LogLevel.INFO: Fore.GREEN,
            LogLevel.DEBUG: Style.DIM
        }
        return f'{colors.get(log_level)}[{datetime.now()}]: "{message}" {Style.RESET_ALL}\n'+\
            f"{obj}"


    def log_error(self, message, obj):
        self.log(LogLevel.ERROR, message, obj)

    def log_info(self, message, obj):
        self.log(LogLevel.INFO, message, obj)

    def log_debug(self, message, obj):
        self.log(LogLevel.DEBUG, message, obj)
