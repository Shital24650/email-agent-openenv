To investigate the impact of different architectural components on agent reliability, we design and evaluate three distinct system variants:

Baseline System (System A): A stateless LLM agent that performs classification, prioritization, and response generation without memory, evaluation, or fallback mechanisms.

Memory + Fallback System (System B): An enhanced agent that incorporates contextual memory, rule-based fallback logic, and deterministic scoring for evaluating outputs.

Advanced Reflective System (System C): A further extension that introduces a critic-based self-reflection mechanism, confidence estimation, and iterative retry strategies to improve output quality and robustness.

Each system is evaluated under identical conditions using a controlled dataset of email inputs to ensure fair comparison
