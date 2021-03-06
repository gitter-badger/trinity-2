from typing import Tuple

from eth_typing import (
    Address,
    Hash32,
)


class ExecutionContext:
    _coinbase = None

    _timestamp = None
    _number = None
    _difficulty = None
    _gas_limit = None
    _prev_hashes = None

    def __init__(
            self,
            coinbase: Address,
            timestamp: int,
            block_number: int,
            difficulty: int,
            gas_limit: int,
            prev_hashes: Tuple[Hash32, ...]) -> None:
        self._coinbase = coinbase
        self._timestamp = timestamp
        self._block_number = block_number
        self._difficulty = difficulty
        self._gas_limit = gas_limit
        self._prev_hashes = prev_hashes

    @property
    def coinbase(self) -> Address:
        return self._coinbase

    @property
    def timestamp(self) -> int:
        return self._timestamp

    @property
    def block_number(self) -> int:
        return self._block_number

    @property
    def difficulty(self) -> int:
        return self._difficulty

    @property
    def gas_limit(self) -> int:
        return self._gas_limit

    @property
    def prev_hashes(self) -> Tuple[Hash32, ...]:
        return self._prev_hashes
