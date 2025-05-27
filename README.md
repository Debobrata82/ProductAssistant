# 🛍️ Product Assistant – AI-Powered

**Product Assistant** is an AI application that delivers concise product summaries and real-time estimated prices in USD using cutting-edge Large Language Models (LLMs). Built with **LangChain** framework, **LangSmith** for Tracing and Observability and **OpenAI/Groq** LLM model, it's perfect for quick product query and market price estimation.

---

## 📌 Features

- ✅ Accepts any product name input
- 🧠 Utilizes GroQ LLMs model - "gemma2-9b-it"  for intelligent responses
- 📦 Returns structured JSON with:
  - **Product Name**
  - **Product Description**
  - **Product Price** in **USD**
- 🔐 Supports multiple API providers via `.env` config

---

## 🖼️ Sample Output

```json
{
"product_name": "LG C2 OLED 65-inch TV",
"product_details": "The LG C2 OLED 65-inch TV is a premium television featuring a 65-inch OLED display with 4K resolution and HDR support. It boasts incredible picture quality with deep blacks, vibrant colors, and wide viewing angles.  The TV is powered by LG's α9 Gen 2 AI processor for enhanced image and sound processing. It also supports various smart features, including webOS for easy access to streaming services and other content.",
"product_price": 1800
}
```
