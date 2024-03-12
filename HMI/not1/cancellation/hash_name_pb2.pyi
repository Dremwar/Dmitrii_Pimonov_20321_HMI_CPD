from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class HashNameRequest(_message.Message):
    __slots__ = ("desired_name", "ideal_hamming_distance", "interesting_hamming_distance")
    DESIRED_NAME_FIELD_NUMBER: _ClassVar[int]
    IDEAL_HAMMING_DISTANCE_FIELD_NUMBER: _ClassVar[int]
    INTERESTING_HAMMING_DISTANCE_FIELD_NUMBER: _ClassVar[int]
    desired_name: str
    ideal_hamming_distance: int
    interesting_hamming_distance: int
    def __init__(self, desired_name: _Optional[str] = ..., ideal_hamming_distance: _Optional[int] = ..., interesting_hamming_distance: _Optional[int] = ...) -> None: ...

class HashNameResponse(_message.Message):
    __slots__ = ("secret", "hashed_name", "hamming_distance")
    SECRET_FIELD_NUMBER: _ClassVar[int]
    HASHED_NAME_FIELD_NUMBER: _ClassVar[int]
    HAMMING_DISTANCE_FIELD_NUMBER: _ClassVar[int]
    secret: str
    hashed_name: str
    hamming_distance: int
    def __init__(self, secret: _Optional[str] = ..., hashed_name: _Optional[str] = ..., hamming_distance: _Optional[int] = ...) -> None: ...
