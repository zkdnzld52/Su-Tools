
# 목록 텍스트 파일에 복붙 후 원하는데로 텍스트 파일 내용 가공
f = open('./trans/change.txt','r', encoding='UTF8')
file_names = f.read()
f.close()
word =[]
j=0
file_names = file_names.replace("</option>","\n")
new_list = file_names.split('\n')
#for i in new_list:
for i in new_list:
    start = i.find(":")
    end = i.find(".wav")
    if ":" not in i[start+2:end] or ".wav" not in i[start+2:end]:
        word.append(i[start+2:end])
    else :
        continue

f = open('./trans/change.txt','w', encoding='UTF8')
for i in word:
    if j+1 == len(new_list):
        print("End")
        f.write(i)
    else:
        f.write(i+"\n")
        print(j)
    j+=1
f.close()
