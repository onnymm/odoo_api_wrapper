import requests
from typing import Any
from typing import Generic
from typing import Literal
from typing import Optional
from typing import Sequence
from ._config import CONFIG
from ._typing import CriteriaStructure
from ._typing import Many2One
from ._typing import MatchingStringOperator
from ._typing import ModelName
from ._typing import ScalarOrSequence
from ._typing import _M
from ._typing import JSONParams
from ._utils import to_list

class OdooAPIWrapper(Generic[_M]):
    _HEADERS = {
        'Authorization': f'bearer {CONFIG.API_KEY}',
        'X-Odoo-Database': CONFIG.DATABASE,
        'User-Agent': 'mysoftware ' + requests.utils.default_user_agent(),
    }

    def create(
        self,
        model_name: ModelName[_M],
        vals_list: ScalarOrSequence[dict],
    ) -> list[int]:

        # Conversión a lista
        vals_list = to_list(vals_list)

        return self._post(
            model_name,
            'create',
            {
                'vals_list': vals_list,
            },
        )

    def search(
        self,
        model_name: ModelName[_M],
        search_criteria: CriteriaStructure = [],
        offset: Optional[int] = None,
        limit: Optional[int] = None,
    ) -> list[int]:

        return self._post(
            model_name,
            'search',
            {
                'domain': search_criteria,
                'offset': offset,
                'limit': limit,
            },
        )

    def search_count(
        self,
        model_name: ModelName[_M],
        search_criteria: CriteriaStructure = [],
    ) -> int:

        return self._post(
            model_name,
            'search_count',
            {
                'domain': search_criteria,
            },
        )

    def name_search(
        self,
        model_name: ModelName[_M],
        name: str,
        search_criteria: CriteriaStructure = [],
        limit: Optional[int] = None,
        operator: Optional[MatchingStringOperator] = 'ilike',
    ) -> list[Many2One]:

        return self._post(
            model_name,
            'name_search',
            {
                'domain': search_criteria,
                'name': name,
                'limit': limit,
                'operator': operator,
            },
        )

    def read(
        self,
        model_name: ModelName[_M],
        ids: ScalarOrSequence[int],
        fields: list[str] = [],
    ) -> None:

        # Conversión a lista
        ids = to_list(ids)

        return self._post(
            model_name,
            'read',
            {
                'ids': ids,
                'fields': fields,
            },
        )

    def search_read(
        self,
        model_name: ModelName[_M],
        search_criteria: CriteriaStructure = [],
        fields: Sequence[str] = [],
        order: Optional[str] = None,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
    ) -> list[dict]:

        return self._post(
            model_name,
            'search_read',
            {
                'domain': search_criteria,
                'fields': fields,
                'offset': offset,
                'limit': limit,
                'order': order,
            },
        )

    def write(
        self,
        model_name: ModelName[_M],
        ids: ScalarOrSequence[int],
        vals: dict,
    ) -> Literal[True]:

        # Conversión a lista
        ids = to_list(ids)

        return self._post(
            model_name,
            'write',
            {
                'ids': ids,
                'vals': vals,
            },
        )

    def unlink(
        self,
        model_name: ModelName[_M],
        ids: ScalarOrSequence[int],
    ) -> Literal[True]:

        # Conversión a lista
        ids = to_list(ids)

        return self._post(
            model_name,
            'unlink',
            {
                'ids': ids,
            },
        )

    def action_archive(
        self,
        model_name: ModelName[_M],
        ids: ScalarOrSequence[int],
    ) -> None:

        self._post(
            model_name,
            'action_archive',
            {
                'ids': ids,
            },
        )

    def action_unarchive(
        self,
        model_name: ModelName[_M],
        ids: ScalarOrSequence[int],
    ) -> None:

        return self._post(
            model_name,
            'action_unarchive',
            {
                'ids': ids,
            },
        )

    def get_external_id(
        self,
        model_name: ModelName[_M],
        ids: str,
    ) -> dict[str, str]:

        # Conversión a lista
        ids = to_list(ids)

        return self._post(
            model_name,
            'get_external_id',
            {
                'ids': ids,
            },
        )

    def executed_method(
        self,
        model_name: ModelName[_M],
        method: str,
        kwargs: dict[str, Any],
    ) -> Any:

        return self._post(
            model_name,
            method,
            kwargs,
        )

    def _post(
        self,
        model_name: ModelName[_M],
        method: str,
        json: JSONParams,
    ) -> Any:

        res = requests.post(
            f'{CONFIG.URL}/{model_name}/{method}',
            headers= self._HEADERS,
            json= {
                'context': {'lang': CONFIG.LANG},
                **json,
            }
        )

        res.raise_for_status()

        return res.json()
