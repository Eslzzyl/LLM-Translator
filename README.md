# LLM-Translator

一个基于大语言模型的翻译工具。编写此工具的主要原因是我需要一个像 Google 翻译那样简单易用的界面。本工具功能简单，但对大部分翻译场景已经足够。

## 使用方法

1. 克隆项目：
    ```bash
    git clone https://github.com/Eslzzyl/LLM-Translator.git
    cd ai-translator
    ```

2. 安装依赖：
    ```bash
    # 安装前，建议新建一个虚拟环境。
    conda create -n llmtranslator python=3.12 -y
    conda activate llmtranslator
    pip install -r requirements.txt
    ```

3. 配置环境变量：将 `start.sh`（或 `start.ps1`） 复制一份到 `start_private.sh`（或 `start_private.ps1`），并修改其中的环境变量值。

4. 运行：
    ```bash
    bash start_private.sh
    ```

    或
    ```powershell
    .\start_private.ps1
    ```

    然后打开终端中显示的链接。
