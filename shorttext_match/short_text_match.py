import math
import pkuseg
import pandas as pd
import csv
import time

'''
 @author: xuchao
 @time:2019-11-04
 @desc: 短文本相似度匹配
'''
seg = pkuseg.pkuseg()           # 以默认配置加载模型






def compute_cosine(sentence_a, sentence_b):
    # 找单词及词频
    words_a = seg.cut(sentence_a)  # 进行分词
    words_b = seg.cut(sentence_b)  # 进行分词


    words_a_dict = {}
    words_b_dict = {}
    for word in words_a:
        if word != '' and word in words_a_dict:
            num = words_a_dict[word]
            words_a_dict[word] = num + 1
        elif word != '':
            words_a_dict[word] = 1
        else:
            continue
    for word in words_b:
        if word != '' and word in words_b_dict:
            num = words_b_dict[word]
            words_b_dict[word] = num + 1
        elif word != '':
            words_b_dict[word] = 1
        else:
            continue
    print(words_a_dict)
    print(words_b_dict)

    # 排序
    dic1 = sorted(words_a_dict.items(), key=lambda asd: asd[1], reverse=True)
    dic2 = sorted(words_b_dict.items(), key=lambda asd: asd[1], reverse=True)
    print(dic1)
    print(dic2)

    # 得到词向量
    words_key = []
    for i in range(len(dic1)):
        words_key.append(dic1[i][0])  # 向数组中添加元素
    for i in range(len(dic2)):
        if dic2[i][0] in words_key:
            pass
        else:  # 合并
            words_key.append(dic2[i][0])

    vector_a = []
    vector_b = []
    for word in words_key:
        if word in words_a_dict:
            vector_a.append(words_a_dict[word])
        else:
            vector_a.append(0)
        if word in words_b_dict:
            vector_b.append(words_b_dict[word])
        else:
            vector_b.append(0)
    print(vector_a)
    print(vector_b)

    # 计算余弦相似度
    sum = 0
    sq1 = 0
    sq2 = 0
    for i in range(len(vector_a)):
        sum += vector_a[i] * vector_b[i]
        sq1 += pow(vector_a[i], 2)
        sq2 += pow(vector_b[i], 2)
    try:
        result = round(float(sum) / (math.sqrt(sq1) * math.sqrt(sq2)), 2)
    except ZeroDivisionError:
        result = 0.0
    print('result -> ' + str(result))
    return result

def return_result(text1, text2):
    if compute_cosine(text1,text2) > 0.5:
        return 'Match'
    else:
        return 'Mismatch'

def loadCsv():

    # 国标码
    """
    select * from dim.dim_region_info where type = '国标'
    """
    gb_data = pd.read_csv("D:/tools/query-hive-163336.csv",usecols=['id', 'name','prov_name'])
    # 银联与国标码未匹配结果
    """
    select
    a.id, a.name, a.parent_id, a.level, a.prov_id, a.prov_name, a.city_id, a.city_name, a.area_id, a.area_name, a.type
    from (select * from dim.dim_region_info where type = '银联') a
    left join (select * from dim.dim_region_info where type = '国标') b on a.name = b.name
    where b.name is null
    """
    yl_data = pd.read_csv("D:/tools/query-hive-163726.csv",usecols=['id', 'name','prov_name'])
    print('加载csv成功...')

    gb_data['area'] = gb_data['prov_name'] + '-' + gb_data['name']
    yl_data['area'] = yl_data['prov_name'] + '-' + yl_data['name']

    data = pd.DataFrame(columns=('gbcode','gbname','gbprovname','ylcode','ylname','ylprovname'))

    with open("d:/demo6.csv", "w") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['gbcode','gbname','gbprovname','ylcode','ylname','ylprovname'])

        for index, row in yl_data.iterrows():
            area = row['name'].replace('　','') + row['prov_name'][0]
            for index, row1 in gb_data.iterrows():
                area_1 = row1['name'].replace('　','') + row1['prov_name'][0]
                if area[0:2] == area_1[0:2]:
                    if area == area_1 :
                        # data['id'] = row['id']
                        # data['name'] = row['name']
                        # data['prov_name'] = row['prov_name']
                        # data['area'] = area
                        # data['type'] = row['type']
                        # data['yl_id'] = row1['id']
                        # data['yl_name'] = row1['name']
                        # data['yl_prov_name'] = row1['prov_name']
                        # data['yl_area'] = area_1
                        # data['yl_type'] = row1['type']
                        writer.writerow([row['id'],row['name'],row['prov_name'],row1['id'],row1['name'],row1['prov_name']])
                        # data.append(pd.DataFrame({'id':[row['id']],'name':[row['name']],'prov_name':[row['prov_name']],'area':[area],'type':[row['type']],'yl_id':[row1['id']],'yl_name':[row1['name']],'yl_prov_name':[row1['prov_name']],'yl_area':[area_1],'yl_type':[row1['type']]}))
                        break
                    else :
                        if compute_cosine(area, area_1) > 0.5:
                            # data['id'] = row['id']
                            # data['name'] = row['name']
                            # data['prov_name'] = row['prov_name']
                            # data['area'] = area
                            # data['type'] = row1['type']
                            # data['yl_id'] = row1['id']
                            # data['yl_name'] = row1['name']
                            # data['yl_prov_name'] = row1['prov_name']
                            # data['yl_area'] = area_1
                            # data['yl_type'] = row1['type']
                            writer.writerow([row['id'], row['name'], row['prov_name'], row1['id'], row1['name'],row1['prov_name']])
                            # data.append(pd.DataFrame(
                            #     {'id': [row['id']], 'name': [row['name']], 'prov_name': [row['prov_name']], 'area': [area],\
                            #      'type': [row['type']],\
                            #      'yl_id': [row1['id']], 'yl_name': [row1['name']], 'yl_prov_name': [row1['prov_name']],\
                            #      'yl_area': [area_1], 'yl_type': [row1['type']]}))
        # data.to_csv('d:/demo.csv')




if __name__ == '__main__':
    text1 = '新疆维吾尔族自治区'
    text2 = '新疆维吾尔自治区'
    print(return_result(text1,text2))
    # start = time.time();
    # loadCsv()
    # end = time.time()
    # print(end - start)