en = "아니아니아니되옵니다"
line = "저니츠어럇되니다"

count = 0
accuracy = 0

for i in range(len(en)) if len(en) < len(line) else range(len(line)):
    if en[i] == line[i]:
        count += 1
        
accuracy = int(round(count / len(en), 2) * 100)
print(accuracy)
