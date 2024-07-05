import pandas as pd
import re
from collections import Counter

def dict_province(keyword):
    area_data = {
        '北京': ['北京市','朝阳区', '海淀区', '通州区', '房山区', '丰台区', '昌平区', '大兴区', '顺义区', '西城区', '延庆县', '石景山区', '宣武区', '怀柔区', '崇文区', '密云县',
               '东城区', '门头沟区', '平谷区'],
        '广东':['广东省', '东莞市', '广州市', '中山市', '深圳市', '惠州市', '江门市', '珠海市', '汕头市', '佛山市', '湛江市', '河源市', '肇庆市','潮州市', '清远市', '韶关市', '揭阳市', '阳江市', '云浮市', '茂名市', '梅州市', '汕尾市'],
        '山东':['山东省', '济南市', '青岛市', '临沂市', '济宁市', '菏泽市', '烟台市','泰安市', '淄博市', '潍坊市', '日照市', '威海市', '滨州市', '东营市', '聊城市', '德州市', '莱芜市', '枣庄市'],
        '江苏':['江苏省', '苏州市', '徐州市', '盐城市', '无锡市','南京市', '南通市', '连云港市', '常州市', '扬州市', '镇江市', '淮安市', '泰州市', '宿迁市'],
        '河南':['河南省', '郑州市', '南阳市', '新乡市', '安阳市', '洛阳市', '信阳市','平顶山市', '周口市', '商丘市', '开封市', '焦作市', '驻马店市', '濮阳市', '三门峡市', '漯河市', '许昌市', '鹤壁市', '济源市'],
        '上海':['上海市', '松江区', '宝山区', '金山区','嘉定区', '南汇区', '青浦区', '浦东新区', '奉贤区', '闵行区', '徐汇区', '静安区', '黄浦区', '普陀区', '杨浦区', '虹口区', '闸北区', '长宁区', '崇明县', '卢湾区'],
        '河北':[ '河北省', '石家庄市', '唐山市', '保定市', '邯郸市', '邢台市', '河北区', '沧州市', '秦皇岛市', '张家口市', '衡水市', '廊坊市', '承德市'],
        '浙江':['浙江省', '温州市', '宁波市','杭州市', '台州市', '嘉兴市', '金华市', '湖州市', '绍兴市', '舟山市', '丽水市', '衢州市'],
        '陕西':['陕西省', '西安市', '咸阳市', '宝鸡市', '汉中市', '渭南市','安康市', '榆林市', '商洛市', '延安市', '铜川市'],
        '湖南':[ '湖南省', '长沙市', '邵阳市', '常德市', '衡阳市', '株洲市', '湘潭市', '永州市', '岳阳市', '怀化市', '郴州市','娄底市', '益阳市', '张家界市', '湘西州'],
        '重庆':[  '重庆市', '江北区', '渝北区', '沙坪坝区', '九龙坡区', '万州区', '永川市', '南岸区', '酉阳县', '北碚区', '涪陵区', '秀山县', '巴南区', '渝中区', '石柱县', '忠县', '合川市', '大渡口区', '开县', '长寿区', '荣昌县', '云阳县', '梁平县', '潼南县', '江津市', '彭水县', '璧山县', '綦江县',
     '大足县', '黔江区', '巫溪县', '巫山县', '垫江县', '丰都县', '武隆县', '万盛区', '铜梁县', '南川市', '奉节县', '双桥区', '城口县'],
        '福建':['福建省', '漳州市', '泉州市','厦门市', '福州市', '莆田市', '宁德市', '三明市', '南平市', '龙岩市'],
        '天津':['天津市', '和平区', '北辰区', '河北区', '河西区', '西青区', '津南区', '东丽区', '武清区','宝坻区', '红桥区', '大港区', '汉沽区', '静海县', '宁河县', '塘沽区', '蓟县', '南开区', '河东区'],
        '云南':[ '云南省', '昆明市', '红河州', '大理州', '文山州', '德宏州', '曲靖市', '昭通市', '楚雄州', '保山市', '玉溪市', '丽江地区', '临沧地区', '思茅地区', '西双版纳州', '怒江州', '迪庆州'],
        '四川':['四川省', '成都市', '绵阳市', '广元市','达州市', '南充市', '德阳市', '广安市', '阿坝州', '巴中市', '遂宁市', '内江市', '凉山州', '攀枝花市', '乐山市', '自贡市', '泸州市', '雅安市', '宜宾市', '资阳市','眉山市', '甘孜州'],
        '广西':['广西壮族自治区', '贵港市', '玉林市', '北海市', '南宁市', '柳州市', '桂林市', '梧州市', '钦州市', '来宾市', '河池市', '百色市', '贺州市', '崇左市',  '防城港市'],
        '安徽':['安徽省', '芜湖市', '合肥市', '六安市', '宿州市', '阜阳市','安庆市', '马鞍山市', '蚌埠市', '淮北市', '淮南市', '宣城市', '黄山市', '铜陵市', '亳州市','池州市', '巢湖市', '滁州市'],
        '海南':['海南省', '三亚市', '海口市', '琼海市', '文昌市', '东方市', '昌江县', '陵水县', '乐东县', '五指山市', '保亭县', '澄迈县', '万宁市','儋州市', '临高县', '白沙县', '定安县', '琼中县', '屯昌县'],
        '江西':['江西省', '南昌市', '赣州市', '上饶市', '吉安市', '九江市', '新余市', '抚州市', '宜春市', '景德镇市', '萍乡市', '鹰潭市'],
        '湖北':['湖北省', '武汉市', '宜昌市', '襄樊市', '荆州市', '恩施州', '孝感市', '黄冈市', '十堰市', '咸宁市', '黄石市', '仙桃市', '随州市', '天门市', '荆门市', '潜江市', '鄂州市', '神农架林区'],
        '山西':['山西省', '太原市', '大同市', '运城市', '长治市', '晋城市', '忻州市', '临汾市', '吕梁市', '晋中市', '阳泉市', '朔州市'],
        '辽宁':['辽宁省', '大连市', '沈阳市', '丹东市', '辽阳市', '葫芦岛市', '锦州市', '朝阳市', '营口市', '鞍山市', '抚顺市', '阜新市', '本溪市', '盘锦市', '铁岭市'],
        '台湾':['台湾省','台北市', '高雄市', '台中市', '新竹市', '基隆市', '台南市', '嘉义市'],
        '黑龙江':['黑龙江', '齐齐哈尔市', '哈尔滨市', '大庆市', '佳木斯市', '双鸭山市', '牡丹江市', '鸡西市','黑河市', '绥化市', '鹤岗市', '伊春市', '大兴安岭地区', '七台河市'],
        '内蒙古':['内蒙古自治区', '赤峰市', '包头市', '通辽市', '呼和浩特市', '乌海市', '鄂尔多斯市', '呼伦贝尔市','兴安盟', '巴彦淖尔盟', '乌兰察布盟', '锡林郭勒盟', '阿拉善盟'],
        '香港':["香港","香港特别行政区"],
        '澳门':['澳门','澳门特别行政区'],
        '贵州':['贵州省', '贵阳市', '黔东南州', '黔南州', '遵义市', '黔西南州', '毕节地区', '铜仁地区','安顺市', '六盘水市'],
        '甘肃':['甘肃省', '兰州市', '天水市', '庆阳市', '武威市', '酒泉市', '张掖市', '陇南地区', '白银市', '定西地区', '平凉市', '嘉峪关市', '临夏回族自治州','金昌市', '甘南州'],
        '青海':['青海省', '西宁市', '海西州', '海东地区', '海北州', '果洛州', '玉树州', '黄南藏族自治州'],
        '新疆':['新疆','新疆维吾尔自治区', '乌鲁木齐市', '伊犁州', '昌吉州','石河子市', '哈密地区', '阿克苏地区', '巴音郭楞州', '喀什地区', '塔城地区', '克拉玛依市', '和田地区', '阿勒泰州', '吐鲁番地区', '阿拉尔市', '博尔塔拉州', '五家渠市',
     '克孜勒苏州', '图木舒克市'],
        '西藏':['西藏区', '拉萨市', '山南地区', '林芝地区', '日喀则地区', '阿里地区', '昌都地区', '那曲地区'],
        '吉林':['吉林省', '吉林市', '长春市', '白山市', '白城市','延边州', '松原市', '辽源市', '通化市', '四平市'],
        '宁夏':['宁夏回族自治区', '银川市', '吴忠市', '中卫市', '石嘴山市', '固原市']
    }
    for k,v in area_data.items():
        for i in v:
            if keyword in i:
                return k

class LiePinDealer:
    def __init__(self,filename) -> None:
        self.filename = filename
        try:
            self.csvfile=pd.read_csv(filename)
        except Exception as e:
            print('文件读取错误',e)
    def readfile(self,filename=''):
        if filename!='':
            self.filename = filename
        try:
            self.csvfile=pd.read_csv(self.filename)
        except Exception as e:
            print('文件读取错误',e)
        return self.csvfile
    def get_position_data(self):
        position_column = self.csvfile['职位']
        #print( self.csvfile.columns,position_column.values.tolist())
        return position_column.values.tolist()
    def get_money_data(self):
        position_money = self.csvfile['工资']
        #print( position_money.values.tolist())
        return position_money.values.tolist() 
    def get_local_data(self):
        position_local = self.csvfile['工作地区、工作年限、学历']
        #print( position_local.values.tolist())
        return position_local.values.tolist() 
    def get_time_data(self):
        position_time = self.csvfile['工作地区、工作年限、学历']
        #print( position_time.values.tolist())
        return position_time.values.tolist() 
    def get_local_time_academic_data(self):  
        position_local_time_academic = self.csvfile['工作地区、工作年限、学历']
        #print( position_local_time_academic.values.tolist())
        return position_local_time_academic.values.tolist() 
    def get_compain_name_data(self):
        position_compain_name = self.csvfile['公司名称']
        #print( position_compain_name.values.tolist())
        return position_compain_name.values.tolist() 
    def get_compain_info_data(self):
        position_compain_info = self.csvfile['公司信息']
        #print( position_compain_info.values.tolist())
        return position_compain_info.values.tolist() 
    def get_url_info_data(self):
        position_detail_info = self.csvfile['详情页']
        #print( position_detail_info.values.tolist())
        return position_detail_info.values.tolist() 
    def get_detail_posions(self):
         position_detail_info = self.csvfile['工作详细']
         position_detail_info=position_detail_info.values.tolist()
         return position_detail_info
    def get_reward_data(self):
         reward_data = self.csvfile['福利']
         #print(reward_data.values.tolist())
         return reward_data.values.tolist()
    def get_capacity_data(self):
        reward_data = self.csvfile['工作需要']
        parsed_data = reward_data.apply(lambda x: None if x.strip('[]') == '' else x)#去除 '[]'
        parsed_data = parsed_data.dropna()
        #print(parsed_data.values.tolist())
        data = [ eval(datas) for datas in parsed_data.values.tolist()]
        #print(data)
        return data
    def get_data_list(self):
        name = self.csvfile['职位']
        salary = self.csvfile['工资']
        info = self.csvfile['工作地区、工作年限、学历'].apply(lambda x: '无' if x.strip('[]') == '' else x.strip('[]').replace("'", "").replace(" ", "") )
        reward = self.csvfile['福利'].apply(lambda x: '无' if x.strip("'[]'") == '' else x.strip('[]') )
        campany_name = self.csvfile['公司名称'].fillna('无')
        #print(campany_name)
        url = self.csvfile['详情页']
        data=[]
        for i in range(len(self.csvfile)):
            data.append((name[i],info[i],salary[i],reward[i],campany_name[i],url[i]))
        #print(data,sep='\n')
        return data  
    def get_position_num(self):   
        data=self.csvfile
        return  len(data)


class AnalysisDealer:
    def __init__(self,liepindealer,filename=''):
         if liepindealer is None and filename!='':
            try:
                liepindealer = LiePinDealer(filename)
            except Exception as e:
                print('AnalysisDealer文件读取错误',e)
         self.data_loader=liepindealer
    def get_position_data(self):
          '''
             返回 ['人工智能技术负责人', '人工智能AI开发工程师',]
          '''
          position_column = self.csvfile['职位']
          #print( self.csvfile.columns,position_column.values.tolist())
          return position_column.values.tolist()        
    def get_salary_data(self):#可能改成年薪
        """
        ([15, 30], 14), ([40, 60],), ([50, 80], 13), ('薪资面议', 8)]     
        薪资面议单独计数   有14 13薪的元组长度为2  第一个元素不是字符串就是 salary_range
        """
        infos=self.data_loader.get_money_data()
        salary_info = []
        salary_face=0
        for info in infos:
            salary_range = None
            salary_type = None
            min_salary=0
            max_salary=0
            data_block=[]
            match_range = re.search(r'(\d+-\d+)k', info)
            if match_range:
               salary_range = match_range.group(1)
               min_salary,max_salary = map(int,salary_range.split('-'))
               data_block.append([min_salary,max_salary])
            if '薪资面议' in info:
                salary_face+=1
            elif '薪' in info:
                salary_type = re.search(r'·(\d+)薪', info).group(1)
                data_block.append(int(salary_type))
            if len(data_block):
              salary_info.append(tuple(data_block))
        salary_info.append(('薪资面议',salary_face))
        return salary_info
        return salary_range,salary_face,salary_type
    def get_time_data(self):
        """ ['经验不限', '3-5年', '3-5年', '5-10年', '10年以上', '1-3年', '1-3年', '5-10年', '3-5年', '5-10年', '5-10年', '5-10年', 
        '3-5年', '3-5年', '5-10年', '5-10 年', '5-10年']"""
        position_local_time_academic =self.data_loader.get_local_time_academic_data()
        times=[eval(data)[1] for data in position_local_time_academic]
        #print(times)
        return times
    def get_time_Hz(self):
        """ ['经验不限', '3-5年', '3-5年', '5-10年', '10年以上', '1-3年', '1-3年', '5-10年', '3-5年', '5-10年', '5-10年', '5-10年', 
        '3-5年', '3-5年', '5-10年', '5-10 年', '5-10年']"""
        position_time =self.get_time_data()
        #print(position_time)
        counts = Counter(position_time)
        #print(dict(counts))
        experience_dict=dict(counts)
        return dict(sorted(experience_dict.items()))
        return times
    def get_time_json(self):
        datas =self.get_time_Hz()
        result = [{ "value":count,"name": name,} for name,count in datas.items()]
        return result
    def get_academic_data(self):
        """['学历不限', '博士', '本科', '本
            科', '硕士', '硕士', '硕士', '本科', '硕士', '统招本科', '博士', '本科',
              '硕士', '统招本科', '硕士', '本科', '本科', '统招本科', '本科', '本科', '统招本科', '硕士']
        """
        position_local_time_academic =self.data_loader.get_local_time_academic_data()
        academics=[eval(data)[2] for data in position_local_time_academic]
        #print(academics)
        return academics
    def get_academic_Hz(self):
        datas =self.get_academic_data()
        counts = Counter(datas)
        #print(dict(counts))
        return dict(counts)
    def get_academic_json(self):
        datas =self.get_academic_Hz()
        result = [{ "value":count,"name": name,} for name,count in datas.items()]
        
        return result
    def get_reward_Hz(self):
        """
        输出为字典
        '扁平管理': 6, '管理规范': 2, '餐补': 2, '交通补贴': 2, '通讯补贴': 2, '防暑降温费': 2, '取暖费': 2, '过节费': 2, 
        '职称津贴': 2, '简历处理快': 7, '回复速度快': 7, '团队聚餐': 2, '生育补贴': 1, '股票期权': 2, '全勤奖': 2, '年度旅游': 1, '住房补贴': 1, '免费班车': 1, '通讯津贴': 2, 
        '交通补助': 2, '午餐补助': 1, '生日福利 假': 1, '特定节日假期': 1, '优秀员工奖': 1, '世界500强企业': 1, '六险一金': 1}
        """
        reward_data =self.data_loader.get_reward_data()
        datas=[ ]
        for reward in reward_data:
            data=eval(reward)
            if len(data):
             datas.extend(eval(reward)) 
        counts = Counter(datas)
        #print(dict(counts))
        return dict(counts)
    
    def get_reward_json(self):
         reward_data =self.get_reward_Hz()
         result = [{"name": name, "value":count} for name,count in reward_data.items()]
         #print(result)
         return result


    def get_province_data(self):
        '''
        ['武汉', '佛山', '武汉', '上海', '苏州', ]
        '''
        cities=self.get_city_data()
        provinces = [dict_province(city) for city in cities]        
        return provinces
    def get_province_Hz(self):
        '''
        {'湖北': 6, '广东': 4, '上海': 4, '江苏': 5, '北京': 11, '山东': 3, '陕西': 1, '浙江': 2, '湖南': 1, '四川': 1}
        '''
        counts = Counter(self.get_province_data())
        #print(dict(counts))
        return dict(counts)
    def get_province_json(self):
         
         data=self.get_province_Hz()
         result = [{"name": name, "value":count} for name,count in data.items()]
         return result
         #print(result)



    def get_local_data(self):  
          """
          ["['武汉-洪山区', '5-10年', '本科']", "['南京-江宁区', '经验不限', '统招本科']",
          """
          position_local_time_academic =self.data_loader.get_local_time_academic_data()
          datas = position_local_time_academic
          locals=[]
          for data in datas:
               data=eval(data)
               #print(data)
               if len(data) !=0:
                local=data[0]
                locals.append(local)
          return locals 
         
    def get_city_data(self):
         local_data=self.get_local_data()
         provinces=[ local.split('-')[0] for local in local_data]
         #print(provinces)
         return provinces
    def get_compain_name_data(self):
          return self.data_loader.get_compain_name_data()
    def get_compain_info_data(self):#待分解   行业 规模 位置
          """['云计算/大数据', '100-499人', '武汉-洪山区长江云通有限公司'], ['其他行业', '100-499人', '佛山-禅城区石湾街道番村世纪车城1栋5楼']]"""
          compain_infos= self.data_loader.get_compain_info_data()
          compain_info=[]
          for data in compain_infos:
               data=eval(data)
               if len(data)==4:
                    del data[1]
               if len(data):
                compain_info.append(data)
          #print(compain_info)
          return compain_info
    def get_industry_Hz(self):
        '''
          行业类型频率
          {'计算机软件': 4, '工业自动化': 4, '云计算': 3, '大数据': 3, '学术': 3, '科研': 3, '互联网': 3, '电力': 3, '热力': 3, 
          '燃气': 3, '水务': 3, '其他行业': 2, '人工智能': 2, 
          '政府': 1, '公共事业': 1, '培训服务': 1, '批发': 1, '零售': 1, '工程施工': 1, '电子商务': 1, '通信设备': 1, '整车制造': 1}
         
        '''
        compain_infos= self.get_compain_info_data()
        data=[]
        for compain_info in compain_infos:
             data.extend(compain_info[0].split('/')) 
        counts = Counter(data)
        
        #print(counts)
        return dict(counts)
    def get_industry_json(self):
        '''
        json数据  用于公司行业词云
        [{'name': '电子商务', 'value': 1}, {'name': '通信设备', 'value': 1}, {'name': '整车制造', 'value': 1}]
        '''
        compain_infos= self.get_industry_Hz()
        return  [{"name": name, "value":count} for name,count in compain_infos.items()]


    def get_url_info_data(self):
                return self.data_loader.get_url_info_data()
    def get_capacity_Hz(self):
        datas=self.data_loader.get_capacity_data()
        counts=[]
        for data in datas:
             counts.extend(data)
        counts=Counter(counts)
        #print(counts)
        return dict(counts)
    def get_capacity_json(self):
        datas=self.get_capacity_Hz()
        return  [{"name": name, "value":count} for name,count in datas.items()]
    def get_scale_data(self):
        '''公司规模'''
        compain_infos= self.get_compain_info_data()
        #print(compain_infos)
        compain_info=[ data[1] for data in compain_infos]
        #print(compain_info) 
        return compain_info
    def get_scale_Hz(self):
        datas=self.get_scale_data()
        counts=Counter(datas)
        #print(counts)
        return  dict(counts)
    def get_scale_json(self):
        datas=self.get_scale_Hz()
        return  sorted( [{"name": name, "value":count} for name,count in datas.items()], key=lambda x: x['name'])
class Dataloader(object):
    def __init__(self,filename) -> None:
        self.AnalysisDealer=AnalysisDealer(LiePinDealer(filename))
    def turn_load(self,filname):
        self.AnalysisDealer=AnalysisDealer(LiePinDealer(filname))
    def get_position_num(self):
        return self.AnalysisDealer.data_loader.get_position_num()
    def get_scale_json(self):#公司规模
        return self.AnalysisDealer.get_scale_json()
    def get_capacity_json(self):#能力需求
        return self.AnalysisDealer.get_capacity_json()
    def get_industry_json(self):#公司行业领域
        return self.AnalysisDealer.get_industry_json()
    def get_province_json(self):#省份分布
        return self.AnalysisDealer.get_province_json()
    def get_reward_json(self):#福利
        return self.AnalysisDealer.get_reward_json()
    def get_datalist_json(self):
        return self.AnalysisDealer.data_loader.get_data_list()
    def get_academic_json(self):
        return self.AnalysisDealer.get_academic_json()
    def get_jobtime_json(self):
        return self.AnalysisDealer.get_time_json()
    def get_jobtime_data(self):
        keylist=self.AnalysisDealer.get_time_Hz().keys()
        valuelist=self.AnalysisDealer.get_time_Hz().values()
        data={'x':list(keylist), 'y':list(valuelist)}
        return data
if __name__ == '__main__':
    data=LiePinDealer('人工智能_liepindata.csv')
    #data.get_data_list()
    # data.get_money_data()
    # data.get_capacity_data()
    # data.get_position_data()
    # data.get_local_data()
    # data.get_time_data()
    # data.get_compain_info_data()
    # data.get_compain_name_data()
    # data.get_url_info_data()
    # data.get_local_time_academic_data()
    a=AnalysisDealer(data)
    # a.get_salary_data()
    #a.get_local_data()
    #a.get_city_data()
    #a.get_academic_data()
    #a.get_academic_Hz()
    #print(a.get_time_json())
    #print(a.get_academic_json())
    # a.get_time_data()
    # a.get_compain_name_data()
    # a.get_url_info_data()
    #a.get_compain_info_data()
    #a.get_reward_Hz()
    #a.get_province_data()
    #a.get_province_Hz()
    #a.get_province_json()
    #a.get_reward_json()
    #print(a.get_industry_Hz())
    #print(a.get_industry_json())
    #a.get_time_Hz()
    #a.get_reward_json()
    #a.get_capacity_Hz()
    #a.get_scale_data()
    #a.get_scale_Hz()
    #print(a.get_scale_json())
    #print(a.get_capacity_json())
    a=Dataloader('人工智能_liepindata.csv')
    print(a.get_jobtime_data())
    #print(a.get_position_num())
    
    #print(a.get_datalist_json())