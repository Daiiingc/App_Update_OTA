import os
import time
import struct
POLYNOMIAL  = 0x04C11DB7

# bên lora gửi đến PC thì mình đọc dữ liệu và ghi vào file output.bin 
def Write_File(original_file,received_file):
    input = open(original_file,'rb')
    output = open(received_file,'wb')
    data = input.read()
    output.write(data)
    
    input.close()
    output.close()

# Kiểm tra xem file gốc và file nhận có dữ liệu giống nhau không 
def Is_Data_Files_Same(original_file,received_file):

    input = open(original_file,'rb')
    output = open(received_file,'rb')
    data = input.read()
    data2 = output.read()

    input.close()
    output.close()

    if(data == data2):
        return True
    else:
        return False

# Lấy kích thước của file
def Get_Size_File(received_file):
    return os.path.getsize(received_file)

# Chuyển message trong file vào mảng 
def Get_Arr_Data_File(file_name,size,offset,data_out_arr):
    f = open(file_name,"rb")
    f.seek(offset, 0)
    del data_out_arr[:]
    while size:
        byte_data = f.read(1)
        if(byte_data != b''):
            data_out_arr.append(ord(byte_data))
            size -= 1
        else:
            break
    
    vitri = f.tell()
    f.close()
    return vitri

def crc32(crc, data, length):
    for i in range(0,length):
        crc ^= data[i]
        for j in range(0, 8):
            if  crc & 0x0001:
                crc >>= 1  # Shift right and XOR 0xA001
                crc ^= POLYNOMIAL
            else:
                crc >>= 1
    return crc

def Get_Check_Sum_File(file_name):
    arr_out = []
    check_sum = 0xFFFFFFFF
    f = open(file_name,"rb")
    size_file_bin = Get_Size_File(file_name)
    for i in range(0, size_file_bin):
        arr_out.append(ord(f.read(1)))
        check_sum = crc32(check_sum,arr_out, 1)
    
    f.close()
    check_sum ^= 0xFFFFFFFF
    return check_sum



