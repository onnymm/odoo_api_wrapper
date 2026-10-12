from typing import Sequence
from ._typing import ScalarOrSequence
from ._typing import _T

def to_list(item_or_sequence: ScalarOrSequence[_T]) -> list[_T]:
    if isinstance(item_or_sequence, Sequence) and not isinstance(item_or_sequence, dict):
        return list(item_or_sequence)
    else:
        return [item_or_sequence]
