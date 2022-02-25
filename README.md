# 基于知识图谱的电影问答项目

## 开发工具
neo4j

pycharm

## 依赖包
py2neo

jieba

sklearn

flask

## 核心方法
获取自然语句 >> 问句分类 >> 查询语句转换

- 使用neo4j搭建知识图谱

- 使用朴素贝叶斯分类器进行问句分类

- 使用flask进行部署

## 心得体会
本项目是学习B站UP “跟若海写代码” 搭建的相同项目 视频课程地址：https://www.bilibili.com/video/BV1g3411E7Dh/?spm_id_from=333.788

重在学习整个项目得搭建流程，而非具体某一项技术

在本项目中学会了构建项目的三层架构 model层 service层 controller层，script目录管理脚本，以及common目录管理通用工具，能够条例清晰得构建项目

## 问题
- 因为没有学习过前端相关知识，故staic目录，template目录基本照搬UP代码，只能进行很小一部分的修改

- neo4j查询语句转化部分直接copy，并未进行过多的学习

- 该项目十分简单，如果为了学习更多关于知识图谱和问答相关的知识，该项目并不能满足
