from typing import Literal
from typing import Union

_LogicOperator = Literal['&', '|']

ComparisonOperator = Literal[
    '=',
    '!=',
    '>',
    '>=',
    '<',
    '<=',
    '=?',
    '=like',
    'not =like',
    'like',
    'not like',
    'ilike',
    'not ilike',
    '=ilike',
    'not =ilike',
    'in',
    'not in',
    'child of',
    'parent of',
    'any',
    'not any',
    'any!',
    'not any!',
]

_Value = Union[int, float, str, bool] | list[Union[int, float, str, bool]]

_Triplet = tuple[str, ComparisonOperator, _Value]

CriteriaStructure = list[Union[_LogicOperator, _Triplet]]
