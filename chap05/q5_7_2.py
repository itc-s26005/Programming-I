data = [
        ['0001' , 'Male' , 'Yamada' , 'Tarou' , 25 , 'Tokyo'],
        ['0002' , 'Male' , 'Satou' , 'Takeshi' , 27 , 'TKanagawa'],
        ['0003' , 'Female' , 'Tanaka' , 'Yuko' , 25 , 'Saitama'],
        ['0004' , 'Male' , 'Suzuki' , 'Ichrou' , 35 , 'Hokkaido']
        ]
print(data)

#辞書変数生成
member_information = {}

#表データをレコードに格納する
for record in data:
    key = record[0]
    info = record[1:]
    member_information[key] = info

print('number', 'information', sep='\t')
for key, info in member_information.items():
    print(key, info)
