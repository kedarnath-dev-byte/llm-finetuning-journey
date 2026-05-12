# Video 02: Quiz

## Purpose of This File

This quiz tests my understanding of Video 02: Detailed Introduction to Fine-Tuning.

The goal is to check whether I understood:

- Model training
- Pretraining
- Foundation models
- Transfer learning
- CNN pretraining
- LLM pretraining
- MLM vs CLM
- Self-supervised learning
- ResNet/BERT pretrained demos
- Job and business applications

---

# Part 1: Beginner-Level Questions

## Q1. What is model training?

### My Answer
Model training means teaching a model to learn patterns from data so it can make predictions on new inputs.

---

## Q2. What is the model-building pipeline?

### My Answer
The model-building pipeline includes data collection, data analysis, data preprocessing, model training, and model evaluation.

---

## Q3. What is pretraining?

### My Answer
Pretraining means training a model on a huge general dataset before adapting it to a specific task.

---

## Q4. What is a pretrained model?

### My Answer
A pretrained model is a model that has already learned general patterns from large-scale data.

---

## Q5. What is a foundation model?

### My Answer
A foundation model is a pretrained model that can be reused for many downstream tasks.

---

# Part 2: Transfer Learning and Fine-Tuning

## Q6. What is transfer learning?

### My Answer
Transfer learning means reusing knowledge learned from one task or dataset for another related task.

---

## Q7. What is fine-tuning?

### My Answer
Fine-tuning means adapting a pretrained model further on a specific dataset, task, domain, tone, or output format.

---

## Q8. What is the difference between pretraining and fine-tuning?

### My Answer
Pretraining creates general knowledge using huge data. Fine-tuning adapts that general knowledge to a specific task.

---

## Q9. Why do we use pretrained models instead of training from scratch?

### My Answer
Because training from scratch needs huge data, compute, time, and money. Pretrained models already know useful patterns.

---

## Q10. What are common ways to adapt a pretrained model?

### My Answer
We can use it as-is, replace the final layer, freeze early layers and train later layers, or fine-tune selected layers.

---

# Part 3: CNN Pretraining

## Q11. What is CNN?

### My Answer
CNN stands for Convolutional Neural Network. It is mainly used for image-related tasks.

---

## Q12. What is ImageNet?

### My Answer
ImageNet is a large image dataset used to train and evaluate computer vision models.

---

## Q13. What do early CNN layers learn?

### My Answer
Early CNN layers learn primitive features like edges, lines, corners, and basic textures.

---

## Q14. What do deeper CNN layers learn?

### My Answer
Deeper CNN layers learn task-specific features like faces, eyes, wheels, or object identity.

---

## Q15. Why do we freeze early CNN layers?

### My Answer
Because early layers learn general features that are useful for many image tasks, so we do not need to retrain them.

---

# Part 4: NLP and Transformer Evolution

## Q16. What were RNN/LSTM used for?

### My Answer
RNN and LSTM were used for sequence data such as text classification, summarization, question answering, generation, and translation.

---

## Q17. Why did RNN/LSTM struggle?

### My Answer
They struggled with long-term dependencies, slow sequential processing, and computational inefficiency.

---

## Q18. Why are Transformers important?

### My Answer
Transformers use self-attention, scale better, handle sequence relationships more efficiently, and became the backbone of modern LLMs.

---

## Q19. What is self-attention?

### My Answer
Self-attention allows a model to understand relationships between tokens in a sequence by attending to different positions in the input.

---

## Q20. Which models came after Transformer architecture?

### My Answer
Models like BERT, GPT, T5, XLNet, LLaMA, Mistral, and Gemini-style models are based on transformer ideas.

---

# Part 5: LLM Pretraining

## Q21. What is LLM pretraining?

### My Answer
LLM pretraining means training a transformer-based language model on massive text data using objectives like next-token prediction or masked-word prediction.

---

## Q22. What is a tokenizer?

### My Answer
A tokenizer converts raw text into tokens or token IDs that the model can process.

---

## Q23. What is Masked Language Modeling?

### My Answer
Masked Language Modeling is a task where a model predicts a masked word in a sentence. It is used in BERT.

---

## Q24. What is Causal Language Modeling?

### My Answer
Causal Language Modeling is a task where a model predicts the next token using previous tokens. It is used in GPT-style models.

---

## Q25. What is span masking?

### My Answer
Span masking means masking and predicting a group of tokens or phrase. It is used in T5-style models.

---

# Part 6: MLM vs CLM

## Q26. Which model uses MLM?

### My Answer
BERT uses Masked Language Modeling.

---

## Q27. Which model uses CLM?

### My Answer
GPT-style models use Causal Language Modeling.

---

## Q28. Which objective is better for generation?

### My Answer
Causal Language Modeling is better for generation because it trains the model to predict the next token.

---

## Q29. Which objective is useful for understanding tasks?

### My Answer
Masked Language Modeling is useful for understanding tasks like classification, NER, and sentence understanding.

---

## Q30. Why did CLM become very powerful?

### My Answer
Because by predicting the next token repeatedly on huge text, the model learns grammar, facts, reasoning, style, and conversation patterns.

---

# Part 7: Self-Supervised Learning

## Q31. What is self-supervised learning?

### My Answer
Self-supervised learning means labels are automatically created from the data itself.

---

## Q32. Why is LLM pretraining self-supervised?

### My Answer
Because the model creates training targets from raw text, such as predicting the next token or masked token, without manual labeling.

---

## Q33. Give one example of self-supervised learning.

### My Answer
In the sentence “Sunny is an AI master,” the input can be “Sunny is an AI” and the label can be “master.”

---

## Q34. Why is self-supervised learning important?

### My Answer
It allows models to learn from massive raw data without requiring humans to manually label everything.

---

# Part 8: Practical Demo Understanding

## Q35. What did the ResNet demo show?

### My Answer
It showed that a pretrained ResNet model can classify images directly without training again.

---

## Q36. What did the BERT demo show?

### My Answer
It showed that pretrained BERT can predict a masked word in a sentence, such as predicting “Paris” for “The capital city of France is [MASK].”

---

## Q37. Why is the BERT tokenizer needed?

### My Answer
The tokenizer converts text into token IDs and input format that BERT can understand.

---

## Q38. Why did the tomato image prediction not exactly give tomato?

### My Answer
Possibly because the exact tomato class may not be present in the pretrained ImageNet labels, so the model predicted visually related classes.

---

# Part 9: High-Package Reflection Questions

## Q39. 10 LPA Question: Explain pretraining in simple words.

### My Answer
Pretraining is like giving a model general education before teaching it a specific job.

---

## Q40. 50 LPA Question: Why is transfer learning useful?

### My Answer
Transfer learning saves time, compute, and data because we reuse knowledge from a pretrained model.

---

## Q41. 1 Crore Question: How would you fine-tune a pretrained CNN?

### My Answer
I would load a pretrained CNN, replace the final layer for my target classes, freeze early layers, train the final/deeper layers, evaluate performance, and then optionally unfreeze more layers if needed.

---

## Q42. 1.5 Crore Question: How would you choose between MLM and CLM models?

### My Answer
For understanding-heavy tasks like classification, NER, and search, I may choose BERT-style MLM models. For generation, chat, summarization, and agents, I would choose GPT-style CLM models.

---

## Q43. 2 Crore Question: How would you design an enterprise LLM customization strategy?

### My Answer
I would first identify use cases, risk level, data availability, privacy needs, and expected ROI. Then I would decide between API model, open-source model, RAG, fine-tuning, continued pretraining, agents, or hybrid architecture. I would include evaluation, monitoring, guardrails, and cost optimization.

---

# Part 10: Business Application Questions

## Q44. How can this concept help education?

### My Answer
Pretrained LLMs can be used with RAG and fine-tuning to create personalized AI tutors for school or college students.

---

## Q45. How can this concept help agriculture?

### My Answer
Pretrained CNNs can be fine-tuned for crop disease detection, and pretrained LLMs can support farmer advisory assistants.

---

## Q46. How can this concept help healthcare?

### My Answer
Pretrained models can help create hospital FAQ assistants or medical document summarizers, but they must be used with expert supervision and safety guardrails.

---

## Q47. How can this concept help finance or CA offices?

### My Answer
Pretrained LLMs with RAG can answer GST, tax, compliance, and finance document questions.

---

## Q48. How can this concept help manufacturing?

### My Answer
Pretrained vision models can be fine-tuned to detect defects in factory product images.

---

# Part 11: My Weak Areas After This Video

I need to study deeper:

- Transformer architecture
- Self-attention formula
- Tokenization in detail
- Cross-entropy loss
- Backpropagation
- ResNet architecture
- BERT architecture
- Hugging Face tokenizer and model classes
- Actual notebook implementation
- Fine-tuning code

---

# Part 12: My Score After Video 02

| Area | Score / 10 | Reason | Improvement Needed |
|---|---:|---|---|
| Model Training | 6/10 | I understand the pipeline | Need hands-on training example |
| Pretraining | 6/10 | I understand foundation models | Need practical notebook |
| Transfer Learning | 6/10 | I understand layer freezing | Need CNN fine-tuning code |
| CNN Pretraining | 6/10 | I understand feature hierarchy | Need ResNet demo |
| LLM Pretraining | 5/10 | I understand MLM/CLM basics | Need tokenizer/model code |
| Interview Readiness | 5/10 | Questions prepared | Need oral practice |
| GitHub Documentation | 7/10 | Notes created | Need notebook proof |
| Business Mapping | 6/10 | Use cases clear | Need MVP demos |

---

# Part 13: My Commitment

Before moving too fast, I will make sure I can explain these clearly:

- Training from scratch
- Pretraining
- Foundation model
- Transfer learning
- Fine-tuning
- CNN feature hierarchy
- MLM
- CLM
- Self-supervised learning
- ResNet/BERT pretrained inference