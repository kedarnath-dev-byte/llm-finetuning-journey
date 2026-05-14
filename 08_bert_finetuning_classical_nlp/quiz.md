# Quiz: BERT Fine-Tuning for Classical NLP

## Beginner Level

1. What is the full form of BERT?

2. Is BERT encoder-based or decoder-based?

3. Is BERT a generative model?

4. What is the difference between BERT and GPT?

5. What is IMDb dataset used for in this module?

---

## Tokenization Level

6. What does `BertTokenizer` do?

7. What is the difference between `BertTokenizer` and `tokenizer`?

8. What are `input_ids`?

9. What is `attention_mask`?

10. Why do we use padding?

11. Why do we use truncation?

12. What does `max_length=256` mean?

---

## Dataset Level

13. What is the difference between train data and test data?

14. Why did we use only 1000 training rows and 500 test rows?

15. What does `.shuffle(seed=42)` do?

16. What does `.select(range(1000))` do?

17. What does `.map()` do in Hugging Face Datasets?

18. Why do we rename `label` to `labels`?

19. What does PyTorch tensor format mean?

---

## Model Training Level

20. Why do we use `BertForSequenceClassification`?

21. What does `num_labels=2` mean?

22. Why do we use a small learning rate like `2e-5`?

23. What is the role of `TrainingArguments`?

24. What does `Trainer` connect together?

25. What does `trainer.train()` do?

26. What does `trainer.evaluate()` do?

---

## Output and Inference Level

27. Why should we save both model and tokenizer?

28. What does Hugging Face `pipeline()` do?

29. What does `LABEL_0` mean for IMDb?

30. What does `LABEL_1` mean for IMDb?

31. What did our Colab model predict for a positive review?

32. What did our Colab model predict for a negative review?

---

## Interview Level

33. Why are some BERT checkpoint weights shown as `UNEXPECTED` when loading `BertForSequenceClassification`?

34. Why are `classifier.weight` and `classifier.bias` shown as `MISSING`?

35. What is a task-specific head?

36. What is the difference between sequence classification, token classification, and question answering?

37. When would you use BERT instead of a large LLM?

38. When would BERT not be enough?

39. How can BERT be used in a RAG pipeline?

40. How would you explain this BERT fine-tuning project to a senior AI engineer?

---

## Business Level

41. How can schools use BERT fine-tuning?

42. How can hospitals use BERT fine-tuning?

43. How can CA offices or banks use BERT fine-tuning?

44. How can HR teams use BERT fine-tuning?

45. What privacy precautions are needed before fine-tuning on client data?

---

## Final Memory Test

Explain this complete flow in your own words:

Raw IMDb review
-> train/test sample
-> BERT tokenizer
-> input_ids and attention_mask
-> PyTorch tensors
-> BertForSequenceClassification
-> TrainingArguments
-> Trainer
-> training on Colab GPU
-> evaluation
-> save model/tokenizer
-> reload with pipeline
-> prediction
