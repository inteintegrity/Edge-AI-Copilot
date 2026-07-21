import os

from dotenv import load_dotenv
from openai import OpenAI

# 读取 .env
load_dotenv()

API_KEY = os.getenv("DEEPSEEK_API_KEY")
client = None
if API_KEY:
    client = OpenAI(
        api_key=API_KEY,
        base_url="https://api.deepseek.com"
    )


def generate_summary(analysis, files):
    """
    Generate repository summary using DeepSeek.
    """

    readme = files.get("README.md", "")

    # 防止 README 太长
    readme = readme[:6000]

    prompt = f"""
You are a senior Edge AI Application Engineer at Seeed Studio.

Please analyze the following GitHub repository.

Repository Analysis

Hardware:
{analysis.get("Hardware", [])}

AI Models:
{analysis.get("AI Models", [])}

Inference Framework:
{analysis.get("Inference", [])}

Deployment:
{analysis.get("Deployment", [])}

README:

{readme}

Please generate a professional report in Markdown.

The report should contain:

# Project Overview

Briefly describe the purpose of this repository.

# Supported Hardware

List supported hardware platforms.

# AI Models

List AI models used in the project.

# Deployment Environment

Summarize Python version, Docker, RKNN Toolkit,
dependencies or runtime requirements.

# Quick Start

Summarize the deployment steps.

# Potential Issues

List common deployment issues.

# Optimization Suggestions

Provide several suggestions for Edge AI deployment.
"""

    if client is None:
        return "# ❌ AI Analysis Failed\n\nDeepSeek API Key is not configured. Please set DEEPSEEK_API_KEY in your .env file."

    try:

        response = client.chat.completions.create(

            model="deepseek-chat",

            messages=[

                {
                    "role": "system",
                    "content": (
                        "You are an expert Edge AI Application Engineer. "
                        "Your job is to explain GitHub repositories clearly "
                        "for engineers and customers."
                    )
                },

                {
                    "role": "user",
                    "content": prompt
                }

            ],

            temperature=0.2,

            max_tokens=1500

        )

        return response.choices[0].message.content

    except Exception as e:

        return f"""
# ❌ AI Analysis Failed

Error:
{str(e)}


Please check:

- DeepSeek API Key
- Network connection
- API balance
- README size
"""