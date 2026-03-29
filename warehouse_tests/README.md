# 仓库管理系统接口自动化测试

## 项目简介
本项目为仓库管理系统的库存模块（入库、出库）提供自动化测试，基于 pytest + requests 框架，支持数据驱动、日志、重试和持续集成。

## 技术栈
- Python 3.10+
- pytest
- requests
- PyYAML
- logging
- GitHub Actions

## 快速开始
1. 克隆仓库
2. 安装依赖：`pip install -r requirements.txt`
3. 修改 `config/config.yaml` 中的 `base_url` 为你的服务地址（如 `http://localhost:8080/api`）
4. 确保数据库中已有一条测试库存（stockId = `STOCK001`），或修改 `data/stock_data.yaml` 中的 `stockId` 为你已有的库存编号
5. 运行测试：`pytest tests/ -v`

## 测试报告
每次测试会自动生成日志文件 `logs/test.log`，CI 中可配置 HTML 报告。

## 项目结构
