from typing import Literal
from typing import overload

class Many2One:
    @overload
    def __getitem__(
        self,
        i: Literal[0],
    ) -> int:
        ...
    @overload
    def __getitem__(
        self,
        i: Literal[1],
    ) -> str:
        ...
