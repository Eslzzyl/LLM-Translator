# LLM-Translator

一个基于大语言模型的翻译工具。编写此工具的主要原因是我需要一个像 Google 翻译那样简单易用的界面。本工具功能简单，但对大部分翻译场景已经足够。

## 使用方法

1. 克隆项目：
    ```bash
    git clone https://github.com/Eslzzyl/LLM-Translator.git
    cd ai-translator
    ```

2. 安装依赖：
    a. 使用 `conda` 和 `pip`：
    ```bash
    # 安装前，建议新建一个虚拟环境。
    conda create -n llmtranslator python=3.12 -y
    conda activate llmtranslator
    pip install -r requirements.txt
    ```

    b. 使用 `uv`：

        这一步可以跳过。

3. 配置环境变量：在项目目录中新建一个 `.env` 文件，按照以下模板填入内容：
    ```
    OPENAI_API_KEY=""
    OPENAI_API_BASE=""
    OPENAI_MODEL=""
    APP_PORT=3000
    ```

4. 运行：
    a. 使用 `conda` 和 `pip`：

        ```bash
        python main.py
        ```

    b. 使用 `uv`：

        ```bash
        uv run main.py
        ```

    然后打开终端中显示的链接。
