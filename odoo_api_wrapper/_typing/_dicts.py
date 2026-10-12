from typing import Optional
from typing import TypedDict
from ._generics import ScalarOrSequence
from ._criteria_structure import CriteriaStructure
from ._literals import MatchingStringOperator

class JSONParams(TypedDict):
    domain: CriteriaStructure
    fields: ScalarOrSequence[str]
    ids: ScalarOrSequence[int]
    limit: Optional[int]
    name: str
    offset: Optional[int]
    order: Optional[str]
    vals: dict
    vals_list: ScalarOrSequence[dict]
    operator: MatchingStringOperator
