import constant
import struct
import convert



def Create_Message(type_msg, length, data_in, data_out):
    del data_out[:]
    frame_message_temp = constant.Message_Frame_Msg_T()
    count_length_arr = 0
    # Start_Frame
    frame_message_temp.Start_Frame = constant.START_BYTE
    # Type Message
    frame_message_temp.Type_Message = type_msg
    # Length
    frame_message_temp.Length_Data = length + constant.DEFAULT_BYTE_CHECKSUM
    # Data
    frame_message_temp = list(data_in)

    # Tạo mảng đầu ra cho bản tin
    data_out.append(frame_message_temp.Start_Frame)
    data_out.append(frame_message_temp.Type_Message)
    
    # Gán giá trị của Length_Data vào trong mảng
    data_len = struct.pack('H',frame_message_temp.Length_Data)
    data_out.append(data_len[0])
    data_out.append(data_len[1])
    
    # Gán giá trị của Data vào trong mảng 
    for i in range(0,length):
        data_out.append(frame_message_temp.Data[i])
    
    # Check_Sum
    count_length_arr = (constant.DEFAULT_BYTE + (frame_message_temp.Length_Data - constant.DEFAULT_BYTE_CHECKSUM))
    frame_message_temp.Check_Frame = Check_Sum(data_out,count_length_arr)
    
    # Gán giá trị Check_Frame vào mảng
    crc = struct.pack('H',frame_message_temp.Check_Frame)
    data_out.append(crc[0])
    data_out.append(crc[1])
    
    count_length_arr += 2
    return count_length_arr

def Detect_Message(datain, dataout):
    count_length_arr = 0
    datain_index = 0
    # Chuyển mảng datain vào các phần trong struct của frame_temp
    frame_temp = constant.Message_Frame_Msg_T()
    
    frame_temp.Start_Frame = datain[datain_index]
    datain_index += 1

    frame_temp.Type_Message = datain[datain_index]
    datain_index += 1

    frame_temp.Length_Data = convert.Convert_From_Bytes_To_Uint16(datain[datain_index], datain[datain_index + 1])
    datain_index += 2

    frame_temp.Check_Frame = convert.Convert_From_Bytes_To_Uint16(datain[-2], datain[-1])

    while datain_index < (frame_temp.Length_Data + 2):
        frame_temp.Data.append(datain[datain_index])
        datain_index += 1

    # Copy struct_frame_temp vào dataout
    dataout.Start_Frame = frame_temp.Start_Frame
    dataout.Type_Message = frame_temp.Type_Message
    dataout.Length_Data = frame_temp.Length_Data
    dataout.Data = list(frame_temp.Data)
    dataout.Check_Frame = frame_temp.Check_Frame
    count_length_arr = constant.DEFAULT_BYTE + (dataout.Length_Data - constant.DEFAULT_BYTE_CHECKSUM)
   
    if(dataout.Start_Frame != constant.START_BYTE):
        return 0
    
    if(dataout.Check_Frame != Check_Sum(datain, count_length_arr)):
        return 0
    
    return (count_length_arr+constant.DEFAULT_BYTE_CHECKSUM)

def Print_Struct(struct, len_data):

    print("Start Frame:", hex(struct.Start_Frame))
    print("Type_Message:", hex(struct.Type_Message))
    print("Length_Data:", hex(struct.Length_Data))
    
    print("Data:", end= ' ')
    for i in range(len_data):
        print(hex(struct.Data[i]), end=' ')
    
    print('\n')
    print("Check_Frame:", hex(struct.Check_Frame))

def memcopy(arr_copy, arr_in, length):
    del arr_copy[:]
    for i in range(0, length):
        arr_copy.append(arr_in[i])

def Check_Sum(buf, length):
    crc = 0xFFFF
    for pos in range(length):
        crc ^= buf[pos]  # XOR byte into least sig. byte of crc
        for i in range(8, 0, -1):  # Loop over each bit
            if crc & 0x0001:  # If the LSB is set
                crc >>= 1  # Shift right and XOR 0xA001
                crc ^= 0xA001
            else:  # Else LSB is not set
                crc >>= 1  # Just shift right
    return crc


arr_in = [0xa5, 0x2, 0x10, 0x0, 0x1, 0x16, 0x0, 0x0, 0x0, 0xd5, 0xa3, 0x1b, 0xff, 0x68, 0x65, 0x6c, 0x6c, 0x6f, 0x5d, 0xf2]
struct_out = constant.Message_Frame_Msg_T()
length = Detect_Message(arr_in,struct_out)
Print_Struct(struct_out,length - 2 - 4)
# arr_out = []

# length = Create_Message(1,6,arr_in,arr_out)
# print(hex(frame_message_temp.Start_Frame))
# print(hex(frame_message_temp.Type_Message))
# print(hex(frame_message_temp.Length_Data))
# print(frame_message_temp.Data)
# print(hex(frame_message_temp.Check_Frame))

# for i in range(0, length):
#     print(hex(arr_out[i]),end=' ')

