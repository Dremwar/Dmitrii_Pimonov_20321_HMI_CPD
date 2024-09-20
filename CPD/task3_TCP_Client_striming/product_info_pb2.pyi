from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Message(_message.Message):
    __slots__ = ["device_id", "event_id", "humidity", "temp_cel", "video_data"]
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    HUMIDITY_FIELD_NUMBER: _ClassVar[int]
    TEMP_CEL_FIELD_NUMBER: _ClassVar[int]
    VIDEO_DATA_FIELD_NUMBER: _ClassVar[int]
    device_id: int
    event_id: int
    humidity: float
    temp_cel: float
    video_data: bytes
    def __init__(self, device_id: _Optional[int] = ..., event_id: _Optional[int] = ..., humidity: _Optional[float] = ..., temp_cel: _Optional[float] = ..., video_data: _Optional[bytes] = ...) -> None: ...
