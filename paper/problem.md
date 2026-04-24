Large Language Models (LLMs) are increasingly deployed as autonomous agents for real-world decision-making tasks, including email triage, customer support, and workflow 
automation. While these systems demonstrate strong reasoning capabilities, they often exhibit unreliable behavior in multi-step pipelines, such as inconsistent outputs,
hallucinated responses, and failure to recover from intermediate errors.

In practical applications like email orchestration, such failures can lead to incorrect classification, improper prioritization, and low-quality or unsafe responses. 
These issues arise because standard LLM-based agents typically lack structured mechanisms for stateful reasoning, explicit evaluation, and controlled error recovery.

Despite growing adoption of agentic systems, there remains limited empirical understanding of how architectural components such as memory, deterministic evaluation, 
and fallback strategies influence system reliability. Most existing implementations rely on prompt engineering and heuristic design, without systematic evaluation of their
impact on robustness and consistency.

This work addresses this gap by investigating how introducing memory-aware workflows, deterministic grading mechanisms, and fault-tolerant fallback strategies can improve
the reliability of LLM-based agents in multi-step decision-making environments. Using an email orchestration task as a representative real-world scenario, we design and 
evaluate multiple agent architectures to quantify their impact on accuracy, consistency, and failure recovery.
