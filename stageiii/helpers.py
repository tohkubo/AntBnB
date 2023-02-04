import datetime
import itertools


class Counter:
    engine = itertools.count(1)
    @classmethod
    def get_id(cls) -> int:
        return next(cls.engine)

def format_date(date: datetime.date) -> str:
    month = f' {date.month}' if date.month <= 9 else f'{date.month}'
    day = f' {date.day}' if date.day <= 9 else f'{date.day}'
    return f'{month}/{day}/{date.year}'

def parse_date(date: str) -> datetime.date:
    # fmt = '%m/%d/%Y'
    m, d, y = map(int, date.split('/'))
    return datetime.date(year=y, month=m, day=d)
