Each system is evaluated using the same dataset and follows this process:

1. Load dataset from email_dataset.json

2. For each email:
        Pass input to agent
        Generate structured output

3. Compare output with ground truth

4. Store results in logs

5. Compute evaluation metrics

This pipeline is repeated for all system variants to ensure fair comparison.
