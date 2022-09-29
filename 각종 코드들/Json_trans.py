import os
import json
from collections import OrderedDict


# 파일명 추출해보기
os.chdir('./trans/음성 파일 샘플')
file_names = os.listdir()
ErrorFile = []
collectorname = []

# 파일명 추출 후 리스트로 변환
for filename in file_names:
    print("파일명 :",filename)
    
# 예외 처리된 파일명 넣어줄 변수
    try:
        
        # json 파일 읽어서 변수에 담기
        with open("C:/workspace/test/trans/음성 파일 샘플/"+filename,"r",encoding = 'UTF8') as f:
            json_data = json.load(f)
        
        
        # 파일명을 test에 담아주기
        test = os.path.splitext(filename)[0]

        

        # test에 담긴 파일명들을 "_" 단위로 쪼개주기
        strings = test.split("_")

        # 추출한 speakerId를 담아줄 비어있는 리스트
        new_strings = []

        # 추출한 audioId를 담아줄 비어있는 리스트
        new_strings2 = ""
        for i in strings:
            # 파일명에서 SpeakerId 추출 후 담아주기
            if "speaker" in i:
                # strings에 담긴 리스트 중에 speaker가 포함된 것들만 new_strings에 담기
                new_strings.append(i)
        # 리스트로 변환하고 json 파일 불러온 변수에다가 speakerId 수정하기
        for i in range(len(new_strings)):
            # speaker/speakerId 변환
            json_data['speaker'][i]['speakerId'] = new_strings[i]
            # audio/records/speakerId 변환
            json_data["audio"]["records"][i]["speakerId"] = new_strings[i]
            # audio/records/recordDevice 변환
            json_data["audio"]["records"][i]["recordDevice"] = "Android_12"
            # audio/records/recordDate 변환
            json_data["audio"]["records"][i]["recordDate"] = "20220825"
            # speaker/recruiterId 행 삭제
            if "recruiterId" in json_data["speaker"][i]:
                del json_data["speaker"][i]["recruiterId"]
            # json_data["speaker"][i].pop("recruiterId") 이것도 가능!

            # 파일명에 speaker가 하난데 json 안에 speaker 파라메터가 2개일때 2번째 파라메터 삭제 코드
            if len(new_strings) != len(json_data['speaker']):
                del json_data["speaker"][1]
            
        # 맨 아랫줄 standard 삭제
        if "standard" in json_data["annotation"]:
            del json_data["annotation"]["standard"]
        # fileName이 아닌 filename이 있을 경우    
        if "filename" in json_data:
            del json_data["filename"]
        # stt/responseDate 변환
        json_data["stt"]["responseDate"] = "20220825"
        # stt/recognizer 변환
        json_data["stt"]["recognizer"] = "naver clova speech"
        # stt/speakerIds 변환
        json_data["stt"]["speakerIds"] = new_strings
        # transcription/sentences/speakerId 변환(첫번째 Id 밖에 없음)
        json_data["transcription"]["sentences"][0]['speakerId'] = new_strings[0]
        # sentences 안에 dialect값을 script value값으로 수정하기
        json_data["script"]["value"] = json_data["transcription"]['dialect']
        # script 안에 audioId 값을 파일명으로 수정하기
        json_data["script"]["audioId"] = test
        # audio 안에 audioId 값을 파일명으로 수정하기
        json_data["audio"]["audioId"] = test
        # stt 안에 audioId 값을 파일명으로 수정하기
        json_data["stt"]["audioId"] = test
        # transcription/segments 안에 audioId 값을 파일명으로 수정하기
        json_data["transcription"]["audioId"] = test
        # script/speechType 타입 변환
        # say, talk일 경우 Speak로, st일 경우 Read로
        if "st" in strings:
            json_data["script"]["speechType"] = "Read"
        elif "say" or "talk" in strings:
            json_data["script"]["speechType"] = "Speak"
        # 파일명이 st이 들어가고 speaker가 2개 일때 2번째 speaker 삭제
        if "st" in strings and (2 == len(json_data["speaker"])):
            del json_data["speaker"][1]
        # 파일명에서 collector 추출 후 담아주기
        for i in strings:
            if "collector" in i:
                # strings에 담긴 리스트 중에 collector가 포함된 것들만 new_strings2에 담기
                new_strings2=i
                collectorname.append(i)
        if new_strings2 == "collectorcc1":
            gender = "m"
            birthYear = "1972"
            residenceProvince = "cc"
            residenceCity = "42"
            residencePeriod = "15"
            job = "사회복지사"
            academicBackground = "4"
            healthCondition = "1"
        elif new_strings2 == "collectorgs1":
            gender = "f"
            birthYear = "1970"
            residenceProvince = "gs"
            residenceCity = "14"
            residencePeriod = "20"
            job = "심리학자"
            academicBackground = "4"
            healthCondition = "1"
        elif new_strings2 == "collectorgs2":
            gender = "f"
            birthYear = "1968"
            residenceProvince = "gs"
            residenceCity = "22"
            residencePeriod = "20"
            job = "직업상담사"
            academicBackground = "3"
            healthCondition = "1"
        elif new_strings2 == "collectorgs3":
            gender = "f"
            birthYear = "1962"
            residenceProvince = "gs"
            residenceCity = "20"
            residencePeriod = "35"
            job = "공인노무사"
            academicBackground = "4"
            healthCondition = "1"
        elif new_strings2 == "collectorgs4":
            gender = "f"
            birthYear = "1967"
            residenceProvince = "gs"
            residenceCity = "6"
            residencePeriod = "20"
            job = "농부"
            academicBackground = "3"
            healthCondition = "1"
        elif new_strings2 == "collectorgs5":
            gender = "f"
            birthYear = "1970"
            residenceProvince = "gs"
            residenceCity = "16"
            residencePeriod = "20"
            job = "심리학자"
            academicBackground = "4"
            healthCondition = "1"
        elif new_strings2 == "collectorgs7":
            gender = "f"
            birthYear = "1970"
            residenceProvince = "gs"
            residenceCity = "47"
            residencePeriod = "28"
            job = "보육교사"
            academicBackground = "3"
            healthCondition = "1"
        elif new_strings2 == "collectorgs9":
            gender = "f"
            birthYear = "1975"
            residenceProvince = "gs"
            residenceCity = "47"
            residencePeriod = "28"
            job = "공무원"
            academicBackground = "3"
            healthCondition = "1"
        elif new_strings2 == "collectorgs14":
            gender = "f"
            birthYear = "1977"
            residenceProvince = "gs"
            residenceCity = "47"
            residencePeriod = "28"
            job = "교사"
            academicBackground = "3"
            healthCondition = "1"
        elif new_strings2 == "collectorgs15":
            gender = "f"
            birthYear = "1981"
            residenceProvince = "gs"
            residenceCity = "47"
            residencePeriod = "28"
            job = "환경미화원"
            academicBackground = "3"
            healthCondition = "1"
        elif new_strings2 == "collectorgs16":
            gender = "f"
            birthYear = "1973"
            residenceProvince = "gs"
            residenceCity = "47"
            residencePeriod = "28"
            job = "군무원"
            academicBackground = "3"
            healthCondition = "1"
        elif new_strings2 == "collectorgs21":
            gender = "f"
            birthYear = "1970"
            residenceProvince = "gs"
            residenceCity = "47"
            residencePeriod = "28"
            job = "공무원"
            academicBackground = "3"
            healthCondition = "1"
        elif new_strings2 == "collectorjl1":
            gender = "m"
            birthYear = "1966"
            residenceProvince = "jl"
            residenceCity = "22"
            residencePeriod = "20"
            job = "직업상담사"
            academicBackground = "3"
            healthCondition = "1"
        elif new_strings2 == "collectorjl2":
            gender = "f"
            birthYear = "1962"
            residenceProvince = "jl"
            residenceCity = "21"
            residencePeriod = "2"
            job = "부동산중계사"
            academicBackground = "3"
            healthCondition = "1"
        elif new_strings2 == "collectorgw1":
            gender = "f"
            birthYear = "1977"
            residenceProvince = "gw"
            residenceCity = "2"
            residencePeriod = "20"
            job = "건강가정사"
            academicBackground = "3"
            healthCondition = "1"          
        elif new_strings2 == "collectorgw2":
            gender = "f"
            birthYear = "1969"
            residenceProvince = "gw"
            residenceCity = "4"
            residencePeriod = "35"
            job = "보육교사"
            academicBackground = "4"
            healthCondition = "1"
        elif new_strings2 == "collectorjj1":
            gender = "f"
            birthYear = "1961"
            residenceProvince = "jj"
            residenceCity = "47"
            residencePeriod = "30"
            job = "심리학자"
            academicBackground = "4"
            healthCondition = "1"
        elif new_strings2 == "collectorjj2":
            gender = "f"
            birthYear = "1966"
            residenceProvince = "jj"
            residenceCity = "48"
            residencePeriod = "20"
            job = "직업상담사"
            academicBackground = "3"
            healthCondition = "1"
        elif new_strings2 == "collectorjj3":
            gender = "f"
            birthYear = "1968"
            residenceProvince = "jj"
            residenceCity = "48"
            residencePeriod = "29"
            job = "공인노무사"
            academicBackground = "3"
            healthCondition = "1"
        elif new_strings2 == "collectorjj4":
            gender = "m"
            birthYear = "1970"
            residenceProvince = "jj"
            residenceCity = "47"
            residencePeriod = "20"
            job = "사회복지사"
            academicBackground = "3"
            healthCondition = "1"
        elif new_strings2 == "collectorjj5":
            gender = "f"
            birthYear = "1961"
            residenceProvince = "jj"
            residenceCity = "48"
            residencePeriod = "30"
            job = "직업상담사"
            academicBackground = "3"
            healthCondition = "1"
        elif new_strings2 == "collectorjj6":
            gender = "m"
            birthYear = "1970"
            residenceProvince = "jj"
            residenceCity = "47"
            residencePeriod = "20"
            job = "사회복지사"
            academicBackground = "3"
            healthCondition = "1"
        elif new_strings2 == "collectorjj7":
            gender = "m"
            birthYear = "1970"
            residenceProvince = "jj"
            residenceCity = "47"
            residencePeriod = "20"
            job = "공인노무사"
            academicBackground = "3"
            healthCondition = "1"

        collector = ['collector', 
                        {"collectorId":new_strings2, 
                        "gender":gender,
                        "birthYear":birthYear,
                        "residenceProvince":residenceProvince, 
                        "residenceCity":residenceCity,
                        "residencePeriod":residencePeriod,
                        "job":job,
                        "academicBackground":academicBackground,
                        "healthCondition":healthCondition
                        }
                    ]

        if len(json_data['speaker'])==2:
            if json_data['speaker'][0]['gender'] == json_data['speaker'][1]['gender']:
        
                if "F" == json_data['speaker'][0]['gender']:
        
                    json_data['speaker'][1]['gender'] = "M"
        
                elif "M" == json_data['speaker'][0]['gender']:
        
                    json_data['speaker'][1]['gender'] = "F"
                
        # fileName 생성 후 파일명을 값에 넣어주기
        fileName = {"fileName":test}

        # json을 list로 변환 후 insert()로 원하는 순서에 삽입(반복 작동시 순서 꼬일 수 있음)
        a = list(json_data.items())

        # collector 객체 삽입
        if "collector" in a[1] and "fileName" in a[0]:
            del a[1]
            a.insert(2,(collector))
        elif "fileName" in a[0] and "speaker" in a[1]:
            if "collector" in a[2]:
                a.insert(2,(collector))
        else :
            a.insert(1, (collector))

        # list로 변환한 객체를 다시 dict로 변환
        aa = OrderedDict(a)

        # dict로 바꾼 후 파일명 요소 삽입
        aa.update(fileName)

        # 맨 뒤로 삽입된 filename을 맨 앞으로 당겨오기
        aa.move_to_end('fileName',False)

        # json_data에 선언
        json_data = aa

        

    except:
        print("예외처리 발생")
        ErrorFile.append(filename)
        continue



    # 저장
    with open('C:/workspace/test/trans/음성 파일 샘플/'+filename, 'w', encoding='UTF8') as make_file:
    # dump 메소드는 기본적으로 ascii 형태로 저장하기 때문에 dump 한글 저장을 위해서 파라메터에 ensure_ascii=False가 필수로 들어가야한다.
        json.dump(json_data, make_file, indent = "\t", ensure_ascii = False)\

print("변환 파일",len(file_names),"개 항목")
if len(ErrorFile)>=0:
    print("예외 처리된 파일 :", ErrorFile)
    print("예외 파일 갯수 :",len(ErrorFile))
cset = set(collectorname)
csett = list(cset)
# print("콜렉터 종류 :",csett)
# print("콜렉터 갯수 :",len(csett))

