import os, random, shutil
print("=== Phần nhập vào đường dẫn folders chứa ảnh. ===")

list_image_folders = []
while True:
    filepath_input = input(f"[?] Nhập vào đường dẫn folder ảnh của bạn hoặc gõ F (final) rồi enter để bắt đầu chạy chương trình.\n-> ").strip().lower()
    if filepath_input == "f":
        break
    elif filepath_input == "final":
        break
    list_image_folders.append(filepath_input)
expected_batch = int(input("[?] Nhập batch số lượng ảnh trên mỗi patch file zip\n-> "))
print()

tempfolder_, zipfolder_ = ('./temp', './zip')
if not os.path.exists(tempfolder_):
    os.mkdir(tempfolder_)
if not os.path.exists(zipfolder_):
    os.mkdir(zipfolder_)
folderpathes = [os.listdir(path) for path in list_image_folders]
filesnum = [len(pathes) for pathes in folderpathes]
total_data = sum(filesnum)
patchnum_files = total_data // expected_batch
batchnum_per_file = [num // patchnum_files for num in filesnum]

for i in range(patchnum_files):
    print(f"=== Bước tính toán cho patch file thứ {i+1}/{patchnum_files} ===")
    print(" [..] Đang tính toán chunk và trộn pathes.")
    fullpathes = []
    for j in range(len(list_image_folders)):
        folderpath = list_image_folders[j]
        start_idx, end_idx = (batchnum_per_file[j] * i), (batchnum_per_file[j] * (i + 1))
        patches_j = folderpathes[j][start_idx:end_idx]
        for path in patches_j:
            fullpath = folderpath + "/" + path
            fullpathes.append(fullpath)
    random.shuffle(fullpathes)
    patchpath = f"patch{i+1}"
    temp_folder, zipfile = f"{tempfolder_}/temp_" + patchpath, f"{zipfolder_}/zip_" + patchpath
    if not os.path.exists(temp_folder):
        os.mkdir(temp_folder)
    print(f" [..] Đang chuyển ảnh vào folder temp => {temp_folder}")
    for path in fullpathes:
        shutil.copy(path, temp_folder + "/" + path.split("/")[-1])
    print(f" [..] Đang chuyển folder temp thành file zip => {zipfile}")
    shutil.make_archive(zipfile, "zip", temp_folder)
    fullpathes.clear()
    print(f" [..] Đã hoàn thành tất cả các bước.")
    print()