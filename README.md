# ★ SmartPick AI — Product Recommendation Agent

> An AI-powered product recommendation agent that suggests the best products based on user preferences, budget, reviews, and ratings — built with Python, Streamlit, and LLaMA 3.3 70B via Groq.

---

## What does it do?

SmartPick AI helps users find the **best products** in any category (phones, laptops, headphones, cameras, etc.) by:

- Taking user inputs: **category, budget, use case, and priority**
- Sending a smart prompt to **LLaMA 3.3 70B** (via Groq API)
- Returning **top N ranked recommendations** with pros, cons, ratings, price, and a buying verdict
- Displaying results in **beautiful, color-coded product cards** with a modern UI

---

## AI Model Used

| Model | Provider | Why |
|-------|----------|-----|
| LLaMA 3.3 70B Versatile | Groq | Free, fast, very accurate for product knowledge |

The agent uses **zero-shot prompting** with structured output parsing to generate consistent, detailed recommendations.

---

## Tech Stack

| Tool | Purpose |
|------|---------|
| Python 3.10+ | Core language |
| Streamlit | Interactive web UI |
| Groq API | LLM inference (free tier) |
| LLaMA 3.3 70B | Product recommendation model |

---

## Project Structure

```
📁 project/
├── app.py              # Main Streamlit app
├── requirements.txt    # Dependencies
└── README.md           # This file
```

---

## How to Run Locally

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Run the app
python -m streamlit run app.py

# 3. Open in browser: http://localhost:8501
```

You will need a **free Groq API key** from [console.groq.com](https://console.groq.com) — enter it in the sidebar.

---

## Deployment

**Live App:** [Add your Railway/Render link here after deploying]

**Deploy on Railway:**
1. Push this repo to GitHub
2. Go to [railway.app](https://railway.app) → New Project → Deploy from GitHub
3. Select your repo → Railway auto-detects Python
4. Add start command: `streamlit run app.py --server.port $PORT --server.address 0.0.0.0`
5. Add environment variable: `PORT=8501`
6. Done! Get your live link ✅

**Deploy on Render:**
1. Go to [render.com](https://render.com) → New Web Service
2. Connect GitHub repo
3. Build command: `pip install -r requirements.txt`
4. Start command: `streamlit run app.py --server.port 10000 --server.address 0.0.0.0`
5. Done! ✅

---

## Features

- 8 product categories (phones, laptops, headphones, cameras, smartwatches, monitors, gaming, power banks)
- Budget slider from ₹1,000 to ₹2,00,000
- 6 use case filters (gaming, business, student, fitness, creative, home)
- 4 priority options (rating, value, battery, camera, performance, design)
- 2–6 customizable result count
- Color-coded product cards with pros, cons, stars, tags, and verdict
- Modern navy + violet + teal color scheme (color theory applied)

---

## Author

**Nandini** — Alta AI Program Final Project  
*Submitted: Sunday, 12:00 noon*

---

## GitHub Repository

https://github.com/gantaNandini/smartpick-ai
