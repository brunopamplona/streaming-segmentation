import pandas as pd
import numpy as np

n = 10000

df = pd.DataFrame({
    "user_id": [f"U{i:05d}" for i in range(n)],
    "plan_type": np.random.choice(["Family","Hollywood"], n),
    "subscription_days": np.random.randint(1, 500, n),
    "cohort_month": np.random.choice(pd.date_range("2023-01-01","2025-12-01", freq="MS").strftime("%Y-%m"), n),
    "acquisition_channel": np.random.choice(["paid","organic"], n, p=[0.6,0.4]),
})

# CAC
df["cac"] = np.where(df["acquisition_channel"]=="paid",
                     np.random.randint(70,150,n),
                     0)

# lifecycle
df["is_new_user"] = (df["subscription_days"] < 30).astype(int)

# base engagement
base_engagement = np.random.uniform(0.2, 1.0, n)

# L30
df["active_days_l30"] = (base_engagement * np.random.randint(8, 25, n)).astype(int)
df["watch_sessions_l30"] = (base_engagement * np.random.randint(10, 35, n)).astype(int)
df["total_watch_time_l30"] = (df["watch_sessions_l30"] * np.random.randint(2, 5, n))

# growth factors
growth_60 = np.random.uniform(1.2, 1.6, n)
growth_90 = np.random.uniform(1.4, 2.2, n)

# L60
df["active_days_l60"] = (df["active_days_l30"] * growth_60).astype(int)
df["watch_sessions_l60"] = (df["watch_sessions_l30"] * growth_60).astype(int)
df["total_watch_time_l60"] = (df["total_watch_time_l30"] * growth_60).astype(int)

# L90
df["active_days_l90"] = (df["active_days_l30"] * growth_90).astype(int)
df["watch_sessions_l90"] = (df["watch_sessions_l30"] * growth_90).astype(int)
df["total_watch_time_l90"] = (df["total_watch_time_l30"] * growth_90).astype(int)

# behavior extras
df["completion_rate_l30"] = np.round(np.random.uniform(0.2,0.95,n),2)
df["binge_sessions_l30"] = np.random.randint(0,15,n)
df["content_diversity_score"] = np.round(np.random.uniform(0.2,0.9,n),2)
df["avg_session_duration"] = np.random.randint(20,70,n)

# recency
df["last_watch_days_ago"] = np.random.randint(0,45,n)

# trial / paid
df["trial_user"] = df["is_new_user"]
df["is_paid"] = (df["subscription_days"] > 30).astype(int)

# churn logic (com decay implícito)
df["churn_prob"] = (
    (df["last_watch_days_ago"]/45)*0.4 +
    (1 - df["completion_rate_l30"])*0.3 +
    (1 - df["active_days_l30"]/25)*0.2 +
    (df["is_new_user"]*0.1)
)

df["churned_90d"] = (df["churn_prob"] > 0.6).astype(int)

df.drop(columns=["churn_prob"], inplace=True)

df.to_csv("streaming_dataset_L30_L60_L90.csv", index=False)

from google.colab import files
files.download("streaming_dataset_L30_L60_L90.csv")