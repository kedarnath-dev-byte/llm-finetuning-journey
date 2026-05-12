# Video 01: Quiz and Interview Practice

## Purpose of This File

This file is for testing my understanding of Video 01: LLM Fine-Tuning Playlist Roadmap.

I will use this file to prepare for:

- Basic understanding
- Practical implementation thinking
- Interview answers
- High-package AI/GenAI roles
- Business and client-service thinking

---

# Part 1: Beginner-Level Questions

## Q1. What is fine-tuning?

### My Answer
Fine-tuning means taking a pretrained model and training it further on a specific dataset so that it performs better for a specific task, domain, tone, or business requirement.

---

## Q2. Why is fine-tuning important?

### My Answer
Fine-tuning is important because pretrained models are general. Companies often need models that understand their own domain, language, tone, output format, and workflow.

---

## Q3. What is a pretrained model?

### My Answer
A pretrained model is a model that has already learned general patterns from a large amount of data before being adapted to a specific task.

---

## Q4. What is transfer learning?

### My Answer
Transfer learning means using knowledge learned from one large/general task and applying it to another related task.

---

## Q5. What is the difference between pretraining and fine-tuning?

### My Answer
Pretraining teaches the model general knowledge from large data. Fine-tuning adapts that pretrained model to a specific task or domain.

---

# Part 2: Fine-Tuning vs RAG vs Agents

## Q6. What is RAG?

### My Answer
RAG means Retrieval-Augmented Generation. It gives the model external documents or knowledge during answering without changing the model weights.

---

## Q7. What is an AI agent?

### My Answer
An AI agent is a system that can use an LLM to reason, call tools, retrieve information, take actions, and complete workflows.

---

## Q8. When should I use RAG instead of fine-tuning?

### My Answer
I should use RAG when the main problem is missing or changing knowledge, such as company documents, PDFs, policies, or latest information.

---

## Q9. When should I use fine-tuning instead of only RAG?

### My Answer
I should use fine-tuning when the model needs to repeatedly follow a specific behavior, tone, format, domain vocabulary, or task style.

---

## Q10. When should I use agents?

### My Answer
I should use agents when the AI must take actions, use tools, call APIs, send messages, update systems, or complete multi-step workflows.

---

# Part 3: Practical Questions

## Q11. Why is Hugging Face important?

### My Answer
Hugging Face is important because it provides models, datasets, tokenizers, training tools, Transformers, PEFT, TRL, and other libraries useful for fine-tuning and deployment.

---

## Q12. What is quantization?

### My Answer
Quantization reduces model memory usage by storing model weights in lower precision formats like INT8 or INT4.

---

## Q13. Why is quantization useful?

### My Answer
Quantization is useful because it helps run large models on lower memory and cheaper hardware.

---

## Q14. What is LoRA?

### My Answer
LoRA is a parameter-efficient fine-tuning technique where we train small additional matrices instead of updating all model weights.

---

## Q15. What is QLoRA?

### My Answer
QLoRA combines quantization with LoRA so that large models can be fine-tuned using much less GPU memory.

---

# Part 4: Advanced Questions

## Q16. What is full fine-tuning?

### My Answer
Full fine-tuning means updating most or all weights of the model for a specific task.

---

## Q17. What is PEFT?

### My Answer
PEFT means Parameter-Efficient Fine-Tuning. It updates only a small number of trainable parameters instead of the full model.

---

## Q18. What is RLHF?

### My Answer
RLHF means Reinforcement Learning from Human Feedback. It is used to align model responses with human preferences.

---

## Q19. What is DPO?

### My Answer
DPO means Direct Preference Optimization. It is a simpler preference-alignment method compared to PPO-based RLHF.

---

## Q20. What is embedding fine-tuning?

### My Answer
Embedding fine-tuning means improving an embedding model so that it gives better vector representations for a specific domain or retrieval task.

---

# Part 5: High-Package Interview Questions

## Q21. 10 LPA Question: Explain fine-tuning simply.

### My Answer
Fine-tuning is like taking a generally smart student and training that student for a specific exam or job.

---

## Q22. 50 LPA Question: Why do companies fine-tune models?

### My Answer
Companies fine-tune models to make them better at their own domain, tone, output format, and business tasks.

---

## Q23. 1 Crore Question: How would you design a fine-tuning pipeline?

### My Answer
I would collect domain data, clean it, format it into instruction-response pairs, choose a base model, select LoRA/QLoRA or full fine-tuning, train the model, evaluate it, compare with baseline, deploy it, and collect feedback for improvement.

---

## Q24. 1.5 Crore Question: How do you choose between RAG and fine-tuning?

### My Answer
If the issue is knowledge access, I choose RAG. If the issue is behavior, tone, structure, or repeated task adaptation, I choose fine-tuning. In many enterprise systems, both are combined.

---

## Q25. 2 Crore Question: How would you build an enterprise AI platform using fine-tuning?

### My Answer
I would build a reusable GenAI platform with data ingestion, RAG pipelines, fine-tuning pipelines, model registry, evaluation dashboards, guardrails, monitoring, cost optimization, department-specific assistants, and feedback-based retraining.

---

# Part 6: Business Questions

## Q26. How can fine-tuning help education?

### My Answer
Fine-tuning can help create a personalized AI tutor that follows a school’s syllabus, teaching tone, local language, and revision method.

---

## Q27. How can fine-tuning or RAG help agriculture?

### My Answer
It can help create a farmer assistant that answers questions about crops, soil, weather, diseases, and government schemes in local language.

---

## Q28. How can RAG help CA offices?

### My Answer
RAG can help CA offices answer questions from GST, tax, compliance, and filing documents without manually searching every document.

---

## Q29. How can AI help legal professionals?

### My Answer
AI can summarize contracts, classify legal documents, retrieve case-law, and help lawyers review clauses faster.

---

## Q30. How can RLHF/DPO help coaching or healthcare assistants?

### My Answer
RLHF/DPO can help align the assistant to respond safely, politely, supportively, and according to human preferences.

---

# Part 7: My Weak Areas After Video 01

## Concepts I Need to Learn Deeply Later

- Actual model training process
- Tokenization
- Loss function
- Backpropagation
- Transformer architecture
- Hugging Face hands-on
- BERT fine-tuning
- T5 fine-tuning
- LoRA/QLoRA implementation
- Quantized model loading
- DPO implementation
- Embedding evaluation

---

# Part 8: Self-Score After Video 01

| Area | Score / 10 | Reason | Improvement Needed |
|---|---:|---|---|
| Concept Clarity | 3/10 | I know the roadmap and basic definitions | Need detailed concept videos |
| Hands-on Practice | 1/10 | Only notes started | Need notebooks and experiments |
| GitHub Documentation | 3/10 | Roadmap files created | Need clean README and commits |
| Interview Readiness | 2/10 | Basic Q&A prepared | Need deeper answers and practice |
| Resume Readiness | 1/10 | No hands-on proof yet | Need projects and notebooks |
| Business Thinking | 4/10 | Industry mapping started | Need MVP demos |

---

# Part 9: My Commitment

I will not only watch the playlist.

For every video, I will create:

- Notes
- Hands-on task
- GitHub proof
- Interview questions
- Resume bullet
- Industry mapping
- Business MVP idea
- Error logs and fixes
- Progress score