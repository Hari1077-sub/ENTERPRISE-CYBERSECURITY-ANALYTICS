import numpy as np
import pandas as pd
from statsmodels.stats.proportion import proportions_ztest

# Phase 1: Synthetic Experimentation Engine
print("Initializing Synthetic Experimentation Engine...")
np.random.seed(42)
n_usrs = 5000
# 1. Generate Base User Profiles
usr_ids = [f"EMP-{str(i).zfill(4)}" for i in range(1, n_usrs + 1)]
depts = np.random.choice(
    ['Engineering', 'Sales', 'Finance', 'HR', 'Operations'], 
    n_usrs, 
    p=[0.30, 0.25, 0.15, 0.10, 0.20]
)

# 2. 50/50 Split Assignment
# Control (Version A): Passive 30-day email reminders
# Variant (Version B): Active 3-day soft-block grace period
grps = np.random.choice(['Control', 'Variant'], n_usrs, p=[0.5, 0.5])
df = pd.DataFrame({
    'employee_id': usr_ids,
    'department': depts,
    'test_group': grps
})

# 3. Simulate MFA Compliance Behavior
# Control group naturally has lower compliance (approx 35%)
# Variant group has forced compliance via soft-block (approx 88%)
def simulate_compliance(grp):
    if grp == 'Control':
        return np.random.choice([1, 0], p=[0.35, 0.65])
    else:
        return np.random.choice([1, 0], p=[0.88, 0.12])
df['mfa_compliant'] = df['test_group'].apply(simulate_compliance)

# 4. Simulate Time-to-Compliance (Days)
# Improvement: Track HOW LONG it takes users to comply
def simulate_time_to_compliance(row):
    if row['mfa_compliant'] == 0:
        return np.nan # Did not comply
    if row['test_group'] == 'Control':
        return np.random.randint(1, 31) # Comply anytime in 30 days
    else:
        return np.random.randint(1, 4)  # Comply within the 3-day grace period (or slightly after)
df['days_to_comply'] = df.apply(simulate_time_to_compliance, axis=1)

# 5. Simulate IT Support Ticket Generation
# Control group generates fewer tickets (approx 4%)
# Variant group generates more tickets due to friction (approx 18%)
def simulate_tickets(grp):
    if grp == 'Control':
        return np.random.choice([1, 0], p=[0.04, 0.96])
    else:
        return np.random.choice([1, 0], p=[0.18, 0.82])

df['generated_ticket'] = df['test_group'].apply(simulate_tickets)

# Export for Power BI
df.to_csv("D:/Mini Project/mfa_experiment_dataset.csv", index=False)
print("-> Successfully generated 5,000 user profiles and exported to 'mfa_experiment_dataset.csv'")

# Phase 2: Statistical Inference Engine
print("\nExecuting Statistical Inference Engine (Z-Tests)...")

# Separate groups
ctrl = df[df['test_group'] == 'Control']
varin = df[df['test_group'] == 'Variant']

# Metric 1: MFA Compliance Rate
successes_comp = [varin['mfa_compliant'].sum(), ctrl['mfa_compliant'].sum()]
nobs_comp = [len(varin), len(ctrl)]
z_stat_comp, p_val_comp = proportions_ztest(successes_comp, nobs_comp, alternative='larger')
print("\n--- Metric 1: MFA Compliance Rate ---")
print(f"Control Compliance Rate: {ctrl['mfa_compliant'].mean():.2%}")
print(f"Variant Compliance Rate: {varin['mfa_compliant'].mean():.2%}")
print(f"Z-Statistic: {z_stat_comp:.4f}, P-Value: {p_val_comp:.4e}")
if p_val_comp < 0.05:
    print("Result: STATISTICALLY SIGNIFICANT INCREASE in compliance for the Variant group.")

# Metric 2: IT Support Ticket Generation Rate
successes_tick = [varin['generated_ticket'].sum(), ctrl['generated_ticket'].sum()]
nobs_tick = [len(varin), len(ctrl)]
z_stat_tick, p_val_tick = proportions_ztest(successes_tick, nobs_tick, alternative='larger')
print("\n--- Metric 2: IT Ticket Generation Rate ---")
print(f"Control Ticket Rate: {ctrl['generated_ticket'].mean():.2%}")
print(f"Variant Ticket Rate: {varin['generated_ticket'].mean():.2%}")
print(f"Z-Statistic: {z_stat_tick:.4f}, P-Value: {p_val_tick:.4e}")
if p_val_tick < 0.05:
    print("Result: STATISTICALLY SIGNIFICANT INCREASE in IT support overhead for the Variant group.")
print("\nPipeline Execution Complete. Data is ready for Power BI Import.")