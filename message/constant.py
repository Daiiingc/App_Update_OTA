from dataclasses import dataclass, field

DEFAULT_MAX_SIZE_DATA   = 140
START_BYTE              = 0xA5
DEFAULT_BYTE            = 4
DEFAULT_BYTE_CHECKSUM   = 2
# arr_in = []

from enum import Enum

class OTA_State_E(Enum):
    OTA_STATE_NULL    = 0
    OTA_STATE_START   = 1
    OTA_STATE_DATA    = 2
    OTA_STATE_END     = 3


class Message_Frame_Msg_T:
    Start_Frame: int = 0                               # chứa 1 byte trong mảng
    Type_Message: int = 0                              # chứa 1 byte trong mảng
    Length_Data: int = 0                               # LengthData = Length(Data[] + CheckFrame) chứa 2 bytes
    Data: int = []                                # Data[] mỗi phần tử trong chiếm 1 byte
    Check_Frame: int = 0                               # chứa 2 byte trong mảng 


class Frame_Meta_Data_T:
    cmd: int  = OTA_State_E.OTA_STATE_NULL.value       # chứa 1 byte trong mảng
    package_size: int = 0                              # chứa 4 bytes trong mảng
    package_crc: int  = 0                              # chứa 4 bytes trong mảng
    name: int = []                                # mỗi phần tử chứa 1 bytes

class Frame_Data_T:
    cmd: int     = OTA_State_E.OTA_STATE_NULL.value    # chứa 1 byte trong mảng
    length: int  = 0                                   # chứa 1 byte trong mảng
    offset: int  = 0                                   # chứa 4 bytes trong mảng
    data: int = []                                # mỗi phần tử chứa 1 bytes
