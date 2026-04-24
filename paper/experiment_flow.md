# 🧪 Experiment Pipeline

Each system is evaluated using the same dataset and follows a standardized evaluation process to ensure fairness and reproducibility.

---

## 📌 Evaluation Workflow

1. **Load Dataset**  
   - The dataset is loaded from `data/email_dataset.json`

2. **Iterate Over Inputs**  
   For each email in the dataset:
   - Pass the input email to the agent  
   - Generate a structured output (category, priority, response, action)

3. **Compare with Ground Truth**  
   - Predicted outputs are compared against ground truth labels  
   - Evaluation is based on classification and prioritization correctness  

4. **Log Results**  
   - Store predictions and ground truth in logs for analysis  
   - Maintain structured records for reproducibility  

5. **Compute Metrics**  
   - Calculate Accuracy, Failure Rate, Consistency, and Recovery Rate  
   - Use standardized metric definitions from `evaluation.md`

---

## 🔁 Multi-System Evaluation

This pipeline is executed independently for each system variant:

- **Baseline System**  
- **Memory + Fallback System**  
- **Advanced Reflective System**

All systems are evaluated on the **same dataset** under identical conditions to ensure a fair comparison.

---

## 🎯 Objective

The goal of this experimental setup is to:
- Compare performance across different agent architectures  
- Measure improvements in reliability and robustness  
- Identify strengths and limitations of each system design  
