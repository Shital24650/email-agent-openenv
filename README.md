# 📧 Email Agent OpenEnv

## 🚀 Overview
This project implements an intelligent email agent designed to simulate real-world email triage.

The agent can:
- Classify emails → *work, spam, personal*
- Assign priority → *high, medium, low*
- Generate contextual responses
- Decide actions → *reply, ignore, escalate*

---

## 🧠 Key Features

### 🔹 LLM-Based Decision Making
Uses a language model to understand email context and make intelligent decisions.

### 🔹 Memory-Aware Reasoning
Maintains recent decision history to improve consistency across emails.

### 🔹 Robust Retry Mechanism
Handles API failures with retries to ensure stability.

### 🔹 Rule-Based Fallback (Critical)
Guarantees output even if the LLM fails — prevents crashes.

### 🔹 Deterministic Grading System
Evaluates performance based on:
- Category accuracy
- Priority accuracy
- Response quality

---

## 🎯 Tasks

| Level   | Description |
|--------|------------|
| Easy   | Classify email |
| Medium | Classify + assign priority |
| Hard   | Full handling (classification + response + action) |

---

## ▶️ How It Works

1. Click **Run Email Agent 🚀**
2. Agent processes multiple emails
3. Logs are displayed in real-time
4. Final score is generated

## 📊 Reward System

- Score Range: **0.0 → 1.0**
- Rewards correct classification and priority
- Encourages meaningful, human-like responses
- Penalizes incorrect or low-quality outputs

---

## ⚙️ Setup

```bash
pip install -r requirements.txt

Create a .env file:

OPENAI_API_KEY=your_api_key
MODEL_NAME=gpt-4o-mini

## ▶️ Run
python app.py

## 🏆 Performance
Baseline Score: 0.67
Final Score: 0.95+

## ✅ Design Goals
Robust (no crashes)
Realistic (production-like behavior)
Deterministic and fair evaluation
Easy to extend

## 📌 Notes
Works even if API fails (fallback system)
No hardcoded secrets (uses .env)
Stable and consistent scoring system
