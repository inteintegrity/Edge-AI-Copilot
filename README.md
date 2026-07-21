# 🤖 Edge AI Project Copilot

An AI-powered assistant that analyzes any Edge AI GitHub repository and automatically generates professional deployment guidance — covering hardware platforms, AI models, inference frameworks, and quick-start steps.

Built with **Streamlit** + **DeepSeek LLM**, designed for Edge AI engineers and customers who need to quickly understand how to deploy a project onto edge devices (RK3588, Jetson, Raspberry Pi, XIAO, ESP32, …).

---

## 📑 Table of Contents

- [✨ Features](#-features)
- [🏗️ Project Structure](#️-project-structure)
- [🚀 Quick Start](#-quick-start)
- [⚙️ Configuration](#️-configuration)
- [🧠 How It Works](#-how-it-works)
- [📦 Tech Stack](#-tech-stack)
- [📄 License](#-license)

---

## ✨ Features

- 🔗 **One-click repo analysis** — paste a GitHub URL and the app clones, scans, and analyzes it.
- 📂 **Folder tree visualization** — see the repository structure at a glance.
- 📑 **Important file extraction** — automatically loads `README.md`, `requirements.txt`, `Dockerfile`, `docker-compose.yml`, `pyproject.toml`.
- 🧠 **Edge AI keyword detection** — identifies supported hardware, AI models, inference frameworks, and deployment tooling.
- 🤖 **AI-generated report** — DeepSeek produces a Markdown report with project overview, supported hardware, AI models, deployment environment, quick start, potential issues, and optimization suggestions.

---

## 🏗️ Project Structure

```
Edge-ai-copilot/
├── app.py                  # Streamlit main application (UI + workflow)
├── core/
│   ├── analyzer.py         # Keyword-based repository analysis
│   ├── github.py           # Git repository cloning (GitPython)
│   ├── llm.py              # DeepSeek LLM integration
│   ├── parser.py           # Important file loader
│   └── scanner.py          # Folder tree scanner
├── .env.example            # Environment variable template
├── .gitignore
├── requirements.txt
└── README.md
```

---

## 🚀 Quick Start

### 1. Clone & install

```bash
git clone https://github.com/inteintegrity/Edge-ai-copilot.git
cd Edge-ai-copilot
pip install -r requirements.txt
```

### 2. Configure your API key

Copy the example env file and fill in your DeepSeek API key:

```bash
cp .env.example .env
# then edit .env and set DEEPSEEK_API_KEY=sk-xxxxxxxx
```

Get a key from <https://platform.deepseek.com/>.

### 3. Run the app

```bash
streamlit run app.py
```

The app opens at <http://localhost:8501>. Paste a GitHub repository URL and click **🚀 Analyze Repository**.

---

## ⚙️ Configuration

| Variable             | File     | Description                                  |
| -------------------- | -------- | -------------------------------------------- |
| `DEEPSEEK_API_KEY`   | `.env`   | DeepSeek API key for the LLM summary engine. |

> ⚠️ Never commit your real `.env`. It is git-ignored; only `.env.example` is tracked.

---

## 🧠 How It Works

```
GitHub URL
   │
   ▼
clone_repo()        ── GitPython clones the repo into ./cloned_repos/
   │
   ▼
scan_repo()         ── builds a folder tree (ignoring .git, __pycache__, …)
   │
   ▼
load_files()        ── extracts README.md, requirements.txt, Dockerfile, …
   │
   ▼
analyze_repository()── keyword scan across 4 categories:
   │                   • Hardware   (RK3588, Jetson, Raspberry Pi, ESP32, XIAO, …)
   │                   • AI Models  (YOLO, Whisper, PaddleOCR, SAM, …)
   │                   • Inference  (RKNN, TensorRT, ONNX, NCNN, TFLite, …)
   │                   • Deployment (Docker, docker-compose, Python, C++)
   ▼
generate_summary()  ── DeepSeek turns the analysis + README into a Markdown report
```

The report is rendered in the **📄 Summary** tab; the **🧠 Edge AI Analysis** tab shows the detected keywords grouped by category.

---

## 📦 Tech Stack

| Layer        | Technology                                   |
| ------------ | -------------------------------------------- |
| Web UI       | [Streamlit](https://streamlit.io/)           |
| Git cloning  | [GitPython](https://github.com/gitpython-developers/GitPython) |
| LLM          | [DeepSeek](https://www.deepseek.com/) (OpenAI-compatible API) |
| Env handling | python-dotenv                                |
| Language     | Python 3                                     |

---

## 📄 License

This project is provided as-is for educational and internal use. Feel free to fork and adapt it to your own Edge AI workflows.

---

# 中文说明

一个 AI 驱动的助手：输入任意 Edge AI 的 GitHub 仓库链接，自动分析并生成专业的部署指南，涵盖硬件平台、AI 模型、推理框架和快速上手步骤。

基于 **Streamlit** + **DeepSeek 大模型**，面向需要快速了解如何把项目部署到边缘设备（RK3588、Jetson、树莓派、XIAO、ESP32 等）的 Edge AI 工程师与客户。

## ✨ 功能特性

- 🔗 **一键分析仓库** —— 粘贴 GitHub 链接，应用自动克隆、扫描并分析。
- 📂 **目录树可视化** —— 一目了然地查看仓库结构。
- 📑 **关键文件提取** —— 自动加载 `README.md`、`requirements.txt`、`Dockerfile`、`docker-compose.yml`、`pyproject.toml`。
- 🧠 **Edge AI 关键词识别** —— 识别支持的硬件、AI 模型、推理框架和部署工具。
- 🤖 **AI 生成报告** —— DeepSeek 生成 Markdown 报告，包含项目概述、支持硬件、AI 模型、部署环境、快速上手、潜在问题与优化建议。

## 🚀 快速开始

### 1. 克隆并安装依赖

```bash
git clone https://github.com/inteintegrity/Edge-ai-copilot.git
cd Edge-ai-copilot
pip install -r requirements.txt
```

### 2. 配置 API 密钥

复制示例环境变量文件并填入你的 DeepSeek API 密钥：

```bash
cp .env.example .env
# 然后编辑 .env，设置 DEEPSEEK_API_KEY=sk-xxxxxxxx
```

密钥获取地址：<https://platform.deepseek.com/>。

### 3. 运行应用

```bash
streamlit run app.py
```

应用会在 <http://localhost:8501> 打开。粘贴一个 GitHub 仓库链接，点击 **🚀 Analyze Repository** 即可。

## ⚙️ 配置说明

| 变量                | 文件     | 说明                                  |
| ------------------- | -------- | ------------------------------------- |
| `DEEPSEEK_API_KEY`  | `.env`   | DeepSeek API 密钥，用于生成摘要报告。 |

> ⚠️ 切勿提交真实的 `.env` 文件。它已被 git 忽略，仓库只跟踪 `.env.example` 模板。

## 🧠 工作原理

```
GitHub 链接
   │
   ▼
clone_repo()        ── 用 GitPython 把仓库克隆到 ./cloned_repos/
   │
   ▼
scan_repo()         ── 生成目录树（忽略 .git、__pycache__ 等）
   │
   ▼
load_files()        ── 提取 README.md、requirements.txt、Dockerfile 等
   │
   ▼
analyze_repository()── 在 4 个类别中做关键词扫描：
   │                   • 硬件    （RK3588、Jetson、树莓派、ESP32、XIAO 等）
   │                   • AI 模型（YOLO、Whisper、PaddleOCR、SAM 等）
   │                   • 推理    （RKNN、TensorRT、ONNX、NCNN、TFLite 等）
   │                   • 部署    （Docker、docker-compose、Python、C++）
   ▼
generate_summary()  ── DeepSeek 把分析结果 + README 转成 Markdown 报告
```

报告显示在 **📄 Summary** 标签页；**🧠 Edge AI Analysis** 标签页按类别展示检测到的关键词。

## 📦 技术栈

| 层级     | 技术                                          |
| -------- | --------------------------------------------- |
| Web 界面 | [Streamlit](https://streamlit.io/)            |
| Git 克隆 | [GitPython](https://github.com/gitpython-developers/GitPython) |
| 大模型   | [DeepSeek](https://www.deepseek.com/)（OpenAI 兼容 API） |
| 环境变量 | python-dotenv                                 |
| 语言     | Python 3                                      |

## 📄 许可

本项目按原样提供，用于学习与内部使用。欢迎 fork 并改造为你自己的 Edge AI 工作流。
