## 前言
在学习cobalt strike内容时，涉及到dns的内容比较多，于是做了抓取dns包的实验，在此记录下，以便以后查阅
## 实验环境
* 系统: kali 2020
* ip: 192.168.42.100
* 自建dns服务器: docker镜像jpillora/dnsmasq
* 抓包工具：kali中wireshark

## 具体步骤
#### 1. 在kali上搭建dns服务
```
root@kali:/home/kali/test# cat dnsmasq.conf
log-queries
#定义主机与IP映射
address=/target.test.com/192.168.42.100
address=/r1.test.com/192.168.42.100

root@kali:/home/kali/test#  docker run --name dnsmasq -d -p 53:53/udp -p 8080:8080 -v /home/kali/test/dnsmasq.conf:/etc/dnsmasq.conf --log-opt  "max-size=100m" -e "HTTP_USER=admin" -e "HTTP_PASS=admin" --restart always jpillora/dnsmasq
# 8080端口是dns服务的管理面板
```
以下是dns管理面板
![Alt text](../../image/dns-dashboard.png)

#### 2. 为kali设置dns地址
```
root@kali:/home/kali/test# cat /etc/resolv.conf 
#nameserver 192.168.42.129  # 修改之前的配置
nameserver 127.0.0.1        # 新增
nameserver 192.168.42.100   # 新增
```
#### wireshark抓包
