import os
import random

f = open("./trans/change.txt",'r', encoding='UTF8')
data = f.read()
f.close()
list_data = data.split('\n')
new_list = []


# 파일 명 변경 코드
path = 'C:/workspace/test/trans/음성 파일 샘플'
os.chdir('./trans/음성 파일 샘플')
file_names = os.listdir()
i = 0
for test in file_names:
    # 확장자를 뺀 파일명을 test1에 담아주기
    test1 = os.path.splitext(test)[0]
    
    # 변경전 파일명을 test2에 담아주기
    test2 = path + "/" + test1 + os.path.splitext(test)[1]
    
    #test2를 리스트에 추가
    new_list.append(test2)

    test2 = new_list[i]
    # 변경하고픈 파일명을 dst에 담아주기
    dst = path + "/"+ list_data[i] + ".json"

    # 파일명 변경 시 파일명 중복이 없으면 실행
    if os.path.exists(dst) == False:
        os.rename(test2, dst)
        print("파일명 :",test1)
        print("변경된 파일명 :",list_data[i]) 
    # 파일명 중복이 있으면 삭제
    else:
        print("------------ 에러 발생 ------------")
        print("중복된 파일명 :",test1,"삭제")
        print("중복된 변경될 파일명 :", list_data[i] )
        os.remove(test2)
        print("------------ 조치 완료 ------------")
    i += 1

# ------------------------------------------------------------------------------------

# 파일명에 set 추가 코드(임의로 넣는거라서 나중에 제대로된 기준이 정해지면 수정해야함)
file_names = os.listdir()

for test in file_names:

    #파일명에 set이 없으면 시작
    if "set" not in test:

        sets = ["set1", "set2", "set3"]
        resets = random.choice(sets)
        test1 = os.path.splitext(test)[0]
        print("test1 :",test1)

        strings=test1.split("_")
        strings.insert(1,resets)
        str_list = strings
        result = ' '.join(s for s in str_list)
        result1 = result.replace(" ", "_")
        test2 = path + "/" + test1 + os.path.splitext(test)[1]
        dst = path + "/" + result1 + ".json"
        os.rename(test2, dst)
        print("파일명 :",dst)