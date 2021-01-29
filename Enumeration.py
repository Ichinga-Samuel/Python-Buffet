import enum
import bisect
from datetime import timedelta


class Days(enum.Enum):
    Sunday = 1
    Monday = 2
    Tuesday = 3

    def worship(self):
        if self is Days.Sunday:
            print(f'{self.name} is a day of worship')
        else:
            print(f"We Worship God {self.name}'s too")


class Grades(enum.IntEnum):

    A = 70
    B = 65
    C = 55
    D = 45
    E = 40
    F = 0

    @classmethod
    def score(cls, mark):
        scores = [i.value for i in reversed(Grades)]
        grades = [i.name for i in reversed(Grades)]
        g = bisect.bisect(scores, mark)
        return grades[g-1]

# class Colors(enum.IntFlag)
d = Days(2)


class Ordinal(enum.Enum):
    North = enum.auto()
    East = enum.auto()
    South = enum.auto()
    West = enum.auto()

    def _generate_next_value_(self, start, count, last_values):
        return start + 90


