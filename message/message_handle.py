import constant
import struct
import File_Size

def UpdateFile_CreateFrameMetaData(cmd, size, crc, arr_name, data_out):
    # tạo struct cho FrameMetaData
    meta_data_temp = constant.Frame_Meta_Data_T()
    
    meta_data_temp.cmd = cmd
    meta_data_temp.package_size = size
    meta_data_temp.package_crc = crc
    memcopy(meta_data_temp.name, arr_name, len(arr_name))

    # truyền struct của MetaData vào trong mảng
    # truyền cmd
    data_out.append(meta_data_temp.cmd)     

    # truyền package_size
    data_len = struct.pack('I',meta_data_temp.package_size)
    data_out.append(data_len[0])
    data_out.append(data_len[1])
    data_out.append(data_len[2])
    data_out.append(data_len[3])

    #truyền package_crc
    data_len = struct.pack('I',meta_data_temp.package_crc)
    data_out.append(data_len[0])
    data_out.append(data_len[1])
    data_out.append(data_len[2])
    data_out.append(data_len[3])

    # truyền mảng name
    for i in range(0,len(arr_name)):
        data_out.append(ord(meta_data_temp.name[i]))

    return len(data_out)

def UpdateFile_CreateFrameData(cmd, length, offset, arr_data, data_out):
    del data_out[:]
    # tạo struct cho FrameData
    data_temp = constant.Frame_Data_T()
    data_temp.cmd = cmd
    data_temp.length = length
    data_temp.offset = offset
    memcopy(data_temp.data, arr_data, len(arr_data))

    del data_out[:]
    # truyền struct của FrameData vào trong mảng
    # truyền cmd
    data_out.append(data_temp.cmd)

    # truyền length
    data_out.append(data_temp.length)
    
    # truyền offset
    data_len = struct.pack('I',data_temp.offset)
    data_out.append(data_len[0])
    data_out.append(data_len[1])
    data_out.append(data_len[2])
    data_out.append(data_len[3])

    # truyền mảng data
    for i in range(0,len(arr_data)):
        data_out.append(data_temp.data[i])

    return len(data_out)

def memcopy(arr_copy, arr_in, length):
    del arr_copy[:]
    for i in range(0, length):
        arr_copy.append(arr_in[i])

# data = [1,2,34,234,534,2,4,756]
# arr_out = []
# length = UpdateFile_CreateFrameData(constant.OTA_State_E.OTA_STATE_DATA.value,10,10,data, arr_out)
# print(length)
# print(arr_out)