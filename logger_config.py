

# https://dev.to/wendrewdevelop/gerando-logs-com-python-25k4
import logging
import sys

file_handler = logging.FileHandler(filename='lema_automation.log')
stdout_handler = logging.StreamHandler(sys.stdout)
handlers = [file_handler, stdout_handler]

logging.basicConfig(
    level=logging.DEBUG, 
    format='[%(asctime)s] {%(filename)s:%(lineno)d} %(levelname)s - %(message)s',
    handlers=handlers
)

logger = logging.getLogger('LOGGER_NAME')
