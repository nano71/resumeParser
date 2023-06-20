from nlp_ecloud import CMSSEcloudNlpClient

accesskey = '613e43c93bf34345acd1786a49efbc6c'
secretkey = '1677beb41213436c9a8ca436f34dc194'
url = 'https://api-wuxi-1.cmecloud.cn:8443'


# 1-1 sentiment for weibo
def request_sentiment_wb():
    requesturl = '/api/nlp/v1/sentiment/wb'
    params = {}
    params['textId'] = '123'
    params['text'] = '今天天气不错'
    items = {}
    items['items'] = [params]
    try:
        nlp_client = CMSSEcloudNlpClient(accesskey, secretkey, url)
        response = nlp_client.request_nlp_service(requesturl, items)
        print(response.text)
    except ValueError as e:
        print(e)

# 1-2 sentiment for news
def request_sentiment_news():
    requesturl = '/api/nlp/v1/sentiment/news'
    params = {}
    params['textId'] = '123'
    params['text'] = '今天天气不错'
    params['title'] = '天气说明'
    items = {}
    items['items'] = [params]
    try:
        nlp_client = CMSSEcloudNlpClient(accesskey, secretkey, url)
        response = nlp_client.request_nlp_service(requesturl, items)
        print(response.text)
    except ValueError as e:
        print(e)

# 1-3 sentiment for forum
def request_sentiment_forum():
    requesturl = '/api/nlp/v1/sentiment/forum'
    params = {}
    params['textId'] = '123'
    params['text'] = '今天天气不错'
    params['title'] = '天气说明'
    items = {}
    items['items'] = [params]
    try:
        nlp_client = CMSSEcloudNlpClient(accesskey, secretkey, url)
        response = nlp_client.request_nlp_service(requesturl, items)
        print(response.text)
    except ValueError as e:
        print(e)


# 1-4 sentiment for negative judgement
def request_sentiment_genative():
    requesturl = '/api/nlp/v1/sentiment/negative'
    params = {}
    params['textId'] = '123'
    params['content'] = '今天天气不错'
    params['title'] = '天气说明'
    items = {}
    items['items'] = [params]
    try:
        nlp_client = CMSSEcloudNlpClient(accesskey, secretkey, url)
        response = nlp_client.request_nlp_service(requesturl, items)
        print(response.text)
    except ValueError as e:
        print(e)

# 2-1 segmentation
def request_segmentation():
    requesturl = '/api/nlp/v1/segmentation'
    params = {}
    params['textId'] = '123'
    params['text'] = '今天天气不错'
    items = {}
    items['items'] = [params]
    try:
        nlp_client = CMSSEcloudNlpClient(accesskey, secretkey, url)
        response = nlp_client.request_nlp_service(requesturl, items)
        print(response.text)
    except ValueError as e:
        print(e)

# 3-1 keywords
def request_keyswords():
    requesturl = '/api/nlp/v1/keywords'
    params = {}
    params['textId'] = '123'
    params['text'] = '今天天气不错'
    params['initial'] = 'words'
    items = {}
    items['items'] = [params]
    try:
        nlp_client = CMSSEcloudNlpClient(accesskey, secretkey, url)
        response = nlp_client.request_nlp_service(requesturl, items)
        print(response.text)
    except ValueError as e:
        print(e)

# 4-1 convert doc
def request_convertdoc():
    requesturl = "/api/nlp/v1/convertdoc"
    params = {}
    # use your own file name here
    params['auditFile'] = open('C:\\Users\\CMSS\\Desktop\\extract.pdf','rb')
    file_path = 'C:\\Users\\CMSS\\Desktop\\extract.pdf'
    try:
        nlp_client = CMSSEcloudNlpClient(accesskey, secretkey, url)
        response = nlp_client.request_nlp_service(requesturl, file_path)
        if response is not None:
            print(response.text)
    except ValueError as e:
        print(e)

# 4-2 announcement
def request_announcement():
    requesturl = '/api/nlp/v1/announcement-ie'
    params = {}
    params['textId'] = '123'
    params['htmlText'] = '招标人：中国移动'
    items = {}
    items['items'] = [params]
    try:
        nlp_client = CMSSEcloudNlpClient(accesskey, secretkey, url)
        response = nlp_client.request_nlp_service(requesturl, items)
        print(response.text)
    except ValueError as e:
        print(e)

# 4-3 summary
def request_summary():
    requesturl = '/api/nlp/v1/summary'
    params = {}
    params['textId'] = '123'
    params['text'] = '今天天气不错'
    params['count'] = 3
    items = {}
    items['items'] = [params]
    try:
        nlp_client = CMSSEcloudNlpClient(accesskey, secretkey, url)
        response = nlp_client.request_nlp_service(requesturl, items)
        print(response.text)
    except ValueError as e:
        print(e)

# 4-4 comment mining
def request_comment_mining():
    requesturl = '/api/nlp/v1/comment-mining'
    params = {}
    params['textId'] = '123'
    params['textlist'] = ['今天天气不错','今天天气很差']
    items = {}
    items['items'] = [params]
    try:
        nlp_client = CMSSEcloudNlpClient(accesskey, secretkey, url)
        response = nlp_client.request_nlp_service(requesturl, items)
        print(response.text)
    except ValueError as e:
        print(e)

# 5-1 industry
def request_industry():
    requesturl = '/api/nlp/v1/industry'
    params = {}
    params['textId'] = '123'
    params['content'] = '阮建安,求职目标：市场营销总监,阮建安,求职目标：市场营销总监,2019.10-至今,微安控股集团,副总监,负责协助集团旗下事业部开展各项工作，制定品牌传播方案；,结合集团与事业部发展，制定营销策略、广告策略、品牌策略和公关策略，组织推进执行；,制定和执行媒体投放计划，跟踪和监督媒体投放效果，进行数据分析与撰写报告；,负责公司品牌形象和价值提升的持续优化，提高品牌知名度；,研究行业发展动态，定期进行市场调查,为产品更新提供建议。,2016.10-2019.10,利群有限公司,市场及运营总监,根据公司发展情况进行战略调整，配合前端销售部门搭建销售渠道；,负责公司品牌形象和价值提升的持续优化，提高品牌知名度；,研究行业发展动态，定期进行市场调查,为产品更新提供建议；,负责公司部门(营运、品牌策划)制度规范，负责组织及监管市场部关于对外合作、渠道管理、媒体合作、推广策划以相关工作的落实。,工作经历,2019.10-至今,微安控股集团,副总监,负责协助集团旗下事业部开展各项工作，制定品牌传播方案；,结合集团与事业部发展，制定营销策略、广告策略、品牌策略和公关策略，组织推进执行；,制定和执行媒体投放计划，跟踪和监督媒体投放效果，进行数据分析与撰写报告；,负责公司品牌形象和价值提升的持续优化，提高品牌知名度；,研究行业发展动态，定期进行市场调查,为产品更新提供建议。,2016.10-2019.10,利群有限公司,市场及运营总监,根据公司发展情况进行战略调整，配合前端销售部门搭建销售渠道；,负责公司品牌形象和价值提升的持续优化，提高品牌知名度；,研究行业发展动态，定期进行市场调查,为产品更新提供建议；,负责公司部门(营运、品牌策划)制度规范，负责组织及监管市场部关于对外合作、渠道管理、媒体合作、推广策划以相关工作的落实。,工作经历,基本信息,出生年月：1995.05,民,族：汉,电,话：13818138525,邮,箱：,住,址：广东省广州市海珠区,性,别：女,身,高：177cm,政治面貌：中共党员,毕业院校：广州新安职业技术学院,学,历：大专,基本信息,出生年月：1995.05,民,族：汉,电,话：13818138525,邮,箱：,住,址：广东省广州市海珠区,性,别：女,身,高：177cm,政治面貌：中共党员,毕业院校：广州新安职业技术学院,学,历：大专,2013.09-2016.06,奈森师范大学,市场营销（大专）,主修课程：管理学、微观经济学、宏观经济学、管理信息系统、统计学、会计学、财务管理、市场营销、经济法、消费者行为学、国际市场营销,教育背景,2013.09-2016.06,奈森师范大学,市场营销（大专）,主修课程：管理学、微观经济学、宏观经济学、管理信息系统、统计学、会计学、财务管理、市场营销、经济法、消费者行为学、国际市场营销,教育背景,利群集团品牌升级发布会,集团全新品牌logo及VI上线，在多渠道进行了传播；,企业VIP客户群体逾60人，结合了线上发布、线下体验；,后续媒体报道持续升温，子品牌罄玉结合代言人罗嘉良制造话题营销，为期3周；,微安招商引资发布会,整场活动以会议+洽谈双重模式进行，首日以介绍微安内部平台资源优势，政府背景优势等为主，一对多推介会进行推广普及；,现场签署地方合作意向书，如：新疆、江西、浙江等优秀企业商户；,中国的波尔多为宣传点，主推旗下新疆大型项目，罄玉生态葡萄庄园、沙漠主题俱乐部等，制造营销、品牌热点。,微安投资控股集团6A自媒体生态圈建设,本项目重构了公司现有微信企业号的功能与架构。,提高公众号的关注粉丝量的同时，对于有客户进行统一宣传，统一管理。,项目经历,利群集团品牌升级发布会,集团全新品牌logo及VI上线，在多渠道进行了传播；,企业VIP客户群体逾60人，结合了线上发布、线下体验；,后续媒体报道持续升温，子品牌罄玉结合代言人罗嘉良制造话题营销，为期3周；,微安招商引资发布会,整场活动以会议+洽谈双重模式进行，首日以介绍微安内部平台资源优势，政府背景优势等为主，一对多推介会进行推广普及；,现场签署地方合作意向书，如：新疆、江西、浙江等优秀企业商户；,中国的波尔多为宣传点，主推旗下新疆大型项目，罄玉生态葡萄庄园、沙漠主题俱乐部等，制造营销、品牌热点。,微安投资控股集团6A自媒体生态圈建设,本项目重构了公司现有微信企业号的功能与架构。,提高公众号的关注粉丝量的同时，对于有客户进行统一宣传，统一管理。,项目经历,拥有多年的市场管理及品牌营销经验，卓越的规划、组织、策划、方案执行和团队领导能力，积累较强的人际关系处理能力和商务谈判技巧，善于沟通，具备良好的合作关系掌控能力与市场开拓能力；,敏感的商业和市场意识，具备优秀的资源整合能力、业务推进能力；,思维敏捷，有培训演讲能力，懂激励艺术，能带动团队的积极性；,擅长协调平衡团队成员的竞争与合作的关系，善于通过培训提高团队综合能力和凝聚力。,自我评价,拥有多年的市场管理及品牌营销经验，卓越的规划、组织、策划、方案执行和团队领导能力，积累较强的人际关系处理能力和商务谈判技巧，善于沟通，具备良好的合作关系掌控能力与市场开拓能力；,敏感的商业和市场意识，具备优秀的资源整合能力、业务推进能力；,思维敏捷，有培训演讲能力，懂激励艺术，能带动团队的积极性；,擅长协调平衡团队成员的竞争与合作的关系，善于通过培训提高团队综合能力和凝聚力。,自我评价,计算机四级证书,大学英语四、六级证书,(CET-4，CET-6),所获证书,计算机四级证书,大学英语四、六级证书,(CET-4，CET-6),所获证书,通过全国计算机二级考试，熟练运用office相关软件。,熟练使用绘声绘色软件，剪辑过各种类型的电影及班级视频。,大学英语四/六级（CET-4/6），良好听说读写能力，快速浏览英语专业书籍。,掌握技能,通过全国计算机二级考试，熟练运用office相关软件。,熟练使用绘声绘色软件，剪辑过各种类型的电影及班级视频。,大学英语四/六级（CET-4/6），良好听说读写能力，快速浏览英语专业书籍。,掌握技能,2016年,新安职业技术学院自强社“优秀社员”,2015年,三下乡”社会实践活动“优秀学生”,2015年新安职业技术学院学生田径运动会10人立定跳远团体赛第三名,2015年,新安职业技术学院盼盼杯烘焙食品创意大赛优秀奖,2014年,新安职业技术学院“点燃中华梦,畅享我青春”微博文征集大赛二等奖,奖项荣誉,2016年,新安职业技术学院自强社“优秀社员”,2015年,三下乡”社会实践活动“优秀学生”,2015年新安职业技术学院学生田径运动会10人立定跳远团体赛第三名,2015年,新安职业技术学院盼盼杯烘焙食品创意大赛优秀奖,2014年,新安职业技术学院“点燃中华梦,畅享我青春”微博文征集大赛二等奖,奖项荣誉'
    params['title'] = '简历'
    items = {}
    items['items'] = [params]
    try:
        nlp_client = CMSSEcloudNlpClient(accesskey, secretkey, url)
        response = nlp_client.request_nlp_service(requesturl, items)
        print(response.text)
    except ValueError as e:
        print(e)

# 5-2 filter
def request_filter():
    requesturl = '/api/nlp/v1/filter'
    params = {}
    params['textId'] = '123'
    params['content'] = '今天天气不错'
    params['title'] = '天气说明'
    params['type'] = 'bbs'
    items = {}
    items['items'] = [params]
    try:
        nlp_client = CMSSEcloudNlpClient(accesskey, secretkey, url)
        response = nlp_client.request_nlp_service(requesturl, items)
        print(response.text)
    except ValueError as e:
        print(e)

# 5-3 viewpiont
def request_viewpoint():
    requesturl = '/api/nlp/v1/viewpoint'
    params = {}
    params['textId'] = '123'
    params['text'] = '今天天气不错'
    items = {}
    items['items'] = [params]
    try:
        nlp_client = CMSSEcloudNlpClient(accesskey, secretkey, url)
        response = nlp_client.request_nlp_service(requesturl, items)
        print(response.text)
    except ValueError as e:
        print(e)

# 5-4 rumor
def request_rumor():
    requesturl = '/api/nlp/v1/rumor'
    params = {}
    params['textId'] = '123'
    params['text'] = '今天天气不错'
    items = {}
    items['items'] = [params]
    try:
        nlp_client = CMSSEcloudNlpClient(accesskey, secretkey, url)
        response = nlp_client.request_nlp_service(requesturl, items)
        print(response.text)
    except ValueError as e:
        print(e)

# 5-5 text similarity
def request_text_similarity():
    requesturl = '/api/nlp/v1/text-similarity'
    params = {}
    params['textId'] = '123'
    params['source'] = '北京是中国的首都'
    params['target'] = '中国的首都是北京'
    items = {}
    items['items'] = [params]
    try:
        nlp_client = CMSSEcloudNlpClient(accesskey, secretkey, url)
        response = nlp_client.request_nlp_service(requesturl, items)
        print(response.text)
    except ValueError as e:
        print(e)

# 5-6 theme matcher
def request_theme_matcher():
    requesturl = '/api/nlp/v1/theme-matcher'
    params = {}
    params['textId'] = '123'
    params['content'] = "2016.05-2018.06                 深圳中专学校                 辩论队（队长）	负责50余人团队的日常训练、选拔及团队建设；	作为负责人对接多项商业校园行活动，如《奔跑吧兄弟》录制、《时代周末》校园行。2016.11-2018.06                 沟通与交流协会                 创始人/副会长	协助省沟通协会创立分部，从零开始组建初期团队；	策划协会会员制，选拔、培训协会导师，推出一系列沟通课程。"
    params['title'] = "简历中的企业工作经历描述"
    params['keyString'] = "简历中的企业工作经历描述"
    items = {}
    items['items'] = [params]
    try:
        nlp_client = CMSSEcloudNlpClient(accesskey, secretkey, url)
        response = nlp_client.request_nlp_service(requesturl, items)
        print(response.text)
    except ValueError as e:
        print(e)

# 6-1 emotion recognize
def request_emotion():
    requesturl = '/api/nlp/v1/emotion'
    params = {}
    params['textId'] = '123'
    params['text'] = '今天天气不错'
    items = {}
    items['items'] = [params]
    try:
        nlp_client = CMSSEcloudNlpClient(accesskey, secretkey, url)
        response = nlp_client.request_nlp_service(requesturl, items)
        print(response.text)
    except ValueError as e:
        print(e)

# 6-2 weibo emotion recognize
def request_wbemotion():
    requesturl = '/api/nlp/v1/wbemotion'
    params = {}
    params['textId'] = '123'
    params['text'] = '今天天气不错'
    items = {}
    items['items'] = [params]
    try:
        nlp_client = CMSSEcloudNlpClient(accesskey, secretkey, url)
        response = nlp_client.request_nlp_service(requesturl, items)
        print(response.text)
    except ValueError as e:
        print(e)

# 7-1 named entity recoginize
def request_entity():
    requesturl = '/api/nlp/v1/entity'
    params = {}
    params['textId'] = '123'
    params['text'] = '2019.10-至今,微安控股集团,副总监,负责协助集团旗下事业部开展各项工作，制定品牌传播方案；,结合集团与事业部发展，制定营销策略、广告策略、品牌策略和公关策略，组织推进执行；,制定和执行媒体投放计划，跟踪和监督媒体投放效果，进行数据分析与撰写报告；,负责公司品牌形象和价值提升的持续优化，提高品牌知名度；,研究行业发展动态，定期进行市场调查,为产品更新基本信息,出生年月：1995.05,民,族：汉,电,话：13818138525,邮,箱：,住,址：广东省广州市海珠区,性,别：女,身,高：177cm,政治面貌：中共党员,毕业院校：广州新安职业技术学院,学,历：大专,2013.09-2016.06,奈森师范大学,市场营销（大专）,主修课程：管理学、微观经济学、宏观经济学、管理信息系统、统计学、会计学、财务管理、市场营销、经济法、消费者行为学、国际市场营销,教育背景,2013.09-2016.06,奈森师范大学,市场营销（大专）,主修课程：管理学、微观经济学、宏观经济学、管理信息系统、统计学、会计学、财务管理、市场营销、经济法、消费者行为学、国际市场营销,教育背景,利'
    items = {}
    items['items'] = [params]
    try:
        nlp_client = CMSSEcloudNlpClient(accesskey, secretkey, url)
        response = nlp_client.request_nlp_service(requesturl, items)
        print(response.text)
    except ValueError as e:
        print(e)

# 7-2 location entity recognize
def request_location():
    requesturl = '/api/nlp/v1/location'
    params = {}
    params['textId'] = '123'
    params['content'] = '北京是中国的首都城市'
    params['title'] = '北京'
    items = {}
    items['items'] = [params]
    try:
        nlp_client = CMSSEcloudNlpClient(accesskey, secretkey, url)
        response = nlp_client.request_nlp_service(requesturl, items)
        print(response.text)
    except ValueError as e:
        print(e)

# 7-3 transmit
def request_transmit():
    requesturl = '/api/nlp/v1/transmit'
    params = {}
    params['textId'] = '123'
    params['text'] = '甘肃张掖网讯（张掖日报融媒体记者 杨静文,10月26日,市人大常委会党组书记王海峰在甘州区检查督导疫情防控工作'
    items = {}
    items['items'] = [params]
    try:
        nlp_client = CMSSEcloudNlpClient(accesskey, secretkey, url)
        response = nlp_client.request_nlp_service(requesturl, items)
        print(response.text)
    except ValueError as e:
        print(e)
        
        
 # warningfilter       
def request_warningfilter():
    requesturl = '/api/nlp/v1/warning-filter'
    params = {}
    params['textId'] = '123'
    params['title'] = '一名30多岁男子因鱼竿掉进河里，跳入河中捞鱼…'
    params['content'] = '7月4日下午1时许，在黑龙江省哈尔滨市道外区团结镇东风村五棵树屯附近阿什河，一名30多岁男子因鱼竿掉进河里，跳入河中捞鱼…'
    textFilterList ={}
    params2 ={}
    params2['textId'] = '1234'
    params2['title'] = '一名30多岁男子因鱼竿掉进河里，跳入河中捞鱼…'
    params2['content'] = '7月4日下午1时许，在黑龙江省哈尔滨市道外区团结镇东风村五棵树屯附近阿什河，一名30多岁男子因鱼竿掉进河里，跳入河中捞鱼…'
    params3 ={}
    params3['textId'] = '12345'
    params3['title'] = '大量鸭子已经“葬身火海'
    params3['content'] = '事发浙江丽水缙云县新建镇，当消防员迅速感到现场后发现，近100平方米的鸭棚已经被烧得面目全非，大量鸭子已经“葬身火海事发浙江丽水缙云县新建镇，当消防员迅速感到现场后发现，近100平方米的鸭棚已经被烧得面目全非，大量鸭子已经'
    textFilterList['textFilterList'] = [params2,params3]
    params['textFilterList'] =[textFilterList]
    items = {}
    items['items'] = [params]
    try:
        nlp_client = CMSSEcloudNlpClient(accesskey, secretkey, url)
        response = nlp_client.request_nlp_service(requesturl, items)
        print(response.text)
    except ValueError as e:
        print(e)      
        
     # 6-2 rumor-feature
def request_rumorfeature():
    requesturl = '/api/nlp/v1/rumor-feature'
    params = {}
    params['textId'] = '123'
    params['title'] = '简历'
    params['content'] = '阮建安,求职目标：市场营销总监,阮建安,求职目标：市场营销总监,2019.10-至今,微安控股集团,副总监,负责协助集团旗下事业部开展各项工作，制定品牌传播方案；,结合集团与事业部发展，制定营销策略、广告策略、品牌策略和公关策略，组织推进执行；,制定和执行媒体投放计划，跟踪和监督媒体投放效果，进行数据分析与撰写报告；,负责公司品牌形象和价值提升的持续优化，提高品牌知名度；,研究行业发展动态，定期进行市场调查,为产品更新提供建议。,2016.10-2019.10,利群有限公司,市场及运营总监,根据公司发展情况进行战略调整，配合前端销售部门搭建销售渠道；,负责公司品牌形象和价值提升的持续优化，提高品牌知名度；,研究行业发展动态，定期进行市场调查,为产品更新提供建议；,负责公司部门(营运、品牌策划)制度规范，负责组织及监管市场部关于对外合作、渠道管理、媒体合作、推广策划以相关工作的落实。,工作经历,2019.10-至今,微安控股集团,副总监,负责协助集团旗下事业部开展各项工作，制定品牌传播方案；,结合集团与事业部发展，制定营销策略、广告策略、品牌策略和公关策略，组织推进执行；,制定和执行媒体投放计划，跟踪和监督媒体投放效果，进行数据分析与撰写报告；,负责公司品牌形象和价值提升的持续优化，提高品牌知名度；,研究行业发展动态，定期进行市场调查,为产品更新提供建议。,2016.10-2019.10,利群有限公司,市场及运营总监,根据公司发展情况进行战略调整，配合前端销售部门搭建销售渠道；,负责公司品牌形象和价值提升的持续优化，提高品牌知名度；,研究行业发展动态，定期进行市场调查,为产品更新提供建议；,负责公司部门(营运、品牌策划)制度规范，负责组织及监管市场部关于对外合作、渠道管理、媒体合作、推广策划以相关工作的落实。,工作经历,基本信息,出生年月：1995.05,民,族：汉,电,话：13818138525,邮,箱：,住,址：广东省广州市海珠区,性,别：女,身,高：177cm,政治面貌：中共党员,毕业院校：广州新安职业技术学院,学,历：大专,基本信息,出生年月：1995.05,民,族：汉,电,话：13818138525,邮,箱：,住,址：广东省广州市海珠区,性,别：女,身,高：177cm,政治面貌：中共党员,毕业院校：广州新安职业技术学院,学,历：大专,2013.09-2016.06,奈森师范大学,市场营销（大专）,主修课程：管理学、微观经济学、宏观经济学、管理信息系统、统计学、会计学、财务管理、市场营销、经济法、消费者行为学、国际市场营销,教育背景,2013.09-2016.06,奈森师范大学,市场营销（大专）,主修课程：管理学、微观经济学、宏观经济学、管理信息系统、统计学、会计学、财务管理、市场营销、经济法、消费者行为学、国际市场营销,教育背景,利群集团品牌升级发布会,集团全新品牌logo及VI上线，在多渠道进行了传播；,企业VIP客户群体逾60人，结合了线上发布、线下体验；,后续媒体报道持续升温，子品牌罄玉结合代言人罗嘉良制造话题营销，为期3周；,微安招商引资发布会,整场活动以会议+洽谈双重模式进行，首日以介绍微安内部平台资源优势，政府背景优势等为主，一对多推介会进行推广普及；,现场签署地方合作意向书，如：新疆、江西、浙江等优秀企业商户；,中国的波尔多为宣传点，主推旗下新疆大型项目，罄玉生态葡萄庄园、沙漠主题俱乐部等，制造营销、品牌热点。,微安投资控股集团6A自媒体生态圈建设,本项目重构了公司现有微信企业号的功能与架构。,提高公众号的关注粉丝量的同时，对于有客户进行统一宣传，统一管理。,项目经历,利群集团品牌升级发布会,集团全新品牌logo及VI上线，在多渠道进行了传播；,企业VIP客户群体逾60人，结合了线上发布、线下体验；,后续媒体报道持续升温，子品牌罄玉结合代言人罗嘉良制造话题营销，为期3周；,微安招商引资发布会,整场活动以会议+洽谈双重模式进行，首日以介绍微安内部平台资源优势，政府背景优势等为主，一对多推介会进行推广普及；,现场签署地方合作意向书，如：新疆、江西、浙江等优秀企业商户；,中国的波尔多为宣传点，主推旗下新疆大型项目，罄玉生态葡萄庄园、沙漠主题俱乐部等，制造营销、品牌热点。,微安投资控股集团6A自媒体生态圈建设,本项目重构了公司现有微信企业号的功能与架构。,提高公众号的关注粉丝量的同时，对于有客户进行统一宣传，统一管理。,项目经历,拥有多年的市场管理及品牌营销经验，卓越的规划、组织、策划、方案执行和团队领导能力，积累较强的人际关系处理能力和商务谈判技巧，善于沟通，具备良好的合作关系掌控能力与市场开拓能力；,敏感的商业和市场意识，具备优秀的资源整合能力、业务推进能力；,思维敏捷，有培训演讲能力，懂激励艺术，能带动团队的积极性；,擅长协调平衡团队成员的竞争与合作的关系，善于通过培训提高团队综合能力和凝聚力。,自我评价,拥有多年的市场管理及品牌营销经验，卓越的规划、组织、策划、方案执行和团队领导能力，积累较强的人际关系处理能力和商务谈判技巧，善于沟通，具备良好的合作关系掌控能力与市场开拓能力；,敏感的商业和市场意识，具备优秀的资源整合能力、业务推进能力；,思维敏捷，有培训演讲能力，懂激励艺术，能带动团队的积极性；,擅长协调平衡团队成员的竞争与合作的关系，善于通过培训提高团队综合能力和凝聚力。,自我评价,计算机四级证书,大学英语四、六级证书,(CET-4，CET-6),所获证书,计算机四级证书,大学英语四、六级证书,(CET-4，CET-6),所获证书,通过全国计算机二级考试，熟练运用office相关软件。,熟练使用绘声绘色软件，剪辑过各种类型的电影及班级视频。,大学英语四/六级（CET-4/6），良好听说读写能力，快速浏览英语专业书籍。,掌握技能,通过全国计算机二级考试，熟练运用office相关软件。,熟练使用绘声绘色软件，剪辑过各种类型的电影及班级视频。,大学英语四/六级（CET-4/6），良好听说读写能力，快速浏览英语专业书籍。,掌握技能,2016年,新安职业技术学院自强社“优秀社员”,2015年,三下乡”社会实践活动“优秀学生”,2015年新安职业技术学院学生田径运动会10人立定跳远团体赛第三名,2015年,新安职业技术学院盼盼杯烘焙食品创意大赛优秀奖,2014年,新安职业技术学院“点燃中华梦,畅享我青春”微博文征集大赛二等奖,奖项荣誉,2016年,新安职业技术学院自强社“优秀社员”,2015年,三下乡”社会实践活动“优秀学生”,2015年新安职业技术学院学生田径运动会10人立定跳远团体赛第三名,2015年,新安职业技术学院盼盼杯烘焙食品创意大赛优秀奖,2014年,新安职业技术学院“点燃中华梦,畅享我青春”微博文征集大赛二等奖,奖项荣誉'
    items = {}
    items['items'] = [params]
    try:
        nlp_client = CMSSEcloudNlpClient(accesskey, secretkey, url)
        response = nlp_client.request_nlp_service(requesturl, items)
        print(response.text)
    except ValueError as e:
        print(e)   
        

if __name__ == "__main__":
    # request_sentiment_wb()
    # request_sentiment_forum()
    # request_sentiment_news()
    # request_sentiment_genative()
    #
    # request_segmentation()
    #
    # request_keyswords()
    #
    # request_announcement()
    #request_convertdoc()

    # request_industry()
    # request_filter()
    # request_viewpoint()
    # request_rumor()
    # request_text_similarity()
    request_theme_matcher()
    #
    # request_emotion()
    # request_wbemotion()
    #
    # request_entity()
    # request_location()
    # request_transmit()
    # request_warningfilter()
    # request_rumorfeature()