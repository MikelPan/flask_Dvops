#### 任务调度系统
主要实现服务器主机上任务调度,修改配置信息
#### 部署
```shell
## 拉取代码
git clone https://github.com/gitplyx/flask_Dvops.git
## 前端
# 安装node
wget https://nodejs.org/dist/v10.16.3/node-v10.16.3-linux-x64.tar.xz -C /usr/local/src && tar zxvf node-v10.16.3-linux-x64.tar.xz
ln -s node-v10.16.3/bin/node /usr/bin/node
ln -s node-v10.16.3/bin/npm /usr/bin/npm
npm install -g cnpm --registry-https://registry.npm.taobao.org
# 构建项目
cnpm install vue-cli -g
vue init webpack flask_devops_front
npm run build
npm run dev
# 启动项目
cd flask_devops_front
## 后端
# 安装python
# 运行项目
cd flask_devops_backhand
pip install -t requirements.txt
python manager.py 
```
