# 0x238E文档
##why?

## 车联网

### 实现的功能

1、SLAM识别->上传->行车轨迹的区块链->用户肖像-> 行车记录仪->车保险定价 
2、距离传感器 SLAM 车骨架分析。。。传感器 ->区块链上传数据->实时更新 决策（提醒）
3、机器无感支付->博弈 付费超车 指数增长特性-公平性

### demo 

用户界面 两个传感器的上链验证 规则

## 分工
1、yyw-zlw solidity SLAM开发
2、yz web3对接 前端 一个web
对于前端的一些网站
https://coursetro.com/posts/code/99/Interacting-with-a-Smart-Contract-through-Web3.js-%28Tutorial%29 basics
https://solidity.readthedocs.io/en/v0.4.24/contracts.html
https://remix.ethereum.org/ remix IDE
https://web3js.readthedocs.io/en/1.0/web3-eth-contract.html#new-contract web-3 
3、csh 树莓派距离传感器
具体可用doc
4、lyw 前端

##数据流
由于仅讨论车和局部网络的特性，以简化理解，用两辆车来讨论。
顶层  chain
数据生成层  传感器将数据收集到两辆车的IoT设备
数据共享层  IPFS(保证数据分布式)
数据呈现层  
![](./img/1.png)
