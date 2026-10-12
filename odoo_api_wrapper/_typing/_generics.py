from typing import Sequence
from typing import Union
from ._type_parameters import _M
from ._type_parameters import _T
from ._literals import PresetModels

ScalarOrSequence = _T | Sequence[_T]
ModelName = Union[PresetModels, _M]
