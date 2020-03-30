艺术对人类有着特殊的意义
平台让作用规模化

要做什么？
AI 能力的艺术品整合系统（AI 线上艺术馆）

页面架构
1 广场（可以看别人发的）
2 我的
3 AI 小梵高

意义在哪？
目前还没有类似的平台
基础功能是线上的绘画数据博物馆，各种维度的检索功能
增值功能是基于平台数据的 AI 服务（API 和 WEB 界面交互两种）
潜在价值是数据的规模效应

可扩展（随时加入新的 AI 能力）
场景解决

1. 来源不明艺术品分析
2. 线下艺术馆的 AI 服务

干系人有谁？
每个人都是用户，但有一些人是认证用户，认证用户有额外的权限
普通用户可以访问平台中数据（查阅作家、作者资料，欣赏作品）
认证的用户拥有额外的权限，这个权限就是发布管理发布作品，发布动态，删除动态
系统的管理员可以管理系统中的数据和模型信息，添加 AI 能力

用户（博物馆认证）主页？
画家主页？

几个关键
整合全网的数据作品

为此需要
搭建数据、算法、交互一体的平台
具备可扩展 AI 能力
建立数据管理引擎

要做什么事？
API 怎么设计？
数据怎么更好的利用？
有哪些用户角色？认证机构可以发布作品
第一版提供哪些 AI 能力

目前收集了 3000，30 个画家
提供三种 AI 能力

后续的工作
完善数据自动化
利用运营等手段收集大规模数据
产生数据的规模效应
扩展 AI 能力
迭代数据模块引擎

画哪些类图
模型引擎（AI 能力接口）
服务端（AI 能力服务+数据接口）
交互前端（）

画哪些流程图
机构发布作品流程图
机构管理作品流程图
加入新的 AI 能力流程图（注册新的 AI 能力）

可以画一个状态机图
AI 服务的状态机

数据库实现
1 依靠 powerdesigner 直接生成数据库表
2 SQL-academy 与数据库连接
3 数据库封装操作

接口设计
作品数据接口（GET 都可以，POST、PUT、DELETE 要权限）
作家数据接口（GET 都可以，POST、PUT、DELETE 要权限）

流派分析 API（基本只有 GET，但是有配额设定）
场景：图像数据经过模型输出流派（这里用的是 TOP-3）
问题定位：多分类
选型：根据调查研究结果，VGG 和 Inception 的两种方法还是后者更好
画家推测 API（基本只有 GET，但是有配额设定）
情感分析 API（基本只有 GET，但是有配额设定）
时代推测 API（基本只有 GET，但是有配额设定）

画哪些顺序图

实体类差了一个展览表，

绘画有什么特征？
笔触、颜色特征、画面主体

在我这里的设定里面，Painter 应该都是 User

# API

## Moment 动态相关

GET /moments
获取所有瞬间

GET /moments/id
获取某条瞬间

POST /moments
发布某条瞬间
data：{

}
发布一条瞬间

## Painter 画家相关

GET /painters
获取画家
params:{
id/ 根据 id 筛选
}

PUT /painters/id
修改画家信息
data:{name=''leonard}

DELETE /painters/id
Accept：aplication/json
删除画家

## Craft 作品相关

POST /crafts/
场景：认证用户可以上传作品，需要权限

GET /crafts
场景：筛选各个数据维度的相关作品

## Exhibition 展览相关

## Analyse 分析相关

GET /analyse/era
传入参数：Image

GET /analyse/style
传入参数：Image

GET /analyse/painter
传入参数：Image

const params = {
image: image,
u_id: user_id,
m_id: model
};
function getCraftStyle() {
return axios.get("/analyse/style", { params: params });
}
function getCraftEra() {
return axios.get("/analyse/era", { params: params });
}
function getCraftPainter() {
return axios.get("/analyse/painter", { params: params });
}
axios
.all([getUserAccount(), getUserPermissions()])
.then(axios.spread(function(acct, perms) {}));

# 论文写作要点

1. 应用场景具体清晰
2. 主体人或者组织要行为明确
3. 要考虑呈现方式（WEB）
4. 涉及算法要加入指标性对比
5. 研究方法不能太单一

VGG 哪里好？
VGG-F 模型的深度结构可以从丰富的感知信息中提取复杂的结构并建立数据中内在的表征

如果是产品
多终端
可扩展 AI 能力

测试的话
测试环境
测试方法
测试结果
测试评估
