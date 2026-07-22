# Scenario 3 — Application/API Outage (SEV‑4 → SEV‑2)
Summary based on OP Lead decisions and incident actions

---

## Executive Summary
A major outage impacted Acme’s API services due to a runaway database query originating from FINCO, a top financial enterprise customer. The query saturated CPU, exhausted the DB connection pool, and caused widespread HTTP 500 errors across all regions. The incident was escalated to SEV‑4 due to regulatory and contractual risk. The OP Lead coordinated DB, DevOps, Cloud, Compliance, and Executive Leadership to stabilize the platform by terminating the runaway query and applying rate limiters. All services recovered fully, and the incident was de‑escalated to SEV‑2 with an RCA scheduled within 24 hours.

---

## Detection
- API Gateway reporting **4,200 HTTP 500 errors/min**
- Latency breaches (1.8s → 2.6s)
- API containers entering **CrashLoopBackOff**
- DB CPU pegged at **95–98%**
- Connection pool saturation
- Cloud autoscaling failing readiness checks
- Customer Support reporting widespread impact
- FINCO P1 ticket opened

---

## Initial Actions (OP Lead)
- Declared **SEV‑3**
- Opened bridge
- Notified DevOps, Network, DB, Cloud
- Issued initial customer communication
- Sent leadership notification with 15‑minute cadence

---

## Team Findings

### Database Team
- Runaway query from **Tenant‑47 (FINCO)**
- Full table scans without pagination
- ~900 queries/sec
- CPU saturation and connection pool exhaustion
- Query confirmed **read‑only** (no corruption risk)

### DevOps
- API containers restarting repeatedly
- Readiness probes failing
- Error logs showing DBTimeoutException and ConnectionPoolExhausted
- Autoscaling paused due to DB latency

### Cloud
- Load balancer showing global 500 errors
- Latency spikes across all regions
- No cloud provider outage

### Network
- No packet loss
- No routing anomalies
- No firewall issues

### Customer Support
- 112+ tickets opened
- FINCO reporting severe delays
- Enterprise customers requesting ETA

---

## Escalation to SEV‑4
Due to:
- FINCO being a top financial customer
- Regulatory exposure
- Contractual risk
- Potential statutory reporting requirements

Actions:
- Notified Executive Leadership and Compliance
- Delivered SEV‑4 executive communication
- Maintained 10‑minute cadence

---

## Mitigation Actions (OP Lead)

### Directive to DB Team
- **Kill runaway query immediately**
- **Apply rate limiters** to FINCO’s offending endpoint

### Results
- DB CPU dropped from 98% → 42%
- Connection pool freed from 100% → 35%
- DB latency normalized (12–18ms)
- Slow query backlog cleared

### DevOps Recovery
- API containers stabilized
- Readiness probes passing 100%
- Error rate dropped from 3,800/min → 0/min
- Autoscaling resumed normally

### Cloud Recovery
- LB errors cleared globally
- Latency normalized (120–140ms)

### Customer Support
- FINCO informed of root cause and mitigation
- No data integrity issues reported
- FINCO service restored

