import os

def list_files_in_directory(directory_path):
    file_list = []
    print(directory_path)
    for root, dirs, files in os.walk(directory_path):
        #print("files:",files)
        for file in files:
            # 파일 경로를 추가 (상대경로 혹은 절대경로)
            print(f"디렉토리: {root}, 파일: {file}")
            file_list.append(os.path.join(root, file))
    return file_list

# 예시 사용
directory_path = 'C:\\Users\\LG33\\Desktop\\작업\\myproject\\templates'  # 확인하고자 하는 디렉토리 경로
files = list_files_in_directory(directory_path)

# 파일 리스트 출력
for file in files:
    print(file)
