# Severity Classification Matrix (Impact vs Urgency)

This Severity Matrix is used to classify incidents consistently across the organization. It determines the correct SEV level based on business impact and urgency. The matrix is intentionally numeric (SEV-0 → SEV-4) because severity definitions live outside the matrix. This follows industry-standard SRE, NOC, and enterprise Ops practices.

---

# 1. [Severity Matrix Grid](diagrams/severity-matrix.png ) 

| Urgency \ Impact | None | Low | Moderate | High |
|------------------|------|-----|----------|------|
| Low              | SEV-0 | SEV-1 | SEV-2 | SEV-3 |
| Medium           | SEV-1 | SEV-2 | SEV-3 | SEV-4 |
| High             | SEV-2 | SEV-3 | SEV-4 | SEV-4 |
| Immediate        | SEV-3 | SEV-4 | SEV-4 | SEV-4 |

---

# 2. Severity Definitions

**SEV-0 — Observation / No Impact**  
- No customer impact  
- No service degradation  
- Logged for awareness only  

**SEV-1 — Minor Issue**  
- Low impact  
- No outage  
- No SLA breach  
- Handled by L1 or single team  

**SEV-2 — Incident / Moderate Impact**  
- Noticeable degradation  
- Some customers affected  
- SLA risk  
- Multi-team involvement possible  

**SEV-3 — Major Incident**  
- Significant impact  
- Large customer segment affected  
- SLA breach likely  
- Bridge initiated  
- Incident Commander assigned  

**SEV-4 — Critical Incident**  
- Full outage or severe degradation  
- High business impact  
- Regulatory or financial risk  
- Executive and compliance notification required  
- Full incident bridge with all teams  

---

# 3. Why the Matrix Uses SEV Numbers (Not Words Like “Critical”)

Severity matrices classify severity — they do not describe it.

The matrix answers:
> “Given impact and urgency, what SEV level does this incident fall into?”

It does **not** answer:
> “What does that SEV level mean?”

The meaning of each SEV level is defined in the **Severity Definitions** section above.

This is standard across:
- AWS  
- Azure  
- Google SRE  
- Fortune 500 Ops teams  
- Healthcare/Finance regulated Ops  
- Government/Defense Ops  

The matrix stays numeric because:
- It keeps the grid clean  
- It prevents clutter  
- It avoids mixing classification with description  
- Color coding already communicates severity  
- SEV-4 inherently means Critical  

---

# 4. Color Coding (Recommended for Diagrams)

Use these colors when building the PNG diagram:

- **SEV-0 → Gray (#D9D9D9)**  
- **SEV-1 → Green (#A8D08D)**  
- **SEV-2 → Yellow (#FFD966)**  
- **SEV-3 → Orange (#F4B183)**  
- **SEV-4 → Red (#E06666)**  

This makes the matrix visually intuitive and easy to scan during an incident.

---

# 5. How to Use This Matrix During an Incident

1. Determine **Impact**  
   - None, Low, Moderate, High  

2. Determine **Urgency**  
   - Low, Medium, High, Immediate  

3. Cross-reference the grid  
   - The cell gives you the SEV level  

4. Trigger escalation based on SEV  
   - SEV-2 → Notify Ops Lead  
   - SEV-3 → Start bridge  
   - SEV-4 → Leadership + Compliance  

5. Begin communication cadence  
   - Every 10–30 minutes depending on severity  

6. After resolution, complete RCA  
   - SEV-3 and SEV-4 require full RCA  
