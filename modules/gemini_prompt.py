# modules/gemini_prompt.py
from vertexai.preview.generative_models import GenerativeModel
import vertexai

def extract_with_gemini(text: str) -> dict:
    """
    Geminiを使ってPDFから情報を抽出
    """
    ##FIXME: プロジェクトIDを設定
    vertexai.init(project="", location="us-central1")
    model = GenerativeModel("gemini-2.0-flash")

    prompt = f"""
    以下のテキストから、発行会社・金額・支払期日を抽出してJSON形式で出力してください。

    テキスト:
    {text}

    出力フォーマット:
    {{
      "vendor": "...",
      "tool": "...",
      "amount_excl_tax": "...",
      "amount_incl_tax": "...",
      "due_date": "YYYY-MM-DD"
    }}
    """
    response = model.generate_content(prompt)
    return response.text
