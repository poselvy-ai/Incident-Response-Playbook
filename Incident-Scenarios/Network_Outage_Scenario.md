# Network Outage Scenario — DC1 Core Switch Failure  
Acme Company — July 21, 2026

This scenario provides a concise, professional incident walkthrough suitable for SRE, IT Operations, and engineering teams. It summarizes the major outage at DC1, the escalation path, key decisions, and final resolution.

---

## 1. Executive Summary

On July 21, 2026, Acme Company experienced a major outage in Data Center 1 (DC1) beginning at **09:12 AM PDT**. A thermal event in Rack R14 caused failure of the **core switch**, **two power supplies**, and **cooling unit CU‑3**, resulting in widespread service disruption across internal applications, VDI, external customer services, and cloud connectivity.

The incident escalated from **SEV‑3 → SEV‑4** due to business impact, customer escalation, and failure of automatic failover. Full restoration was achieved by **11:20 AM PDT** after replacing the core switch and associated hardware.

---

## 2. Impact Summary

### Systems Impacted
- VDI (Region A)  
- Internal applications (Accounting, Sales, PMO)  
- External customer applications  
- AWS Direct Connect  
- VPN concentrator  
- DC1 core networking  

### Business Impact
- Full outage for internal and external users  
- Accounting and Sales operations halted  
- Enterprise customers escalated (NorthStar, BluePeak)  
- SLA breach at **10:42 AM**  
- Significant reputational and financial risk  

---

## 3. Detection

At **09:12 AM**, multiple monitoring systems reported:

- Core switch DC1CSW01 unreachable  
- Downstream switches orphaned  
- VDI broker dependency failures  
- VPN concentrator reporting “no upstream gateway”  
- Service desk reporting widespread user outages  

Initial severity: **SEV‑3**

---

## 4. Escalation Path

| Time   | Action                                                |
|--------|--------------------------------------------------------|
| 09:12  | Detection — monitoring alerts + user reports          |
| 09:20  | Escalated to SEV‑3                                    |
| 09:25  | Bridge opened — Networking, DC Ops, DevOps, VDI, CS   |
| 09:40  | DC Ops confirms thermal event in Rack R14             |
| 09:45  | Networking identifies corrupted STP/BGP packets       |
| 10:00  | Power cycle attempted — partial stabilization         |
| 10:00  | Escalated to SEV‑4 due to business impact             |
| 10:20  | Executive approval for hardware replacement           |
| 10:25  | Replacement of core switch + PSUs + CU‑3 begins       |
| 11:20  | Full restoration — de-escalated to SEV‑1              |

---

## 5. Key Technical Findings

### Thermal Event
- Rack R14 temperature **20°F above normal**  
- Cooling unit CU‑3 compressor failure  
- Core switch overheating  

### Hardware Failures
- PSU1: critical fault  
- PSU2: warning state  
- CU‑3: offline  
- Core switch: sending corrupted STP/BGP packets  

### Network Behavior
- Failover to redundant core switch failed  
- OOB console unreachable  
- Downstream switches orphaned  
- AWS Direct Connect degraded  
- VPN concentrator unreachable  

---

## 6. Decision Points

### Migration vs. Repair
- DevOps confirmed migration was possible for some apps  
- VDI and VPN could not be migrated  
- Migration would cause **45–60 minutes** of additional downtime  
- **Decision:** Restore DC1 instead of migrating

### Stabilize vs. Replace Core Switch
- Stabilization confidence: **20–30%**  
- Replacement ETA: **~55 minutes**  
- Risk of refailure high  
- **Decision:** Replace core switch + PSUs + CU‑3

### Customer & Compliance
- SLA breach confirmed at **10:42 AM**  
- Enterprise customers escalated  
- Leadership intervened directly with BluePeak Logistics  
- Compliance prepared formal SLA breach notice  

---

## 7. Final Resolution

Hardware replaced:
- Core Switch DC1CSW01  
- PSU1  
- PSU2  
- Cooling Unit CU‑3  

Post-repair actions:
- Routing tables rebuilt  
- Downstream switches synced  
- VDI dependency checks passed  
- AWS Direct Connect restored  
- VPN concentrator restored  
- Customer services fully operational  

**Full restoration achieved at 11:20 AM.**  
Incident de-escalated to **SEV‑1** and assigned to IT Ops for closeout.

---

## 8. Customer Notification (Final)

> Your service has been restored. The failure was caused by a faulty core switch in our DC1 facility.  
> Our technicians replaced the switch and rebuilt routing tables to restore connectivity.  
> We will continue monitoring for 24 hours.  
> A full RCA will be published shortly.

---

## 9. Lessons Learned

- Thermal monitoring gaps allowed overheating to go undetected  
- Failover logic failed due to corrupted control-plane traffic  
- VDI dependency on DC1 created a single point of failure  
- Customer communication cadence stabilized sentiment  
- Early leadership involvement reduced enterprise escalation pressure  
