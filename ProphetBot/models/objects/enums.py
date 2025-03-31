from enum import Enum


class QueryResultType(Enum):
    single = "Single"
    multiple = "Multiple"
    scalar = "Scalar"
    none = "None"