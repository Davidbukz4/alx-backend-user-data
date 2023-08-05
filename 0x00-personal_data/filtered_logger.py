#!/usr/bin/env python3
'''
Handling Personal Data
'''
import re
from typing import List
import logging
from os import environ
import mysql.connector
PII_FIELDS = ('name', 'email', 'phone', 'ssn', 'password')


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    ''' Regex-ing '''
    for field in fields:
        message = re.sub(f'{field}=.*?{separator}',
                         f'{field}={redaction}{separator}', message)
    return message


class RedactingFormatter(logging.Formatter):
    """
    Redacting Formatter class
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        ''' filters values using filter_datum method '''
        record.msg = filter_datum(self.fields, self.REDACTION,
                                  record.getMessage(), self.SEPARATOR)
        return super(RedactingFormatter, self).format(record)


def get_logger() -> logging.Logger:
    ''' create logger object '''
    logger = logging.getLogger('user_data')
    logger.setLevel(logging.INFO)
    logger.propagate = False

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(RedactingFormatter(list(PII_FIELDS)))
    logger.addHandler(stream_handler)
    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    ''' Connect to secure database '''
    host = environ.get('PERSONAL_DATA_DB_HOST')
    user = environ.get('PERSONAL_DATA_DB_USERNAME')
    password = environ.get('PERSONAL_DATA_DB_PASSWORD')
    db = environ.get('PERSONAL_DATA_DB_NAME')
    cur = mysql.connector.connection.MySQLConnection(host=host,
                                                     user=user,
                                                     password=password,
                                                     database=db)
    return cur
