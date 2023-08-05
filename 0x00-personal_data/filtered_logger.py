#!/usr/bin/env python3
'''
Handling Personal Data
'''
import re
from typing import List


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    ''' Regex-ing '''
    for field in fields:
        message = re.sub(f'{field}=.*?{separator}',
                     f'{field}={redaction}{separator}', message)
    return message
