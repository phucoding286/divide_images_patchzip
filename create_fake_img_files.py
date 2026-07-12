import os, random

folder = "./imagesv2"
sequence_text = list("qwertyuiopasdfghjklzxcvbnm")
file_format = "png"
fake_file_num = 10_000

if not os.path.exists(folder):
    os.mkdir(folder)

for _ in range(fake_file_num):
    random.shuffle(sequence_text)
    filename = folder + "/" + "".join(sequence_text) + "." + file_format
    with open(filename, mode="w"): pass

print(f"Tổng số file đã tạo => {len(os.listdir(folder))}")