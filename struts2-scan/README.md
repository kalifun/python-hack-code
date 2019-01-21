# Struts2-scan Frame
## 思路
```
--s Scan  后面可以接url直接检测，也可以接all，程序将会去scan-list目录查找txt后缀文件。并打开文件readlines，当检测有漏洞将会写入文件。
--u  当你已经知道url有漏洞，直接调用函数上传马
--a auto 自动，将从信息收集到漏洞检查，再到漏洞使用
```
## 使用模块
>#  argparse
```
都习惯使用sys.argv。但是未能对一些不太懂代码的人理解你的使用过程。
```
```python
    parser = argparse.ArgumentParser(description="Use this script")
    parser.add_argument("--s",type=str,metavar='Scan',default=None,help="--s http://xxxx or --s all  please put the file in the scan-list folder")
    parser.add_argument("--u",type=str,metavar='Use',default=None,help="--u http://xxxx or --u xxx.ini   If you know the vulnerability url,use url or file directly")
    parser.add_argument("--a",type=str,metavar='auto',default=None,help="--a baidu  or  google   choose the search engine you need to take advantage of")
    args = parser.parse_args()
```
### 其余就是正常加入函数。人太懒，写不下去了，又不敢利用别被抓了。感兴趣的可以补充补充。
```
███████╗████████╗ ██████╗  ██╗      ██╗████████╗███████╗              ██████╗ 
██╔════╝╚══██╔══╝ ██╔══██╗██║      ██║╚══██╔══╝██╔════╝              ╚════██╗
███████╗      ██║       ██████╔╝██║      ██║      ██║      ███████╗█████╗    █████╔╝
╚════██║      ██║       ██╔══██╗██║      ██║      ██║      ╚════██║╚════╝  ██╔═══╝ 
███████║      ██║       ██║    ██║╚██████╔╝      ██║      ███████║              ███████╗
╚══════╝      ╚═╝       ╚═╝    ╚═╝ ╚═════╝         ╚═╝      ╚══════╝              ╚══════╝
```
