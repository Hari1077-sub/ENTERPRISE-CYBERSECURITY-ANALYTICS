Enterprise Cybersecurity Analytics: A Data-Driven A/B Testing Framework for MFA Compliance

**Authors:** Anand S, Hariharan M, Hariharan S
**Guide:** Mr. Ravi Rajesh AP / AI&DS
**Institution:** V.S.B College of Engineering Technical Campus, Coimbatore

---

1. Abstract
Unsecured employee credentials and endpoints remain leading vectors for corporate data breaches and ransomware attacks, making rapid Multi-Factor Authentication (MFA) adoption critical. However, organizations struggle to achieve high compliance without disrupting productivity or surging helpdesk tickets. 

This project establishes an automated, statistically rigorous A/B Testing Framework. Using Python (Pandas, NumPy, SciPy, Statsmodels) and Power BI, the system programmatically generates a synthetic dataset of 5,000 corporate employee profiles in a 50/50 split. It evaluates a **Control Group (Version A: passive 30-day email reminders)** against a **Variant Group (Version B: active soft-block with a 3-day grace period)**. By tracking the MFA Compliance Rate (%) and IT Ticket Rate (%) using a two-sample proportion Z-test at a 95% confidence level ($\alpha$ = 0.05), this approach translates behavioral logs into actionable, data-backed policy recommendations.

---

2. Project Enhancements (Beyond Baseline)
To elevate the analytical depth of the project while remaining strictly within the original scope, the following data points were engineered into the Python Analytics Pipeline:
1. **Departmental Stratification:** Employees are assigned to departments (Engineering, Sales, Finance, HR, Operations). This allows us to observe if certain demographics (e.g., technical vs. non-technical) react differently to the active soft-block.
2. **Time-to-Compliance (TTC) Metric:** We track the exact number of days it takes an employee to comply. This highlights the urgency created by the Variant group (clustering around days 1-3) compared to the Control group (spread thinly across 30 days).

---

3. Methodology & Architecture

 Phase 1: Synthetic Experimentation Engine
A Python script generates `mfa_experiment_dataset.csv` simulating 5,000 user profiles. The logic accurately mimics real-world enterprise behaviors, projecting a ~35% natural compliance rate for the passive group and an ~88% forced compliance rate for the active group.
 
 Phase 2: Core Metric Evaluation
We isolate two competing metrics to illustrate the "Security vs. Friction Trade-Off":
* **Primary Security Metric:** MFA Compliance Rate (Goal: Maximize)
* **Primary Operational Metric:** IT Support Ticket Rate (Goal: Minimize)

 Phase 3: Statistical Inference Engine (Hypothesis Testing)
We perform a two-sample proportion Z-test for both metrics. 
* **Null Hypothesis ($H_0$):** There is no difference in compliance/ticket rates between the Control and Variant groups.
* **Alternate Hypothesis ($H_1$):** The Variant group has a significantly higher rate.
The engine calculates the Z-statistic and P-value, evaluating against $\alpha$ = 0.05 to definitively prove policy efficacy.

---

4. Power BI Implementation Guide

To complete the end-to-end framework, use the generated `mfa_experiment_dataset.csv` in Microsoft Power BI to build an Executive Dashboard. Follow these visualization steps:

 A. Core KPIs (Top Banner)
* **Overall Compliance Rate:** Card visual displaying the global MFA adoption.
* **Variant vs Control Compliance:** Two distinct KPI cards showing the stark difference (e.g., 88% vs 35%).
* **Ticket Surge:** Card showing the total helpdesk tickets generated during the experiment.

 B. Analytical Visuals (Main Body)
1. **Compliance by Test Group (Donut Chart):**
   * *Legend:* `test_group`
   * *Values:* Count of `mfa_compliant` (Filtered to 1)
   * *Purpose:* Visually proves the Variant's superiority.
2. **Compliance across Departments (Clustered Bar Chart):**
   * *X-Axis:* `department`
   * *Y-Axis:* % of Total `mfa_compliant`
   * *Legend:* `test_group`
   * *Purpose:* Shows if technical departments (Engineering) adapted to the soft-block faster than others.
3. **Time-to-Compliance Distribution (Line Chart):**
   * *X-Axis:* `days_to_comply`
   * *Y-Axis:* Count of `employee_id`
   * *Legend:* `test_group`
   * *Purpose:* Shows a massive spike at Day 3 for the Variant group (the grace period deadline), proving the behavioral nudge works.

 C. The Trade-Off Visual
* **Scatter Plot or Dual-Axis Chart:** Plot Compliance Rate (%) against IT Ticket Rate (%) by Department. This visually summarizes the entire thesis: achieving high security compliance inherently generates a temporary spike in operational friction.

---

5. Conclusion
By translating employee behavioral logs into clear statistical metrics and visual evidence, this framework empowers IT leadership to enforce effective compliance mandates, safeguarding digital assets while proactively managing workplace productivity and helpdesk resources.
