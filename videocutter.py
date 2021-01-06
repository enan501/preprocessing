from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
import os


def is_folder(line:str):
    return line.split(":")[0] == "folder"

def is_type(line:str):
    return line.split(":")[0] == "type"

def is_file(line:str):
    return line.split(":")[0] == "file"

def get_name(line:str):
    return line.split(":")[-1].replace("\n", "")

def get_times_and_category(line:str):
    category = line.split(" ")[-1].replace("\n", "")
    times = line.split(" ")[0].split("-")
    start_time, end_time = convert_to_sec(times[0]), convert_to_sec(times[1])
    return start_time, end_time, category

def convert_to_sec(time:str):
    min = float(time.split(":")[0])
    sec = float(time.split(":")[1])
    msec = float(time.split(":")[2])
    return min * 60 + sec + msec/100

def mkdir_if_not_exist(dir:str):
    if not os.path.isdir(dir):
        os.mkdir(dir)

if __name__ == "__main__":
    os.chdir("/Users/enan/Projects/2020-02/grad-project/data")
    trim_list = open("trim_list.txt", 'r')
    folder, file, type = "", "", ""
    index = 1
    output_prefix = "cheating"
    mkdir_if_not_exist(output_prefix)
    while True:
        line = trim_list.readline()
        if not line:
            break
        if is_folder(line):
            folder = get_name(line)
        elif is_type(line):
            type = get_name(line)
        elif is_file(line):
            file = get_name(line)
            index = 1
        else:  # 부정행위
            start_time, end_time, category = get_times_and_category(line)
            output_name = f"{output_prefix}/{category}/{type}/{index}_{file}"
            mkdir_if_not_exist(f"{output_prefix}/{category}")
            mkdir_if_not_exist(f"{output_prefix}/{category}/{type}")
            ffmpeg_extract_subclip(f"{folder}/{file}", start_time, end_time, targetname=output_name)
            print(f"{output_name}_saved")
            index += 1
