批量将oss域名的图片上传并替换
如
![img](https://cdn.nlark.com/yuque/0/2025/png/50542277/1749177958169-def3b3b1-ec1e-401c-9e65-b0f5dd4d140d.png)
上传替换为
http://oss.sundayhk.com/blog-pic/1749177958169-def3b3b1-ec1e-401c-9e65-b0f5dd4d140d.png


https://github.com/Molunerfinn/PicGo
启动PicGo客户端，配置OSS

命令测试上传
```
$ curl --location 'http://127.0.0.1:36677/upload' \
--header 'Content-Type: application/json' \
--data '{"list": ["https://cdn.nlark.com/yuque/0/2025/png/50542277/1749177958169-def3b3b1-ec1e-401c-9e65-b0f5dd4d140d.png"]}'

{"success":true,"result":["http://oss.sundayhk.com/blog-pic/1749177958169-def3b3b1-ec1e-401c-9e65-b0f5dd4d140d.png"]}
```

使用
```
python3  picgo_replace_md.py 目录/文件
```