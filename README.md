# 🧩 Streaming Segmentation — RFM & Behavioral Clustering for a Brazilian Streaming Platform

> **Subscriber segmentation pipeline** combining RFM scoring and behavioral engagement clustering to identify actionable audience segments — enabling personalized retention, upsell, and reactivation strategies across a tiered subscription base.

---

## Overview

This project builds a multi-dimensional segmentation framework for a subscription streaming business. Rather than treating all subscribers as a single audience, it identifies structurally distinct behavioral profiles — from highly engaged power users to at-risk dormant subscribers — and maps each segment to concrete growth interventions.

**Why segmentation matters beyond churn models:** A churn model tells you *who is likely to leave*. Segmentation tells you *who they are, how they behave, and what they respond to*. The two are complementary: churn scores determine urgency; segments determine the intervention strategy. A "dormant sports fan" and a "price-sensitive casual viewer" may have identical churn probabilities but require completely different retention approaches.

---

## Key Features

- **RFM Scoring** — Recency, Frequency, and Monetary scoring with quintile-based segmentation and composite RFM tiers
- **Behavioral Clustering** — K-Means and hierarchical clustering on engagement features (content diversity, binge behavior, device usage, session depth)
- **Segment Profiling** — Rich descriptive profiles per cluster including content preferences, plan distribution, churn risk, and LTV estimates
- **Segment Stability Analysis** — Cohort tracking to measure how subscribers migrate between segments over time
- **Growth Action Mapping** — Each segment paired with recommended acquisition, retention, upsell, or reactivation playbook

---

## Model Architecture

```
Subscriber Behavioral Data (30/60/90-day rolling windows)
                    │
                    ▼
          RFM Feature Construction
     (Recency, Frequency, Monetary proxy)
                    │
                    ▼
         Quintile Scoring + RFM Tiers
     (Champions / Loyal / At-Risk / Dormant / ...)
                    │
          ┌─────────┴──────────┐
          ▼                    ▼
   Behavioral Features    RFM Composite Score
   (engagement depth,     (5x5x5 tier grid)
    content diversity,
    device, binge flag)
          │                    │
          └─────────┬──────────┘
                    ▼
         K-Means Clustering
    (optimal k via elbow + silhouette)
                    │
                    ▼
         Segment Profiles + LTV Estimates
                    │
                    ▼
         Growth Action Mapping per Segment
```

---

## Dataset

The dataset is **fully synthetic**, generated to reflect realistic behavioral patterns of a Brazilian SVOD platform across tiered subscription plans:

| Plan | Price | Subscriber Share | Behavioral Profile |
|---|---|---|---|
| Família | R$ 80/mo | 28% | High frequency, multi-device, co-viewing sessions |
| Premiere (Football) | R$ 60/mo | 22% | Highly seasonal, event-driven spikes, low inter-season engagement |
| Telecine (Movies) | R$ 38/mo | 31% | Weekend-concentrated, catalog-driven, moderate churn |
| HBO Max bundle | R$ 35/mo | 19% | Short tenure, content breadth seekers, price-sensitive |

Behavioral signals included: **session frequency, active days (L7/L14/L30/L60/L90), content categories consumed, binge sessions, avg watch time, device count, login gap, plan tenure, support contacts, payment history**

---

## RFM Framework

### Dimension Definitions for Streaming

Standard RFM was adapted for the subscription streaming context:

| Dimension | Standard Definition | Streaming Adaptation |
|---|---|---|
| **Recency** | Days since last purchase | Days since last streaming session |
| **Frequency** | Number of transactions | Active days in the last 30 days |
| **Monetary** | Total spend | Plan value × tenure (LTV proxy) |

> **Design note:** In subscription businesses, "Monetary" does not vary transaction-by-transaction — all subscribers on the same plan pay the same amount. Monetary is therefore used as an LTV proxy (monthly plan value × months active), which captures the accumulated revenue relationship rather than a single transaction signal.

### RFM Tier Grid

| Tier | RFM Profile | Description |
|---|---|---|
| **Champions** | High R, High F, High M | Highly engaged, long-tenure, high-value subscribers |
| **Loyal** | High F, High M | Consistent engagement, moderate recency |
| **Potential Loyalists** | High R, Moderate F | Recently active, building engagement habit |
| **At-Risk** | Low R, Historically High F | Previously engaged, now disengaging |
| **Can't Lose Them** | Low R, High M | High-value subscribers showing early churn signals |
| **Dormant** | Low R, Low F, Low M | Minimal engagement, high churn probability |
| **New Subscribers** | High R, Low F | Recently activated, engagement pattern not yet established |

---

## Behavioral Clustering

Beyond RFM, a separate clustering layer captures behavioral archetypes that RFM alone cannot distinguish:

| Cluster | Label | Profile |
|---|---|---|
| 0 | **Binge Watchers** | High session depth, low frequency, concentrated weekend activity |
| 1 | **Daily Streamers** | High active days, diverse content, multi-device, high tenure |
| 2 | **Sports Fans** | Seasonal spikes, low inter-season engagement, Premiere plan concentration |
| 3 | **Casual Viewers** | Low frequency, narrow content breadth, price-sensitive plans |
| 4 | **Lapsed Explorers** | Previously high diversity, now dormant — catalog exhaustion pattern |
| 5 | **New & Undecided** | Short tenure, erratic sessions, high uncertainty on retention |

---

## Segment Profiles Snapshot

| Segment | Size | Avg LTV | Churn Risk | Avg Active Days L30 | Top Plan |
|---|---|---|---|---|---|
| Champions | 12% | R$ 1,240 | 3% | 22 | Família |
| Loyal | 18% | R$ 890 | 6% | 17 | Família / Telecine |
| Potential Loyalists | 14% | R$ 310 | 8% | 14 | HBO / Telecine |
| At-Risk | 16% | R$ 720 | 24% | 6 | Premiere |
| Can't Lose Them | 7% | R$ 1,050 | 19% | 5 | Família |
| Dormant | 11% | R$ 180 | 61% | 1 | HBO |
| New Subscribers | 22% | R$ 80 | 14% | 11 | All plans |

---

## Growth Action Mapping

| Segment | Priority | Recommended Action |
|---|---|---|
| **Champions** | Retention + Upsell | Plan upgrade offers, loyalty perks, referral program activation |
| **Loyal** | Retention | Content recommendations, early access to new releases |
| **Potential Loyalists** | Engagement | Onboarding nudges, feature discovery, habit-forming push notifications |
| **At-Risk** | Retention | Personalized win-back content, targeted discount offer, churn model escalation |
| **Can't Lose Them** | Urgent Retention | High-value intervention: personal outreach, premium offer, dedicated support |
| **Dormant** | Reactivation | Re-engagement campaign, content refresh messaging, price incentive |
| **New Subscribers** | Activation | Onboarding flow optimization, early engagement checkpoints, content onboarding |

---

## Project Structure

```
streaming-segmentation/
│
├── data/
│   ├── generate_subscriber_data.py      # Synthetic subscriber behavioral generator
│   └── streaming_subscribers.csv        # Generated subscriber dataset
│
├── notebooks/
│   ├── 01_eda_subscriber_base.ipynb     # Cohort analysis, plan distribution, tenure curves
│   ├── 02_rfm_scoring.ipynb             # RFM construction, quintile scoring, tier assignment
│   ├── 03_behavioral_clustering.ipynb   # Feature prep, K-Means, elbow/silhouette, profiling
│   ├── 04_segment_profiles.ipynb        # Descriptive profiles, LTV, churn risk per segment
│   └── 05_growth_action_mapping.ipynb   # Intervention playbook + segment migration analysis
│
├── src/
│   ├── rfm.py                           # RFM scoring pipeline
│   ├── clustering.py                    # K-Means + hierarchical clustering wrapper
│   └── profiling.py                     # Segment descriptive statistics and LTV estimation
│
├── outputs/
│   ├── rfm_tier_distribution.png
│   ├── cluster_scatter_pca.png
│   ├── segment_profiles_heatmap.png
│   └── segment_migration_sankey.png
│
├── requirements.txt
└── README.md
```

---

## Tech Stack

| Layer | Tools |
|---|---|
| Feature Engineering | Python, pandas, NumPy |
| RFM Scoring | pandas (quintile-based scoring) |
| Clustering | scikit-learn (K-Means, AgglomerativeClustering) |
| Dimensionality Reduction | PCA (visualization), t-SNE (cluster validation) |
| Visualization | matplotlib, seaborn, Plotly, plotly Sankey (migration) |

---

## How to Run

```bash
# 1. Clone the repository
git clone https://github.com/your-username/streaming-segmentation.git
cd streaming-segmentation

# 2. Install dependencies
pip install -r requirements.txt

# 3. Generate synthetic subscriber dataset
python data/generate_subscriber_data.py

# 4. Run notebooks in order
jupyter notebook notebooks/
```

---

## Methodology Notes

**RFM Monetary proxy for subscriptions**
In transactional businesses, Monetary is straightforward. In subscriptions, all subscribers on the same plan pay identical amounts per billing cycle. To preserve the Monetary dimension's signal, this project uses `plan_monthly_value × months_active` as an LTV proxy — which captures the *accumulated revenue relationship* rather than a single transaction value and correlates meaningfully with retention probability.

**Optimal cluster selection**
K was selected using a combined criterion: elbow method on within-cluster sum of squares (WCSS) and silhouette score maximization. The final k=6 was validated against business interpretability — each cluster needed to map to a distinct, recognizable subscriber archetype with actionable differences.

**Segment stability**
Subscribers are re-scored monthly. The Sankey diagram in outputs tracks migration between segments across quarters, which is operationally important: a large flow from "Potential Loyalists" to "At-Risk" signals a breakdown in the onboarding or early engagement funnel that a static snapshot would miss.

**Identified Limitations**
- RFM does not capture content preference — two subscribers with identical RFM scores may have completely different content needs and respond to different retention interventions
- K-Means assumes spherical clusters and is sensitive to outliers; high-LTV outliers in the Champions segment may distort centroids
- Segment labels are assigned post-hoc based on cluster centroids — interpretability is a design choice, not a model output

---

## Roadmap

- [ ] Content-based segmentation layer (genre affinity, franchise loyalty, format preference)
- [ ] Propensity score integration — combining segment membership with churn model output for intervention prioritization matrix
- [ ] Real-time segment scoring pipeline (feature store + daily batch re-scoring)
- [ ] Segment-level A/B test framework for intervention validation

---

## Portfolio Context

This repository is the **fourth component** of an integrated Marketing Science portfolio for a streaming subscription business:

| Repository | Focus |
|---|---|
| [`streaming-mmm`](../streaming-mmm) | Media Mix Modeling, saturation curves, budget optimization |
| [`streaming-churn-forecasting`](../streaming-churn-forecasting) | Behavioral churn prediction, intervention threshold optimization |
| [`streaming-mta`](../streaming-mta) | Multi-touch attribution, model comparison, MTA vs. MMM framework |
| **`streaming-segmentation`** *(this repo)* | RFM + behavioral clustering, segment profiling, growth action mapping |

All repositories share the same synthetic platform dataset and subscription plan structure, enabling cross-model analysis and a unified analytical narrative across the full subscriber lifecycle.

---

## Author

**Bruno** — Technical Architect & Decision Science Lead  
Focused on Growth Analytics, subscriber segmentation, and lifecycle marketing for subscription businesses.

[LinkedIn](https://linkedin.com/in/your-profile) • [GitHub](https://github.com/your-username)

---

*Synthetic data. All figures are illustrative and do not represent any real company's performance.*

