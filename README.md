# 🎬 Streaming Segmentation — RFM, Behavioral Clustering & Value-Based Decisioning

Subscriber segmentation pipeline combining RFM scoring, behavioral clustering, and value-based prioritization to drive retention, conversion, and LTV optimization in a Brazilian streaming subscription platform.

---

## 📌 Context

This project simulates a Marketing Science system applied to a subscription streaming platform (modeled after a ficticious video+ streaming services in Brazil), with a monthly plan of **R$90** and 120+ live channels.

The core challenge is not just identifying who users are — but determining:

→ **where to allocate budget and interventions to maximize LTV/CAC**

---

## 🎯 Business Problem

How can we:

* Increase trial → paid conversion
* Improve early-stage activation
* Reduce churn in the first 90 days
* Maximize subscriber lifetime value (LTV)

---

## 🧠 Core Insight

Churn models answer:

→ *Who is likely to leave?*

Segmentation answers:

→ *What should we do about it?*

This project integrates both perspectives into a unified decision framework:

> **Expected Value = P(conversion / retention) × LTV**

---

## 🏗️ Model Architecture

Subscriber Behavioral Data (30/60/90-day windows)

                 │
                 ▼
                 
Feature Engineering Layer
(Recency, Engagement, Consumption Patterns)

                 │
                 ▼
                 
RFM Value Modeling (LTV Proxy)

                 │
       ┌─────────┴──────────┐
       ▼                    ▼
       
Behavioral Features      Value Score
(engagement depth,       (RFM-based)
binge behavior,
content diversity)

       │                    │
       └─────────┬──────────┘
                 ▼

Intent Score (Engagement Probability)

                 │
                 ▼

Expected Value Score (Intent × Value)

                 │
       ┌─────────┴──────────┐
       ▼                    ▼

  Behavioral Clustering   RFM Tiering
  
       │                    │
       └─────────┬──────────┘
                 ▼
  
  Segment Profiles + LTV Estimates
  
                 │
                 ▼

Growth Action Mapping per Segment

---

## 🔢 Scoring System

### 🎯 Intent Score (Short-term engagement likelihood)

Proxy for near-term retention or conversion:

* Active days (L7)
* Watch sessions (L30)
* Completion rate

---

### 💰 Value Score (LTV proxy)

* Subscription tenure
* Total watch time
* Binge behavior

---

### ⚠️ Churn Risk

* Days since last watch
* Engagement decay signals

---

### 🧠 Expected Value Score

> **Expected Value = Intent Score × Value Score**

This score is used for **prioritization**, not just classification.

---

## 🧩 Segmentation Framework

Segmentation combines:

* RFM tiers (economic value)
* Behavioral clusters (usage patterns)
* Expected value scoring (decision layer)

---

### Segment Overview

| Segment             | Size | Avg LTV  | Churn Risk | Behavior                     |
| ------------------- | ---- | -------- | ---------- | ---------------------------- |
| Champions           | 12%  | R$ 1,240 | 3%         | High engagement, long tenure |
| Loyal               | 18%  | R$ 890   | 6%         | Consistent usage             |
| Potential Loyalists | 14%  | R$ 310   | 8%         | Early habit formation        |
| At-Risk             | 16%  | R$ 720   | 24%        | Engagement drop-off          |
| Can't Lose Them     | 7%   | R$ 1,050 | 19%        | High value, declining usage  |
| Dormant             | 11%  | R$ 180   | 61%        | Minimal engagement           |
| New Subscribers     | 22%  | R$ 90    | 14%        | Early lifecycle              |

---

## 🎯 Decision Layer (Key Differentiator)

Unlike traditional segmentation:

This system answers:

→ **Where should we invest the next dollar?**

Example:

| Segment                  | Action                        |
| ------------------------ | ----------------------------- |
| High intent + high value | Aggressive retention / upsell |
| High value + high churn  | Immediate intervention        |
| Low value + low intent   | Budget minimization           |

---

## 🎨 Personalization Strategy

Examples:

* "Continue watching [Series]" → Engagement recovery
* "New episodes available" → Habit reinforcement
* "Top picks for you" → Activation
* "We miss you — 15% off" → Winback

---

## 📣 Activation Channels

### Paid Media

* Meta Ads → Retargeting, lookalike expansion
* Google Ads → RLSA, Customer Match

### CRM (Primary Impact Driver)

* Push notifications
* Email campaigns
* In-app personalization

---

## 🔬 Experiment Design

A/B testing framework:

* Control → Generic messaging
* Treatment → Segment-based personalization

---

## 📊 Simulated Results

| Metric                  | Baseline | Treatment | Uplift |
| ----------------------- | -------- | --------- | ------ |
| Trial → Paid Conversion | 18%      | 23%       | +27%   |
| D30 Retention           | 52%      | 61%       | +17%   |
| Monthly Churn           | 8.5%     | 6.8%      | -20%   |
| LTV (R$)                | 540      | 690       | +28%   |
| ROAS                    | 2.8      | 3.6       | +29%   |

---

## 🧠 Key Insights

* Behavioral signals outperform demographic targeting
* Retention has higher impact than acquisition
* Timing (when to act) matters more than messaging alone
* Segment + score > segment alone

---

## ⚠️ Limitations

* RFM does not capture content preference
* K-Means assumes cluster homogeneity
* Synthetic data limits real-world variance
* Rule-based scoring approximates true probability

---

## 🚀 Roadmap

* ML-based propensity modeling (XGBoost)
* Survival analysis for churn prediction
* Real-time scoring pipeline (feature store)
* Budget allocation optimization based on expected value
* Incrementality testing (geo experiments)

---

## 📁 Project Structure

streaming-segmentation/
│
├── data/
│   ├── generate_streaming_data.py
│   └── streaming_users.csv
│
├── notebooks/
│   ├── 01_eda.ipynb
│   ├── 02_rfm_scoring.ipynb
│   ├── 03_behavioral_clustering.ipynb
│   ├── 04_scoring_model.ipynb
│   └── 05_experiment_simulation.ipynb
│
├── src/
│   ├── rfm.py
│   ├── scoring.py
│   ├── clustering.py
│   └── simulation.py
│
├── outputs/
│   ├── segment_distribution.png
│   ├── cluster_pca.png
│   ├── ltv_distribution.png
│   └── uplift_simulation.png
│
└── README.md

---

## 👤 Author

Bruno — Marketing Science & Growth Strategy
Focus: segmentation, LTV modeling, and decision systems for subscription businesses

---

## 📌 Final Takeaway

Segmentation is not about grouping users.

It is about:

→ **allocating capital based on probability × value × timing**
