import constant
import struct



def Create_Message(type_msg, length, data_in, data_out):
    del data_out[:]
    frame_message_temp = constant.Message_Frame_Msg_T()
    count_length_arr = 0
    # Start
    frame_message_temp.Start_Frame = constant.START_BYTE
    # Type Message
    frame_message_temp.Type_Message = type_msg
    # Length
    frame_message_temp.Length_Data = length + constant.DEFAULT_BYTE_CHECKSUM
    # Data
    # print(frame_message_temp.Data)
    memcopy(frame_message_temp.Data,data_in,length)

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


# arr_in = [1,2,3,4,5,6]
# arr_out = []

# length = Create_Message(1,6,arr_in,arr_out)
# print(hex(frame_message_temp.Start_Frame))
# print(hex(frame_message_temp.Type_Message))
# print(hex(frame_message_temp.Length_Data))
# print(frame_message_temp.Data)
# print(hex(frame_message_temp.Check_Frame))

# for i in range(0, length):
#     print(hex(arr_out[i]),end=' ')

