# 🧠 이루다 만들기 — ML Research Learning Project

> Python 기초부터 시작해서,  
> 대화형 AI의 데이터·모델·평가·선호학습을 직접 실험하며 배우는 프로젝트.

---

## 프로젝트 한 줄 소개

**“캐릭터형 대화 모델의 재미와 일관성을 데이터와 학습 방법으로 얼마나 개선할 수 있는가?”**

이 저장소는 단순히 챗봇 하나를 만드는 프로젝트가 아닙니다.

`Python → NumPy → Pandas → PyTorch → NLP → Transformer → LLM → SFT → Evaluation → Preference Optimization`

순서로 성장하면서,  
스캐터랩이 공개한 이루다·제타의 ML Research 문제를 작은 규모로 직접 재현합니다.

---

# 0. 프로젝트 철학

이 프로젝트에서는 처음부터 LLM을 학습하지 않습니다.

먼저 데이터를 다룰 줄 알아야 합니다.

```text
Python
  ↓
NumPy
  ↓
Pandas
  ↓
PyTorch
  ↓
Machine Learning / Deep Learning
  ↓
NLP
  ↓
Transformer
  ↓
LLM
  ↓
Dialogue Model
  ↓
SFT
  ↓
Evaluation
  ↓
Preference Optimization
  ↓
Online Learning
```

이 프로젝트에서 가장 중요한 규칙은 하나입니다.

> **배우지 않은 기술을 멋있어 보인다는 이유로 먼저 사용하지 않는다.**

---

# 1. 지금 나는 어디에 있는가?

현재 학습 상태:

```text
Python
├─ list                       ✅
├─ dictionary                 ✅
├─ function                   ✅
├─ enumerate                  ✅
├─ zip                        ✅
├─ list comprehension         ✅
└─ NumPy
   ├─ ndarray                 ✅
   ├─ indexing                ✅
   └─ boolean indexing        ← NOW
```

현재 목표:

> **Python으로 데이터를 자유롭게 다룰 수 있는 사람이 된다.**

아직 목표는 LLM Fine-tuning이 아닙니다.

---

# 2. 왜 Python 기초부터 프로젝트인가?

지금 배우는 문법은 나중에 그대로 ML 코드가 됩니다.

## list

지금:

```python
scores = [80, 50, 90]
```

나중:

```python
responses = [
    "오늘 뭐했어?",
    "나 그냥 누워있었어 ㅋㅋ",
    "너는?"
]
```

---

## dictionary

지금:

```python
student = {
    "name": "Kim",
    "score": 90
}
```

나중:

```python
sample = {
    "user": "오늘 너무 힘들었어",
    "assistant": "헐 왜 ㅠ 무슨 일 있었는데?",
    "quality": 0.92
}
```

---

## enumerate

지금:

```python
names = ["Kim", "Lee", "Park"]

for index, name in enumerate(names):
    print(index, name)
```

나중:

```python
for index, sample in enumerate(dataset):
    print(index, sample["user"])
```

---

## zip

지금:

```python
names = ["Kim", "Lee"]
scores = [80, 90]

for name, score in zip(names, scores):
    print(name, score)
```

나중:

```python
prompts = ["안녕", "뭐해?"]
scores = [0.8, 0.4]

for prompt, score in zip(prompts, scores):
    print(prompt, score)
```

---

## list comprehension

지금:

```python
passed = [score for score in scores if score >= 60]
```

나중:

```python
good_responses = [
    sample
    for sample in dataset
    if sample["quality"] >= 0.8
]
```

---

## NumPy Boolean Indexing

지금:

```python
import numpy as np

scores = np.array([50, 70, 80, 90])

passed_scores = scores[scores >= 70]

print(passed_scores)
```

나중:

```python
quality_scores = np.array([
    0.91,
    0.32,
    0.84,
    0.71,
    0.95
])

high_quality = quality_scores[quality_scores >= 0.8]

print(high_quality)
```

이게 바로 ML 데이터 분석입니다.

---

# 3. 프로젝트 최종 목표

이 프로젝트를 완료했을 때 다음 질문에 답할 수 있어야 합니다.

## 데이터

- 대화 데이터를 어떤 형식으로 저장해야 하는가?
- 데이터 품질은 어떻게 측정할까?
- 중복 데이터는 왜 제거해야 할까?
- train / validation / test는 왜 나눌까?
- 좋은 데이터와 많은 데이터 중 무엇이 더 중요할까?

## 모델

- Language Model은 다음 토큰을 어떻게 예측할까?
- Transformer는 왜 대화 모델에 적합할까?
- Attention은 무엇을 계산할까?
- Tokenizer는 왜 필요할까?
- Fine-tuning과 Pre-training의 차이는 무엇일까?

## 대화

- “말이 되는 답변”과 “좋은 답변”은 무엇이 다를까?
- 캐릭터의 성격을 모델에 어떻게 학습시킬까?
- 긴 문맥을 모델이 어떻게 활용할까?
- 페르소나를 어떻게 유지할까?

## 평가

- 모델 A와 모델 B 중 무엇이 더 좋은지 어떻게 알까?
- 자동 평가를 어디까지 믿어도 될까?
- LLM-as-a-Judge는 어떻게 만들까?
- pairwise evaluation은 왜 유용할까?

## 선호 학습

- chosen / rejected 데이터는 무엇인가?
- DPO는 왜 등장했을까?
- RLHF와 DPO의 차이는 무엇인가?
- 사용자 행동을 학습 데이터로 사용할 수 있을까?

---

# 4. Repository Structure

처음부터 모든 폴더를 만들 필요는 없습니다.

배우는 단계에 맞춰 하나씩 추가합니다.

```text
luda/
│
├── README.md
│
├── 00_python/
│   ├── list.py
│   ├── dictionary.py
│   ├── comprehension.py
│   ├── enumerate.py
│   ├── zip.py
│   └── functions.py
│
├── 01_numpy/
│   ├── ndarray.py
│   ├── indexing.py
│   ├── boolean_indexing.py
│   ├── aggregation.py
│   ├── axis.py
│   └── exercises.py
│
├── 02_pandas/
│   ├── dataframe.py
│   ├── filtering.py
│   ├── missing_values.py
│   ├── groupby.py
│   └── conversation_analysis.ipynb
│
├── 03_visualization/
│   ├── matplotlib_basic.ipynb
│   └── conversation_stats.ipynb
│
├── 04_pytorch/
│   ├── tensor.py
│   ├── autograd.py
│   ├── linear.py
│   ├── loss.py
│   ├── optimizer.py
│   └── first_network.py
│
├── 05_ml_basics/
│   ├── train_validation_test.py
│   ├── regression.py
│   ├── classification.py
│   ├── overfitting.py
│   └── metrics.py
│
├── 06_nlp/
│   ├── tokenization.py
│   ├── vocabulary.py
│   ├── embedding.py
│   ├── text_classification.py
│   └── dialogue_dataset.py
│
├── 07_transformer/
│   ├── attention.py
│   ├── self_attention.py
│   ├── transformer_notes.md
│   └── tiny_transformer.py
│
├── 08_llm/
│   ├── huggingface_basics.py
│   ├── generation.py
│   ├── sampling.py
│   └── prompt_baseline.py
│
├── 09_luda_dataset/
│   ├── persona.md
│   ├── raw/
│   ├── processed/
│   ├── preference/
│   └── evaluation/
│
├── 10_sft/
│   ├── prepare_dataset.py
│   ├── train.py
│   ├── inference.py
│   └── result.md
│
├── 11_evaluation/
│   ├── evaluator.py
│   ├── pairwise.py
│   ├── llm_judge.py
│   └── leaderboard.md
│
├── 12_preference/
│   ├── build_pairs.py
│   ├── dpo.py
│   └── result.md
│
├── 13_advanced/
│   ├── reward_model/
│   ├── online_learning/
│   └── tokenizer/
│
├── experiments/
│   ├── exp001_baseline/
│   ├── exp002_sft/
│   └── exp003_dpo/
│
└── reports/
    ├── sft_vs_base.md
    └── dpo_vs_sft.md
```

---

# 5. PHASE 0 — Python for ML

## 목표

```text
데이터를 Python으로 자유롭게 다룰 수 있다.
```

---

## 반드시 알아야 할 것

### 변수 / 자료형

```text
int
float
str
bool
```

### 자료구조

```text
list
tuple
dict
set
```

### 흐름 제어

```text
if
for
while
```

### 함수

```text
parameter
return
scope
```

### 자주 쓰는 Python 기능

```text
enumerate
zip
range
sorted
lambda
list comprehension
dictionary comprehension
```

---

## 프로젝트 실습

### 00-1. 대화 리스트

```python
messages = [
    "안녕",
    "뭐해?",
    "나 심심해"
]
```

각 문장에 번호를 붙여 출력합니다.

### 00-2. 대화 Dictionary

```python
conversation = {
    "user": "오늘 뭐했어?",
    "assistant": "나 그냥 집에 있었어 ㅋㅋ"
}
```

### 00-3. 데이터 필터링

```python
scores = [0.4, 0.9, 0.7, 0.95]

good_scores = [
    score
    for score in scores
    if score >= 0.8
]
```

## 완료 조건

- [ ] list를 직접 설명할 수 있다.
- [ ] dict를 직접 설명할 수 있다.
- [ ] 함수에 인자를 넘기고 return 받을 수 있다.
- [ ] enumerate를 사용할 수 있다.
- [ ] zip을 사용할 수 있다.
- [ ] comprehension을 읽고 작성할 수 있다.
- [ ] 대화 데이터 10개를 dict/list 구조로 표현할 수 있다.

---

# 6. PHASE 1 — NumPy

## 목표

```text
숫자로 표현된 데이터를 빠르게 선택하고,
변형하고,
요약할 수 있다.
```

## 학습 순서

```text
ndarray
 ↓
shape / ndim
 ↓
indexing
 ↓
slicing
 ↓
boolean indexing
 ↓
aggregation
 ↓
axis
 ↓
reshape
 ↓
broadcasting
```

## 왜 ML에서 NumPy가 중요한가?

ML에서는 결국 대부분의 데이터가 숫자로 표현됩니다.

```text
문장
 ↓
Token
 ↓
Token ID
 ↓
Vector
 ↓
Matrix
 ↓
Model
```

NumPy를 배우면서 익히는 배열 감각이 나중에 PyTorch Tensor로 그대로 이어집니다.

## 1-1. Boolean Indexing

현재 배우고 있는 핵심 내용입니다.

```python
import numpy as np

scores = np.array([
    0.32,
    0.91,
    0.75,
    0.88,
    0.41
])

good = scores[scores >= 0.8]

print(good)
```

`scores >= 0.8`의 결과:

```python
[False, True, False, True, False]
```

이 Boolean Mask가 원본 배열에서 원하는 데이터만 골라냅니다.

### 프로젝트 연결

```python
import numpy as np

sensibleness = np.array([
    0.95,
    0.20,
    0.78,
    0.88,
    0.41
])

bad_samples = sensibleness[sensibleness < 0.5]

print(bad_samples)
```

연구 질문:

> 모델이 실패한 샘플만 골라서 분석해볼 수 있을까?

## 1-2. Aggregation

```python
scores.mean()
scores.sum()
scores.min()
scores.max()
scores.std()
```

ML에서는 다음처럼 사용합니다.

```text
평균 모델 점수
평균 loss
평균 token 수
분산/표준편차
```

## 1-3. Axis

```python
scores = np.array([
    [0.9, 0.7, 0.8],
    [0.5, 0.8, 0.6],
    [0.8, 0.9, 0.9]
])
```

각 행을 대화 샘플, 각 열을 평가 항목으로 볼 수 있습니다.

```text
Sensibleness
Specificity
Safety
```

## NumPy 미니 프로젝트

### Conversation Score Analyzer

입력:

```python
quality = np.array([
    0.92,
    0.53,
    0.81,
    0.21,
    0.95,
    0.72
])
```

구현:

```text
평균 점수
최고 점수
최저 점수
0.8 이상 개수
0.5 미만 데이터
점수 표준편차
평균보다 높은 데이터
```

## 완료 조건

- [ ] ndarray를 설명할 수 있다.
- [ ] indexing / slicing을 사용할 수 있다.
- [ ] boolean indexing을 이해한다.
- [ ] mean / sum / min / max를 사용할 수 있다.
- [ ] axis가 무엇인지 설명할 수 있다.
- [ ] reshape를 사용할 수 있다.
- [ ] broadcasting의 기본 개념을 이해한다.

---

# 7. PHASE 2 — Pandas

## 목표

```text
표 형태의 데이터를 분석할 수 있다.
```

대화 데이터:

```csv
user,assistant,score,safety
안녕,안녕ㅋㅋ,0.91,safe
오늘 힘들었어,왜ㅠ 무슨 일인데?,0.95,safe
```

```python
import pandas as pd

df = pd.read_csv("conversation.csv")
```

## 공부할 것

```text
Series
DataFrame
head
info
describe
loc
iloc
boolean filtering
missing value
sort_values
groupby
value_counts
apply
merge
```

## 미니 프로젝트 — Dialogue Dataset Analyzer

분석:

```text
총 대화 수
평균 답변 길이
카테고리별 데이터 수
평균 품질 점수
낮은 품질 데이터
중복 문장
결측치
```

---

# 8. PHASE 3 — Visualization

사용:

```text
matplotlib
```

그려볼 것:

```text
score histogram
category distribution
response length distribution
loss curve
model comparison
```

---

# 9. PHASE 4 — PyTorch

## 목표

```text
Tensor가 무엇인지 이해하고
작은 Neural Network를 직접 학습한다.
```

NumPy:

```python
import numpy as np
x = np.array([1, 2, 3])
```

PyTorch:

```python
import torch
x = torch.tensor([1, 2, 3])
```

PyTorch에서 추가되는 핵심:

```text
GPU
Autograd
Neural Network
Optimizer
```

## 공부 순서

```text
Tensor
 ↓
shape
 ↓
operation
 ↓
GPU
 ↓
autograd
 ↓
Linear
 ↓
Loss
 ↓
Optimizer
 ↓
training loop
```

반드시 설명할 수 있어야 할 것:

```text
epoch
batch
learning rate
loss
gradient
optimizer
forward
backward
```

---

# 10. PHASE 5 — Machine Learning Basics

핵심 개념:

```text
Train Set
Validation Set
Test Set
Overfitting
Classification
Metrics
```

작은 프로젝트:

```text
대화 문장을
daily / empathy / safety
등으로 분류하는 모델
```

---

# 11. PHASE 6 — NLP Basics

공부 순서:

```text
Tokenization
Vocabulary
Token ID
Embedding
Text Classification
Dialogue Dataset
```

문장:

```text
나는 오늘 학교에 갔다
```

Token → ID → Embedding으로 바뀌는 흐름을 직접 확인합니다.

---

# 12. PHASE 7 — Attention / Transformer

반드시 이해할 것:

```text
Query
Key
Value
Self Attention
Multi Head Attention
Feed Forward
Residual Connection
Layer Normalization
```

목표 질문:

> 왜 Transformer는 문맥 속 다른 토큰을 참고할 수 있을까?

---

# 13. PHASE 8 — Hugging Face / LLM Inference

공부할 것:

```text
AutoTokenizer
AutoModelForCausalLM
generate
max_new_tokens
temperature
top_k
top_p
do_sample
```

실험:

```text
temperature = 0.1
temperature = 0.7
temperature = 1.2
```

같은 프롬프트로 출력 차이를 비교합니다.

---

# 14. PHASE 9 — Character Baseline

이제 “이루다 만들기” 본편입니다.

아직 학습하지 않고 Prompt만 사용합니다.

## persona.md

```markdown
# Persona

이름:
나이:
성격:
말투:
취미:
좋아하는 것:
싫어하는 것:
사용자와의 관계:
자주 하는 표현:
금지된 행동:
```

최소 50개의 평가 프롬프트를 만듭니다.

```text
일상
고민
장난
프로필
관계
기억
안전
공격
```

---

# 15. 스캐터랩에서 가져올 첫 번째 연구 문제

스캐터랩은 Luda Gen 1에서 검색 기반 챗봇의 한계를 넘어 생성 기반 챗봇을 서비스에 적용했습니다.

우리도 작은 질문으로 재현합니다.

> **고정된 답변 후보에서 검색하는 방식과 생성형 모델은 어떤 상황에서 차이가 날까?**

실험:

```text
고정 답변 후보
vs
LLM 생성 답변
```

20개 질문에서 직접 비교합니다.

---

# 16. PHASE 10 — Dialogue Dataset

Dataset Schema:

```json
{
  "messages": [
    {
      "role": "user",
      "content": "뭐해?"
    },
    {
      "role": "assistant",
      "content": "나 누워있었음 ㅋㅋ 너는?"
    }
  ],
  "category": "daily",
  "quality": 1
}
```

데이터 종류:

```text
profile
daily
humor
empathy
relationship
memory
safety
abuse
```

category를 남기는 이유:

> 모델이 어떤 종류의 대화에서 실패하는지 분석하기 위해서.

---

# 17. 데이터 품질과 Deduplication

많은 데이터가 항상 좋은 것은 아닙니다.

중복 데이터:

```text
안녕
안녕
안녕
안녕
```

Pandas로 중복을 확인합니다.

```python
duplicates = df[df.duplicated()]
clean_df = df.drop_duplicates()
```

그리고 중복 제거 전후의 분포를 비교합니다.

---

# 18. PHASE 11 — SFT

```text
Supervised Fine-Tuning
```

좋은 대화 예시를 이용해 원하는 행동을 학습합니다.

추천 순서:

```text
Small Instruction Model
 ↓
Dialogue Dataset
 ↓
LoRA
 ↓
SFT
 ↓
Inference
 ↓
Baseline Comparison
```

처음부터 하지 않을 것:

```text
❌ LLM pre-training
❌ 거대한 모델 학습
❌ 거대한 GPU 서버 구축
```

---

# 19. PHASE 12 — Dialogue Evaluation

모델을 만들었으면 **좋아졌다는 것을 증명해야 합니다.**

평가 기준:

## Sensibleness

```text
문맥상 말이 되는가?
```

## Specificity

```text
현재 상황에 맞는 구체적인 답변인가?
```

## Safeness

```text
안전한 답변인가?
```

## Better

```text
두 답변 중 어느 것이 더 좋은가?
```

이 프로젝트에서는 추가로:

## Character Consistency

```text
캐릭터의 성격과 말투를 유지하는가?
```

## Engagement

```text
대화를 계속하고 싶게 만드는가?
```

---

# 20. Evaluation Dataset

학습 데이터와 분리합니다.

```text
evaluation/
├── daily.jsonl
├── persona.jsonl
├── empathy.jsonl
├── humor.jsonl
├── safety.jsonl
└── adversarial.jsonl
```

모델 비교 예시:

```markdown
| Model | Sensible | Specific | Safety | Character | Win Rate |
|---|---:|---:|---:|---:|---:|
| base | 0.82 | 0.52 | 0.91 | 0.44 | 36% |
| sft-v1 | 0.89 | 0.73 | 0.94 | 0.81 | 64% |
```

---

# 21. Pairwise Evaluation

A:

```text
많이 힘드셨겠네요.
```

B:

```text
헐 왜 ㅠ 오늘 뭔 일 있었는데?
```

질문:

```text
A와 B 중 어떤 답변이 캐릭터 관점에서 더 좋은가?
```

---

# 22. LLM-as-a-Judge

LLM에게 일부 평가를 맡겨봅니다.

```text
평가 기준:
1. 자연스러움
2. 구체성
3. 캐릭터 일관성
4. 대화 지속 가능성
```

그리고 반드시:

```text
Human Evaluation
vs
LLM Evaluation
```

일치도를 비교합니다.

---

# 23. PHASE 13 — Preference Dataset

구조:

```json
{
  "prompt": "오늘 학교에서 개빡쳤어",
  "chosen": "왜 ㅋㅋ 뭔 일 있었는데",
  "rejected": "학교에서 힘든 일이 있으셨군요."
}
```

둘 다 완전히 틀린 답변은 아닙니다.

하지만 캐릭터 관점에서 하나가 더 좋습니다.

---

# 24. 사용자 행동을 Preference로 보기

스캐터랩은 제타에서 실제 사용자 행동을 Preference Signal로 이용하는 연구를 공개했습니다.

우리 프로젝트에서는 작은 규모로 재현합니다.

```text
Original Response
→ rejected candidate

Regenerated Response
→ chosen candidate
```

하지만:

> **행동 데이터 = 정답**

이라고 단정하지 않습니다.

---

# 25. PHASE 14 — DPO

```text
Direct Preference Optimization
```

직관:

```text
좋은 답변 확률 ↑
덜 좋은 답변 확률 ↓
```

왜 DPO부터?

RLHF:

```text
Preference Data
 ↓
Reward Model
 ↓
RL
 ↓
Policy
```

DPO:

```text
Preference Data
 ↓
Model
```

첫 Preference Optimization 실험에 더 단순합니다.

비교:

```text
Base
vs
SFT
vs
DPO
```

---

# 26. PHASE 15 — Reward Model

입력:

```text
Prompt + Response
```

출력:

```text
Reward Score
```

NumPy가 다시 등장합니다.

```python
import numpy as np

rewards = np.array([
    0.92,
    0.31,
    0.71,
    0.88,
    0.22
])

good = rewards[rewards >= 0.8]
```

처음 배운 Boolean Indexing이 이 단계까지 연결됩니다.

---

# 27. Best-of-N

```text
Prompt
 ↓
LLM
 ├─ A
 ├─ B
 ├─ C
 └─ D
 ↓
Reward Model
 ↓
Best Response
```

실험:

```text
N = 1
N = 2
N = 4
N = 8
```

비교:

```text
Quality
Diversity
Latency
```

---

# 28. PHASE 16 — Online Learning

이 단계는 아주 나중입니다.

스캐터랩은 2026년 제타에서 DPO 이후 GRPO 기반 Online Learning을 적용한 경험을 공개했습니다.

Offline:

```text
Dataset
 ↓
Training
```

Online:

```text
Model
 ↓
Generate
 ↓
Reward
 ↓
Train
 ↓
New Model
```

공부할 것:

```text
Policy
Rollout
Reward
GRPO
Distribution Shift
Reward Hacking
```

---

# 29. Reward가 오르는데 답변이 이상해질 수도 있다

```text
Reward Score ↑
```

가 반드시

```text
Human Preference ↑
```

를 뜻하지 않습니다.

연결 개념:

```text
Reward Hacking
Overoptimization
Proxy Metric
Distribution Shift
```

---

# 30. PHASE 17 — Tokenizer Research

스캐터랩은 2026년 언어 특화 Tokenizer를 도입하며 토큰 효율과 모델 품질을 함께 다루는 과정을 공개했습니다.

실험:

```text
한국어 문장 1,000개
```

Tokenizer A/B에 대해 비교:

```text
tokens / sentence
tokens / conversation
context usage
generation speed
quality
```

연구 질문:

> Token 수가 적으면 무조건 좋은가?

아닙니다. 품질과 함께 봐야 합니다.

---

# 31. PHASE 18 — Continual Learning

새로운 데이터를 학습했는데 기존 능력을 잊을 수 있습니다.

```text
New Knowledge ↑
Old Knowledge ↓
```

연결 개념:

```text
Catastrophic Forgetting
Continual Learning
```

---

# 32. PHASE 19 — Multimodal

텍스트 모델이 안정된 이후에만 진행합니다.

```text
Image + Text → Conversation
```

공부:

```text
Vision Encoder
Multimodal Embedding
Vision-Language Model
```

---

# 33. 실험 관리

```text
experiments/
├── exp001_prompt_baseline/
├── exp002_temperature/
├── exp003_sft/
├── exp004_lora/
├── exp005_dpo/
└── exp006_best_of_n/
```

각 실험:

```markdown
# Experiment

## Question
## Hypothesis
## Setup
## Result
## Samples
## Failure Cases
## Conclusion
## Next
```

---

# 34. 실험 이름 규칙

금지:

```text
model1
model2
final
real-final
```

사용:

```text
base-prompt
persona-prompt-v2
sft-daily-profile
sft-safety-v1
dpo-character-preference
```

---

# 35. Research Question 중심으로 공부하기

잘못된 접근:

```text
DPO 해보고 싶다.
```

더 좋은 접근:

```text
SFT 모델이 캐릭터 말투를 유지하지 못한다.
↓
Preference Pair를 만들면 개선될까?
↓
DPO 실험
```

---

# 36. 실패 샘플 저장하기

```text
failures/
├── persona_failures.jsonl
├── safety_failures.jsonl
├── boring_responses.jsonl
└── hallucination.jsonl
```

실패 데이터가 다음 실험의 시작점입니다.

---

# 37. 스캐터랩 ML Research 흐름과 프로젝트 연결

## Luda Gen

```text
검색 기반 → 생성 기반
긴 문맥
시간 정보
화자 정보
페르소나
안전성
대화 품질
```

우리 프로젝트:

```text
PHASE 9 ~ 12
```

## Deduplication

```text
학습 데이터 중복 제거
```

우리 프로젝트:

```text
PHASE 10
```

## RLHF / DPO

```text
Human Preference
RLHF
DPO
```

우리 프로젝트:

```text
PHASE 13 ~ 15
```

## Zeta Preference Optimization

```text
실제 유저 행동
→ preference pair
→ DPO
```

우리 프로젝트:

```text
Regeneration simulation
→ chosen/rejected
→ DPO
```

## Zeta Online Learning

```text
Reward Model
Rollout
GRPO
Online Learning
```

우리 프로젝트:

```text
PHASE 16
```

## Tokenizer

```text
언어 특화 Tokenizer
Token Efficiency
Quality
Cost
```

우리 프로젝트:

```text
PHASE 17
```

---

# 38. 스캐터랩 추천 읽기 순서

## LEVEL 0 — 지금

### Luda Gen 1 — 생성 기반 챗봇
https://blog.scatterlab.co.kr/luda-gen-1

질문:

```text
검색 기반과 생성 기반의 차이는?
왜 생성형 모델이 필요했을까?
대화 문맥은 왜 중요할까?
```

### Luda Gen 1 — 생성 모델을 챗봇으로 빚어내기
https://blog.scatterlab.co.kr/luda-gen-2

질문:

```text
생성 모델에는 어떤 문제가 있었나?
좋은 답변은 어떻게 정의했나?
```

## LEVEL 1 — Pandas / PyTorch 이후

### Deduplication
https://blog.scatterlab.co.kr/deduplication/

## LEVEL 2 — Transformer / LLM 이후

### RLHF 외에 LLM이 피드백을 학습할 수 있는 방법은 무엇이 있을까?
https://blog.scatterlab.co.kr/alt-rlhf

## LEVEL 3 — SFT 이후

### 제타 Preference Optimization
https://blog.scatterlab.co.kr/%EC%9C%A0%EC%A0%80%EC%99%80-%ED%95%A8%EA%BB%98-%EB%A7%8C%EB%93%9C%EB%8A%94-llm-%EC%A0%9C%ED%83%80%EC%97%90-preference-optimization-%EB%8F%84%EC%9E%85%ED%95%98%EA%B8%B0-172134

## LEVEL 4 — DPO 이후

### 제타 Online Learning
https://blog.scatterlab.co.kr/%EC%9C%A0%EC%A0%80%EC%99%80-%ED%95%A8%EA%BB%98-%EB%A7%8C%EB%93%9C%EB%8A%94-llm-2%ED%8E%B8-%EC%A0%9C%ED%83%80%EC%97%90-online-learning-%EB%8F%84%EC%9E%85%ED%95%98%EA%B8%B0-196476

## LEVEL 5 — LLM 이해 이후

### 언어 특화 Tokenizer
https://blog.scatterlab.co.kr/tokenizer-281373

---

# 39. 지금 당장 하지 않을 것

```text
❌ Kubernetes
❌ Spring Boot
❌ Redis
❌ PostgreSQL
❌ MLOps 플랫폼 구축
❌ vLLM 튜닝
❌ RLHF 구현
❌ GRPO 구현
❌ LLM Pre-training
```

이 기술들이 나쁘다는 뜻이 아닙니다.

> **지금 내 연구 질문을 푸는 데 필요하지 않기 때문입니다.**

---

# 40. 지금 당장 할 것

현재:

```text
NumPy Boolean Indexing
```

다음:

```text
[ ] Boolean Mask
[ ] Boolean Indexing
[ ] mean / min / max
[ ] std
[ ] axis
[ ] reshape
[ ] broadcasting
```

---

# 41. NumPy 완료 미니 프로젝트

파일:

```text
01_numpy/conversation_scores.py
```

```python
import numpy as np

scores = np.array([
    0.91,
    0.32,
    0.87,
    0.76,
    0.95,
    0.42,
    0.83,
    0.68
])
```

구현:

```text
1. 전체 평균
2. 최고 점수
3. 최저 점수
4. 0.8 이상 점수
5. 0.5 미만 점수
6. 0.8 이상 데이터 개수
7. 평균보다 높은 점수
```

---

# 42. NumPy 보너스 프로젝트

```python
scores = np.array([
    [0.9, 0.8, 1.0],
    [0.4, 0.7, 0.9],
    [0.8, 0.9, 0.8],
    [0.3, 0.2, 0.9]
])
```

열:

```text
Sensibleness
Specificity
Safety
```

구현:

```text
각 평가 항목 평균
각 대화 평균
전체 평균
Specificity 0.5 미만 샘플
Safety 0.8 이상 샘플
```

---

# 43. Pandas로 넘어가는 기준

```text
scores[scores >= 0.8]
scores.mean()
scores.std()
scores.shape
scores.reshape(...)
scores.mean(axis=0)
```

위 코드를 외우는 것이 아니라 결과를 설명할 수 있어야 합니다.

---

# 44. PyTorch로 넘어가는 기준

```text
CSV 읽기
조건 필터링
결측치 처리
groupby
평균 계산
데이터 분포 확인
간단한 그래프
```

---

# 45. Transformer로 넘어가는 기준

```text
Tensor
Matrix Multiplication
Linear Layer
Loss
Gradient
Optimizer
Training Loop
```

---

# 46. SFT로 넘어가는 기준

```text
Token
Tokenizer
Embedding
Attention
Transformer
Causal Language Model
Prompt
Inference
Train / Validation
Loss
```

---

# 47. DPO로 넘어가는 기준

```text
[ ] Base Model 평가
[ ] SFT
[ ] SFT Model 평가
[ ] Pairwise Evaluation
[ ] chosen/rejected Dataset 제작
```

그 전에는 DPO를 하지 않습니다.

---

# 48. 매일 공부 방식

```text
개념 공부
↓
짧은 예제
↓
프로젝트형 문제
↓
코드 설명
↓
Git Commit
```

---

# 49. Commit 예시

```text
study: practice numpy boolean indexing
study: learn numpy axis and aggregation
feat: add conversation score analyzer
experiment: compare temperature settings
experiment: compare base and sft model
```

---

# 50. AI를 공부 도구로 사용하는 방법

좋은 질문:

```text
이 코드가 왜 이렇게 동작하는지 설명해줘.
답을 말하지 말고 힌트만 줘.
내 풀이를 리뷰해줘.
이 개념을 활용하는 ML 문제를 하나 내줘.
내가 이해했는지 확인할 문제를 내줘.
```

프로젝트의 목표는 결과물이 아니라  
**내가 직접 설명할 수 있는 능력**입니다.

---

# 51. Learning Log

```markdown
# YYYY-MM-DD

## 오늘 공부
## 직접 작성한 코드
## 이해한 것
## 아직 헷갈리는 것
## 프로젝트와 연결하면?
## 내일
```

---

# 52. 첫 번째 연구 노트

`docs/research_questions.md`

```markdown
# Research Questions

## Q1
캐릭터 정보를 Prompt에 넣는 것만으로
얼마나 일관된 Persona를 만들 수 있을까?

## Q2
SFT 이후 Persona Consistency는 얼마나 개선될까?

## Q3
SFT 모델은 왜 뻔한 답변을 만들까?

## Q4
Pairwise Preference를 학습하면
더 재미있는 답변을 만들 수 있을까?

## Q5
LLM-as-a-Judge 결과는 사람 평가와 얼마나 일치할까?

## Q6
Best-of-N은 품질을 얼마나 올리고
추론 비용을 얼마나 증가시킬까?

## Q7
한국어 Tokenizer에 따라
같은 대화의 Token 수가 얼마나 달라질까?
```

---

# 53. 프로젝트의 최종 모습

```text
Raw Dialogue
     ↓
Data Analysis
     ↓
Cleaning
     ↓
Baseline LLM
     ↓
SFT
     ↓
Offline Evaluation
     ↓
Human / LLM Pairwise Evaluation
     ↓
Preference Dataset
     ↓
DPO
     ↓
Evaluation
     ↓
Reward Model
     ↓
Best-of-N
     ↓
Online Learning Study
```

---

# 54. 최종 결과물

최종 저장소에는 다음이 남습니다.

```text
Python / NumPy 학습 기록
Pandas 데이터 분석
PyTorch 실습
Transformer 학습
Dialogue Dataset
SFT
DPO
Evaluation
Experiment Logs
Failure Analysis
Final Report
```

Final Report:

```markdown
# Character Dialogue Model Research

## 1. Problem
## 2. Dataset
## 3. Baseline
## 4. SFT
## 5. Evaluation
## 6. Preference Optimization
## 7. Results
## 8. Failure Analysis
## 9. Limitations
## 10. Future Work
```

---

# 55. 이 프로젝트의 진짜 성공 기준

❌

> “DPO 써봤어요.”

✅

> “SFT 모델의 캐릭터 응답이 문맥상 자연스럽지만 지나치게 일반적인 문제가 있었습니다. Pairwise Preference 데이터를 구축해서 DPO를 적용했고, 동일한 평가셋에서 SFT 모델 대비 pairwise win-rate가 개선되었습니다. 다만 Safety에서는 큰 차이가 없었고 특정 질문에서는 답변 길이가 과도하게 증가하는 문제가 있었습니다.”

이게 이 프로젝트에서 목표로 하는 **ML Research의 사고 방식**입니다.

---

# 56. 프로젝트 Motto

> **코드를 많이 쓰는 것이 목표가 아니다.  
> 질문을 만들고, 데이터를 보고, 실험하고, 결과를 설명한다.**

> **Python 한 줄부터 LLM 실험까지 전부 하나의 프로젝트다.**

---

# 57. 오늘의 위치

```text
[Python]      ██████████
[NumPy]       ████░░░░░░  ← HERE
[Pandas]      ░░░░░░░░░░
[PyTorch]     ░░░░░░░░░░
[NLP]         ░░░░░░░░░░
[Transformer] ░░░░░░░░░░
[LLM]         ░░░░░░░░░░
[SFT]         ░░░░░░░░░░
[DPO]         ░░░░░░░░░░
```

지금 해야 할 일:

> **NumPy를 제대로 배우기.**

LLM은 도망가지 않습니다.

---

# References — Scatter Lab Research Blog

이 프로젝트의 연구 방향은 스캐터랩이 공개한 ML Research / ML Engineering 글의 문제의식을 참고했습니다.

- Scatter Lab Blog  
  https://blog.scatterlab.co.kr/

- ML Research  
  https://blog.scatterlab.co.kr/category/ml-research

- ML Engineering  
  https://blog.scatterlab.co.kr/category/ml-engineering

- Luda Gen 1 — 생성 기반 챗봇  
  https://blog.scatterlab.co.kr/luda-gen-1

- Luda Gen 1 — 생성 모델을 챗봇으로 빚어내기  
  https://blog.scatterlab.co.kr/luda-gen-2/

- Deduplication — 학습 데이터에서 중복 제거하기  
  https://blog.scatterlab.co.kr/deduplication/

- RLHF 외에 LLM이 피드백을 학습할 수 있는 방법은 무엇이 있을까?  
  https://blog.scatterlab.co.kr/alt-rlhf

- 유저와 함께 만드는 LLM — 제타에 Preference Optimization 도입하기  
  https://blog.scatterlab.co.kr/%EC%9C%A0%EC%A0%80%EC%99%80-%ED%95%A8%EA%BB%98-%EB%A7%8C%EB%93%9C%EB%8A%94-llm-%EC%A0%9C%ED%83%80%EC%97%90-preference-optimization-%EB%8F%84%EC%9E%85%ED%95%98%EA%B8%B0-172134

- 유저와 함께 만드는 LLM 2편 — 제타에 Online Learning 도입하기  
  https://blog.scatterlab.co.kr/%EC%9C%A0%EC%A0%80%EC%99%80-%ED%95%A8%EA%BB%98-%EB%A7%8C%EB%93%9C%EB%8A%94-llm-2%ED%8E%B8-%EC%A0%9C%ED%83%80%EC%97%90-online-learning-%EB%8F%84%EC%9E%85%ED%95%98%EA%B8%B0-196476

- 비용과 성능을 한번에 — 언어 특화 토크나이저 도입기  
  https://blog.scatterlab.co.kr/tokenizer-281373

---

## NEXT

```text
NumPy Boolean Indexing
→ Aggregation
→ Axis
→ Reshape
→ Broadcasting
→ Pandas
```

**오늘의 한 줄**

> `scores[scores >= 0.8]`를 완전히 이해하는 것부터 시작한다.
