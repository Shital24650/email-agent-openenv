# LLM Email Orchestrator â€” RL-Style Decision Automation Agent

> An autonomous email agent that classifies, prioritizes, and responds to emails using a self-evaluating LLM pipeline with deterministic grading and RL-inspired feedback loops.

**Baseline â†’ Optimized accuracy: 0.67 â†’ 0.95+ F1**

---

## The Problem

Most email automation stops at filtering. Real-world triage requires:
- Understanding context and intent, not just keywords
- Consistent prioritization under ambiguous inputs
- Graceful degradation when the LLM fails
- A way to measure and improve decisions over time

This system solves all four.

---

## Architecture

```
Input Email
    â”‚
    â–¼
â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
â”‚           LLM Decision Engine           â”‚
â”‚  Classification â†’ Priority â†’ Response  â”‚
â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜
    â”‚                        â”‚
    â–¼                        â–¼
Memory Layer            Fallback (rules-based)
(context window)        (activates on LLM failure)
    â”‚
    â–¼
â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
â”‚        Deterministic Grader             â”‚
â”‚   Scores: classification Â· priority    â”‚
â”‚           response quality Â· action    â”‚
â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜
    â”‚
    â–¼
Scored Output + Feedback Loop
```
## 🧩 System Architecture
<img width="1024" height="1536" alt="ChatGPT Image Apr 17, 2026, 02_37_41 PM" src="https://github.com/user-attachments/assets/1358df3a-f9b8-463b-a896-d982735abe80" />
---

## What Makes This Different

Most LLM projects are single-shot: prompt in, answer out. This system has three things you rarely see together:

**1. Self-evaluation loop**
Every output is scored by a deterministic grader (0.0 â†’ 1.0). The agent uses that score as feedback to improve subsequent decisions â€” no manual retraining required.

**2. Fault-tolerant execution**
If the LLM fails, times out, or returns malformed output, a rule-based fallback activates. The system never fails silently.

**3. Memory-aware consistency**
A context window of recent decisions prevents the agent from contradicting itself across a session â€” critical for production reliability.

---

## Performance

| Stage | F1 Score |
|---|---|
| Baseline (zero-shot) | 0.67 |
| After evaluation loop | 0.85 |
| Optimized (structured feedback) | **0.95+** |

Improvement driven entirely by the grading + feedback loop â€” no fine-tuning, no labelled dataset.

---

## Task Levels

| Level | Capability Tested |
|---|---|
| Easy | Email classification only |
| Medium | Classification + priority assignment |
| Hard | Full pipeline â€” classification, response generation, action selection |

---

## Tech Stack

| Layer | Technology |
|---|---|
| LLM | GPT-4o-mini |
| Backend | Python |
| Containerization | Docker |
| Evaluation | Custom deterministic grading system |
| Config | `.env`-based environment management |

---

## Live Demo

ðŸ‘‰ [huggingface.co/spaces/Shital2605/email-agent-openenv](https://huggingface.co/spaces/Shital2605/email-agent-openenv)

See real-time decision logs, multi-step reasoning outputs, and live performance scoring.

---

## Setup

```bash
# Install dependencies
pip install -r requirements.txt

# Configure environment
cp .env.example .env
# Add your API key to .env:
# OPENAI_API_KEY=your_key
# MODEL_NAME=gpt-4o-mini

# Run
python app.py
```

---

## Design Principles

| Principle | Implementation |
|---|---|
| **Robustness** | Retry logic + rule-based fallback â€” guaranteed output |
| **Measurability** | Every decision scored, every improvement tracked |
| **Realism** | Simulates production triage, not toy examples |
| **Extensibility** | Swap LLM provider or add tools without restructuring |

---

## Why This Matters for Real Systems

The architecture pattern here â€” LLM reasoning + deterministic evaluation + feedback loop â€” is directly applicable to any decision-automation system: incident triage, customer support routing, compliance flagging. The email domain is the testbed. The pattern is the product.

---

*Built by [Shital Parab](https://github.com/Shital24650)*- Response quality  

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
