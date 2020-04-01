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

尺度不变特征转换 SIFT(Scale-invariant Feature Transform)
全局颜色直方图 HSV
笔触，形状
小波变换+隐含马尔科夫链
颜色特征
纹理特征提取（灰度共生矩阵）
颜色板熵、冗余度、有序度、复杂度

深度学习方法

改卷积核
改网络宽度（网络结构）：传统卷积神经网络结构一般为串联结构，文考虑在传统串联网络结构的基础上，在两个卷积层之间并联一个卷积层，以增加网络结构宽度，实现多种特征融合，提高网络分类性能
增加少量样本
选激活函数讲激活函数

PCA
SVM
图像处理
CNN 特性提取
InceptionV4

对于相当一部分绘画流派来说，由于持续的时间并不长，流派内作品在量级上无法达到深度学习的数量级要求
现有对艺术画进行分类的文献大多对整幅画作直接进行特征提取，但任何图像内容特征的可适应性都存在一定的局限性
艺术风格并不是用图像的 RGB 特征来表达的
同一个作家在不同时期也有不同的艺术流派(只针对作家特定时期的艺术流派)
要不要考虑分析绘画里面画了什么东西（人还是动物）

个人意见，不仅分类对的值得参考，其实分类错误的信息也是值得参考的

后续的工作
API 授权认证
在一般的网页应用中，认证操作是经常要接收用户名和密码的，然后在 session 中保存用户 ID。用户的浏览器就会保存会话中的 ID 到 cookie 中。当用户在网站上访问需要认证授权的页面时，浏览器就会发送 cookie，应用程序就会查找 seesion 会话中的 ID（如果它没有失效的话），由于用户的 ID 保存在 seesion 中，用户就可以浏览页面了。

用这个 API，就可以使用 seesion 会话保存用户记录,但这毕竟不是最好的方法。有时候，用户想直接访问 API，或是用户想自己授权其他应用程序去访问这个 API。

解决方法是在认证的基础上使用秘钥。用户输入用户名和密码以登录，应用程序就以一个特殊秘钥返回给用户以备后续之需。这个秘钥可以通入应用程序，以至于如果用户想要选择拒绝应用更进一步的接入时，可以撤回这个秘钥。

其实，网上已经有一个做上面这件事的很流行的标准方式，叫做 OAuth（开放授权：是一个开放标准，允许用户让第三方应用访问该用户在某一网站上存储的私密的资源（如照片，视频，联系人列表），与以往的授权方式不同之处是 OAUTH 的授权不会使第三方触及到用户的帐号信息（如用户名与密码），即第三方无需使用用户的用户名与密码就可以申请获得该用户资源的授权，因此 OAUTH 是安全的。），特别的，标准第二版的 OAuth。网上有很多非常好的实现 OAuth 的资源，所以我才说那是超出此教程范围的。如果你正在使用 Ruby，这里有一些帮你解决大多数工作的很好的类库，比如 OmniAuth 。

花了那么多时间给你们讲解这个教程，希望对你们有所帮助。