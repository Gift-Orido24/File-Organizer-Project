import os
import shutil

def file_organiser(folder_path):
    categories = { "images":[".jpg",".jpeg",".png",".webp"], 
    "documents":[".pdf",".xlsx",".docx",".txt","epub"],
    "videos":[".mp4",".mkv"],
    "music":[".mp4",".wav"],
    "code":[".py",".js",".html"]}
    counts = {"images":0, "documents":0, "videos":0, "music":0, "code":0, "others":0}
    for files in os.listdir(folder_path):
        files_path = os.path.join(folder_path,files)
        print(f"processing {files}")
        if os.path.isdir(files_path):
            continue
        name,extn = os.path.splitext(files)
        ext = extn.lower()
        count = 1
        folder = "others"
        for category,file in categories.items():
            if ext in file:
                folder = category
                break
        counts[folder]+=1
        sub_path = os.path.join(folder_path,folder)
        if not os.path.exists(sub_path):
            os.mkdir(sub_path)
        dst_path = os.path.join(sub_path,files)
        while os.path.exists(dst_path):
            duplicate = f"{name} ({count}) {extn}"
            dst_path = os.path.join(sub_path,duplicate)
            print(f"moving {duplicate}")
            count+=1
        shutil.move(files_path,dst_path)
        print(f"moving {files}")
        print(f"moved {files} into {folder}")
        
        
    return counts
folder_path = input("path: ")
print(file_organiser(folder_path))