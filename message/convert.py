import struct

# Kết hợp 2 số dạng Bytes thành 1 số dạng Uint16
def Convert_From_Bytes_To_Uint16(data0, data1):
    uint16_value = (data1 << 8) | data0 
    
    return uint16_value

# Chuyển 1 số dạng Uint16 thành 2 số dạng Bytes
def Convert_From_Uint16_To_Bytes(uint16_data):
    uint8_value = []
    uint8_value.append(uint16_data[1])
    uint8_value.append(uint16_data[0])
    return len(uint8_value)

# Chuyển từ dạng Float thành dạng Bytes
def Convert_Float_To_Bytes(float_data):
    byte_value = struct.pack('f', float_data)
    return byte_value

# Chuyển từ dạng bytes thành dạng Float
def Convert_Bytes_To_Float(byte_data_float):
    [float_value] = struct.unpack('f',byte_data_float)
    return float_value