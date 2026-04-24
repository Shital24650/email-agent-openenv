To systematically evaluate agent performance, we define the following metrics:

Accuracy: Measures correctness of classification and prioritization decisions relative to ground truth labels.

Failure Rate: Percentage of outputs that are incorrect, incomplete, or unusable in a practical setting.

Consistency: Measures output stability by evaluating whether repeated runs on identical inputs produce consistent results.

Recovery Rate: Quantifies the effectiveness of fallback mechanisms in correcting failures during intermediate steps.

These metrics enable a comprehensive assessment of both correctness and robustness across different agent architectures.

Metric Computation

To ensure reproducibility and consistency, each metric is computed using the following methodology:

1. Accuracy

Accuracy is calculated as the proportion of correctly predicted outputs compared to the ground truth.

Accuracy = Number of Correct Predictions / Total Number of Samples

A prediction is considered correct only if:

The category matches the ground truth
The priority matches the ground truth

2. Failure Rate

Failure rate measures the proportion of outputs that are incorrect, incomplete, or unusable.

Failure Rate = Number of Failed Outputs / Total Number of Samples

An output is considered a failure if:

The category or priority is incorrect
The response is missing, irrelevant, or low quality
The output format is invalid or incomplete

3. Consistency

Consistency evaluates whether the system produces stable outputs for identical inputs.

Method:

Each input is executed 3 times
Outputs are compared across runs
Consistency = Number of Consistent Outputs / Total Number of Inputs

An output is considered consistent if:

All runs produce identical structured results (category, priority, action)

4. Recovery Rate

Recovery rate measures the effectiveness of fallback mechanisms in correcting failures.

Recovery Rate = Number of Failures Corrected by Fallback / Total Number of Failures

A failure is considered “recovered” if:

The initial output is incorrect
The fallback mechanism produces a correct final output
🧪 Evaluation Procedure

The evaluation process is conducted as follows:

Each system variant (Baseline, Memory + Fallback, Advanced Reflective) is tested on the same dataset
For each input:
The agent generates a structured output
Outputs are logged for analysis
Metrics are computed using the definitions above
Results are aggregated and compared across systems to analyze improvements in reliability, consistency, and robustness
