> 每日清单书写规则
>1. 一级标题为每日列表和大任务
>2. 打钩为Done，斜体为标记的解决方案
# 5.7 
- [x] train.sh脚本运行错误 *training文件夹有误 loss求平均有误*
- [x] 读训练代码 *级联回归代码已经找到*
- [x] 3DDFA 文章第五章 未读 *已标注文中*
- [ ] 3DMM->68landmark 过程

# 5.8 
- [ ] PAC 如何project 重点是第一步映射 和 下一步的patch移动
- [ ] PNCC中有个z-buffer操作
- [ ] VDC WPDC 等 多出来操作 在代码中待找  顺着loss的定义 找一下输入的地方
- [x] 开题报告整理一下 *做出id无法稳定验证想法，继续修正result部分*

# 5.9 
- [x] .sh文件改写入py文件
- [x] training 文件
- [x] 训练集测试集构成  涉及文中 face profiling *未找到训练机准备代码*

# 5.10
### 未同步
# 5.13
- [x] 转移到mac
- [x] id任务 *已开头，这周内做出视频demo*
# exp id transfer loss
## **ID 和 EXPRESSION提取**
## 5.13
- [x] render文件和lighting文件
- [x] 整理render流程 需要重新看一下 total paper
- [x] paper里有3d纹理蒙皮的 找出代码 *github mesh solution cpythond代码*
## 5.14
- [ ] render 整理成一个py文件
- [x] triangle 待实验('tri_refine')
## 5.15
- [x] triangles 和 vertices 依然不匹配 
> 试验过所有可能 main文件 和demo文件 visualize的triangle完全不同；tri_refine文件应该为neck——remove的结果 但没有代码（待找） *main文件预测的vertices和用的tri.mat文件也无法render？？* **解决方案：重新训练模型，找出训练的运用的triangle和vertices再render试试看**
- [x] train的target从哪里得到 怎么做这个loss-> 找到运用的triangle *target 为已经计算好的矩阵 不涉及triangle的原型*
- [x] main文件用自己的训练模型
## 5.16
- [x] 修复render自己predict的vertices文件和triangles文件 *下标错误*
- [x] 标数据
- [x] 网络输出param到vertices的转换 *代码基本看懂 *
- [ ] 阅读paper看一下训练集的准备 可能是ibug的自带的 {delta} P
## 5.17
- [x] 数据集整理
> - [x] 300W
> - [ ] AFLW
- [x] rendering obama 文件-> mat
- [x] param 写出
## 5.24
- [x] render cpp 文件的trianglebug 
## **render vertices**
## 5.27
- [x] photo loss 的 render 原rgb至新图像
## 5.28
- [x] lighting 论文待看 **暂时放空 用mean替代**
- [x] BFM 用的地方 与渲染时用的
- [x] texture map 生成
- [x] MVF 中 直接映射
## 5.29 
- [x] main 文件验证映射
## 5.30
- [x] render 文件跑通
## **re render**
## 5.31
- [ ] vertices 和 colors 关系表 求mean（具体到是否为NA）
- [ ] exp 迁移 需要vertices重新渲染
- [x] 68 landmark -> vertices exclude in Zhu.paper *应该就是keypoint*
## 6.1
- [ ] 如何 68landmark 找出 occluded point *mvf中 多出的filter工作 为了精确edge 不好实现*
## 6.3
- [x] colors 的求解仍需优化
## 6.4 6.5 6.6
- [x] 变换坐标系去求最小的z轴*逆矩阵已确定 先乘一个转置矩阵*
- [x] 找鼻子那个vertices  *inference if label 中还未调试好***27-35为鼻梁 30鼻尖**
- [ ] 通过鼻子的左右去判断属于左还是右
- [x] 算出keypoint最靠左或右的旋转坐标系后的原始z轴 
## 6.10
- [x] 已算出colors矩阵 *待求解序列图片的mean color*
## 6.11
- [x] 修复旋转矩阵求解bug
- [x] mean colors 计算好了 vertices具体对应pixel待求解
## 6.13
- [x] mean colors的render通过原始x轴进行比较 **需要在加入在z轴上上的变换后的z轴比较 感觉是精度不够问题** *解决了 vertices没有转置*
- [ ] 光流模型运行 加入render进行比较 
## 6.14
- [x] pytorch版本不适应
## 6.15
- [x] photoloss 原文
- [x] photoloss 定义
## 6.17
- [x] bfm remove neck *新的tri模型已写好 训练不改动 render时改动*
## **network build & training**
## 6.18
- [ ] training  add pwcnet
- [ ] loss modificate *loss 基本为 3dmm param  target为？？？*
# IK
- [ ] 4篇papaer 重点IJCAI
- [x] 重读了ik review *1）主要强调以往的工作比较 2）**工作量较少问题** 考虑加入attention继续优化* 
- []
## 待做
 - [ ] 3DMM重新训练
 - [ ] 用gan做图片的render