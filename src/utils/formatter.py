from datetime import datetime

def format_date(dt: datetime = None, fmt: str = "%Y-%m-%d %H:%M:%S") -> str:
    """
    Formats a datetime object into a string.
    
    :param dt: datetime object (defaults to now if None)
    :param fmt: strftime format string
    :return: formatted date string
    """
    if dt is None:
        dt = datetime.now()
    return dt.strftime(fmt)

def parse_date(date_str: str, fmt: str = "%Y-%m-%d %H:%M:%S") -> datetime:
    """
    Parses a string into a datetime object.
    
    :param date_str: string representation of a date
    :param fmt: strftime format used in the string
    :return: datetime object
    """
    return datetime.strptime(date_str, fmt)
