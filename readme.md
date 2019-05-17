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
- [ ] 训练集测试集构成  涉及文中 face profiling 

# 5.10
### 未同步
# 5.13
- [x] 转移到mac
- [x] id任务 *已开头，这周内做出视频demo*

# ID 和 EXPRESSION分离出来
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
- [ ] 标数据
- [x] 网络输出param到vertices的转换 *代码基本看懂 *
- [ ] 阅读paper看一下训练集的准备 可能是ibug的自带的 \delta P 
# 5.17
- [x] 数据集整理 -[x]300W -[ ] AFLW 
- [x] rendering obama 文件-> mat
- [ ] param 写出

# IK
- [ ] 4篇papaer 重点IJCAI
- [x] 重读了ik review *1）主要强调以往的工作比较 2）**工作量较少问题** 考虑加入attention继续优化* 
