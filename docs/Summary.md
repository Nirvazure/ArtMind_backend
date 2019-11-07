## 摘要

## Abstract

## 绪论

关键词：CNN,特征提取

### 研究背景

绘画的重要性
绘画是对人类精神世界的重要表达，体现着人类的精神追求，反映着时代的变化和发展。
我们通过美术作品认识不同时代，不同民族，不同文化，不同社会制度下人们的生活，历史，风俗，行为，观念等，甚至包括认识我们连自己在内的整个世界
流派分类的必要
艺术作品在形态和作品形式上有很大的差异，隶属于不同的美术门类，每个门类都有自己的艺术特点和形式规范，需要将其分成不同的门类，按照自己的艺术特点去鉴赏
作品产生的时代背景不同，作品也呈现出较大的差异

绘画的问题
绘画特征难以表达，易受人主观性的影响，每个画家在长期的艺术创作中都形成着各自鲜明的特点，这些风格特征时常显得抽象而难以形容，传统方法在对画作进行分析的时候主要是通过各种对图像进行预处理和各种变化在笔触，颜色，形态上提取特征，人工提取图像特征过程繁琐而复杂，需要更加专业的艺术背景，且抽离的图像只是图像的局部特征且包含了部分人的主观性，使得分类效果有时候并不能真正反映绘画之间的内在联系

为什么用这种方法
深度学习实质是一种特征学习方法． 原始数据通过一些简单、非线性的模型变换，成为更高层次的、更加抽象的表达，可以提升处理复杂分类问题时泛化能力，比浅层学习优势大，自动地从大量数据学习特征，更加精准地表征数据内部隐藏的丰富信息

为什么要用卷积网络：解决传统方法人工提取特征和细节丢失等问题其局部感受野和权值共享特性，减少了网络模型权值数量，从而降低了网络模型的复杂度．且卷积神经网络结构对平移、倾斜、比例缩放等变形拥有高度不变性，从而提高了分类识别的鲁棒性，提高运算效率。利用卷积神经网络发掘低层特征之间的联系，提取绘画图像特征，对得到的特征进行 PCA 降维、归一化等操作后，利用支持向量机(SVM)分类器进行分类

### 研究目的和意义

然而基于卷积神经网络，针对绘画题材进行分类的研究相对较少
绘画流派分类在学术界不好界定，本文提出的分类模型也许能提供思路
对美术史发展的过程提供重要意义
当代画家可以看看自己的作品与谁的相似

让模型的分类力求准确是一方面，对于预测错误的部分也有着相当的现实意义

1. 艺术品鉴赏分析
2. 来源不明的艺术信息推测
3. 基于内容的绘画风格推荐
4. 艺术风格自动分类识别

### 研究现状

1. 绘画流派分类

古代：图腾信仰
文艺复兴之前：画神 （中世纪）
文艺复兴：以神的名义画人 文艺复兴（静态人物）
文艺复兴后：单纯画人（肖像画）和写实风景：委拉斯凯兹，伦勃朗（荷兰西班牙）（奢靡洛可可，激情）
19 世纪：画风景（印象派）,浪漫主义（画英雄）
画梦境中的风景（超现实主义）
为了生活而创作（波普艺术）

这里的难点在于不同流派呈现不同风格的绘画特点，不同时期风格也有所不同，主义这种东西更多的是理念上的表达

2. 深度学习发展

传统方法:主要分为两个部分: 先提取图像特征，然后利用机器学习分类算法(PCA+SVM)进行分类．

- LAZEBNIK 等提出将图像分成若干子区域，分别计算每个子区域特征，后将所有子区域的特征拼接起来形成对自然场景的描述
- JIANG 等通过提取纹理特征和边缘大小直方图来建立对传统中国绘画图像的描述
- CAO 等提出应用 梯度直方图 HOG( Histogram of Oriented Gradient) 特征到运动车辆检测中

尺度不变特征转换 SIFT(Scale-invariant Feature Transform)
全局颜色直方图 HSV
笔触，形状
小波变换+隐含马尔科夫链
颜色特征
纹理特征提取（灰度共生矩阵）
颜色板熵、冗余度、有序度、复杂度
VGG-F 模型的深度结构可以从丰富的感知信息中提取复杂的结构并建立数据中内在的表征

深度学习方法

改卷积核
改网络宽度（网络结构）：传统卷积神经网络结构一般为串联结构，文考虑在传统串联网络结构的基础上，在两个卷积层之间并联一个卷积层，以增加网络结构宽度，实现多种特征融合，提高网络分类性能
增加少量样本
选激活函数讲激活函数

### 论文主要工作

利用错误样本的特性提升性能

本课题现支持的流派包括
写实主义
印象派（后印象派包含在印象派之中）
超现实主义
抽象派

#### 研究内容

#### 研究方法

#### 实施方案

系统以 WEB 应用的模式展示
在本课题的系统实现过程中，前端采用目前流行的前端框架 Vue.js，使用 MVVM 模式实现前端逻辑与数据的分离
vue.js 讲一些
后端采用 Python 作为后台逻辑处理
本课题使用的算法在流行机器学习框架 PyTorch 下构建

### 论文组织架构

## 相关理论基础

PCA
SVM
图像处理
CNN 特性提取
InceptionV4
基于内容和协同过滤的混合推荐

### 自己的工作

##

##

## 总结展望

### 工作总结

本文的创新点在于针对绘画流派分类的问题，提出了，在得到了

### 未来展望

对于相当一部分绘画流派来说，由于持续的时间并不长，流派内作品在量级上无法达到深度学习的数量级要求
现有对艺术画进行分类的文献大多对整幅画作直接进行特征提取，但任何图像内容特征的可适应性都存在一定的局限性
艺术风格并不是用图像的 RGB 特征来表达的
同一个作家在不同时期也有不同的艺术流派(只针对作家特定时期的艺术流派)
抽象艺术和具象艺术之间怎么界定
要不要考虑分析绘画里面画了什么东西（人还是动物）

个人意见，不仅分类对的值得参考，其实分类错误的信息也是值得参考的

## 致谢

## 参考文献