import logging

from src.configurations import settings


def update_logger() -> None:
    for name in logging.root.manager.loggerDict:
        log = logging.getLogger(name)
        log.handlers = []
        log.propagate = True


logging_config = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "%(levelname)s | %(asctime)s | %(name)s:%(lineno)s | %(funcName)s() | %(message)s"
        }
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "verbose",
            "stream": "ext://sys.stdout",
        },
    },
    "root": {"handlers": ["console"]},
}


def init_logging():
    update_logger()
    logging.config.dictConfig(logging_config)
    root_logger = logging.getLogger()
    root_logger.setLevel(settings.log_level)
