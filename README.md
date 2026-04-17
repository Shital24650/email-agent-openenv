# 📧 RL-Based AI Email Orchestrator Agent

## 🚀 Overview

This project implements a **production-style AI email agent** that autonomously processes and manages incoming emails using LLM-driven decision-making combined with deterministic evaluation.

The system simulates **real-world email triage workflows**, where reliability, consistency, and fallback mechanisms are critical.

### ✅ Core Capabilities
- Email classification → *work, spam, personal*  
- Priority assignment → *high, medium, low*  
- Context-aware response generation  
- Action selection → *reply, ignore, escalate*  

---

## 🧩 System Architecture
<img width="1024" height="1536" alt="ChatGPT Image Apr 17, 2026, 02_37_41 PM" src="https://github.com/user-attachments/assets/1358df3a-f9b8-463b-a896-d982735abe80" />


---

## 🧠 Key Features

### 🔹 LLM-Orchestrated Decision Engine
Uses an LLM to perform multi-step reasoning across classification, prioritization, and response generation.

### 🔹 Memory-Aware Workflow
Maintains recent decision context to ensure consistency across multiple emails.

### 🔹 Fault-Tolerant Design
Implements retry logic and a rule-based fallback system to ensure the agent **never fails silently**.

### 🔹 Deterministic Evaluation (RL-style)
Custom grading system evaluates:
- Classification accuracy  
- Priority correctness  
- Response quality  

This enables **measurable performance improvement**, similar to reinforcement learning feedback loops.

---

## ⚙️ Workflow

1. Input email is parsed  
2. LLM performs reasoning and generates structured output  
3. System assigns:
   - Category  
   - Priority  
   - Response  
   - Action  
4. Memory layer updates context  
5. Fallback activates if LLM fails  
6. Output is scored using deterministic grading  

---

## 📊 Reward System

- Score Range: **0.0 → 1.0**  
- Encourages:
  - Accurate classification  
  - Correct prioritization  
  - High-quality, human-like responses  
- Penalizes:
  - Incorrect decisions  
  - Low-quality outputs  

---

## 🧪 Tasks

| Level   | Capability |
|--------|-----------|
| Easy   | Classification |
| Medium | Classification + Priority |
| Hard   | Full pipeline (classification + response + action) |

---

## 🏆 Performance

- Baseline Score: **0.67**  
- Optimized Score: **0.95+**

Demonstrates strong improvements through structured evaluation and workflow design.

---

## 🛠️ Tech Stack

- **LLM:** GPT-4o-mini  
- **Backend:** Python  
- **Containerization:** Docker  
- **Evaluation:** Custom deterministic grading system  
- **Config:** `.env`-based environment management  

---

## ▶️ Live Demo

👉 https://huggingface.co/spaces/Shital2605/email-agent-openenv  

Run the agent to see:
- Real-time decision logs  
- Multi-step reasoning outputs  
- Final performance score  

---

## ⚙️ Setup

### Install dependencies
```bash
pip install -r requirements.txt
## ⚙️ Setup

```bash
pip install -r requirements.txt

Create a .env file:

OPENAI_API_KEY=your_api_key
MODEL_NAME=gpt-4o-mini

## ▶️ Run
python app.py

## 🎯 Design Principles

- **Robustness** → No crashes, guaranteed outputs  
- **Realism** → Simulates production email workflows  
- **Determinism** → Consistent and fair evaluation  
- **Extensibility** → Easy to plug in new tools/models  

---

## 📌 Key Highlights

- Combines **LLM reasoning + system design**, not just prompting  
- Implements **agent orchestration with memory and fallback**  
- Includes **evaluation loop (rare in most projects)**  
- Designed with **production reliability in mind**  
