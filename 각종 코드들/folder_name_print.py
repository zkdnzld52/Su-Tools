import os


path = 'C:/workspace/test/trans/음성 파일 샘플'
os.chdir(path)
file_names = os.listdir()
for test in file_names:
    # 확장자를 뺀 파일명을 test1에 담아주기
    test1 = os.path.splitext(test)[0]
    print(test1)
