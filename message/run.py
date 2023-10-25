import constant
import File_Size
import message
import message_handle
import serial
import time

port = serial.Serial("COM11", baudrate=9600)

def Send_Msg_To_Lora(arr):
    port.write(arr)

def run():
    input_file = "input.bin"
    output_file = "output.bin"
    size = 10                   # Độ dài của data đọc từ file(kích thước số byte cần lấy)
    index = 0                   # ví trị lấy (GetArrDataFile);
    update_count_size_loop = 0  # biến đếm 
         
    file_size = 0               # kich thước file 

    
    File_Size.Write_File(input_file,output_file)
    if(File_Size.Is_Data_Files_Same(input_file,output_file) == 1):
        file_size = File_Size.Get_Size_File(output_file)
    else:
        pass

    arr_out = []
    name = "hello"
    crc_file = File_Size.Get_Check_Sum_File(output_file)
    length = message_handle.UpdateFile_CreateFrameMetaData(constant.OTA_State_E.OTA_STATE_START.value,file_size,crc_file, name, arr_out)
    
    data_out = []
    length = message.Create_Message(2, length, arr_out, data_out)
    print("Create frame metadata:")
    Print_Array(data_out, length)
    Send_Msg_To_Lora(data_out)
    time.sleep(3)

    while update_count_size_loop < file_size:
        arr_data = []
        frame_data_out = []
        
        print("offset: ",index) 
        File_Size.Get_Arr_Data_File(output_file, size, index, arr_data)
        print("Create arr data in file:")
        print(arr_data)
        length_data = message_handle.UpdateFile_CreateFrameData(constant.OTA_State_E.OTA_STATE_DATA.value, size, index, arr_data, frame_data_out)
        
        length_msg = message.Create_Message(2, length_data, frame_data_out, data_out)
        
        print("Create message FrameData:")        
        Print_Array(data_out, length_msg)
        Send_Msg_To_Lora(data_out)
        time.sleep(3)

        update_count_size_loop += size
        index += size

    # crc_file = struct.pack('I',Get_Check_Sum_File(output_file))
    # print(crc_file)
    # print(Get_Check_Sum_File(output_file))

# In mảng 
def Print_Array(arr, length):
    for i in range(length):
        print(hex(arr[i]),end=' ')
    print('')

if __name__ == "__main__":
    run()