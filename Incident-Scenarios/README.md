[← Back to README](../README.md)

# Incident Scenarios

Example incidents used for training, simulation and operational readiness. Severity uses the playbook scale: **SEV-1 (critical) to SEV-5 (informational)**. See the [Severity Matrix](../Severity-Matrix.md).

| Scenario | Severity path | Summary |
|----------|---------------|---------|
| [Application / API Outage](API-Outage.md) | SEV-2 → SEV-1 → SEV-3 | Runaway customer DB query exhausts the connection pool; global HTTP 500s; regulatory risk drives SEV-1 |
| [Network Outage: DC1 Core Switch](Network-Outage.md) | SEV-2 → SEV-1 → SEV-4 | Thermal event takes out the DC1 core switch; failover fails; hardware replaced |
| [VDI Broker Failure](VDI-Broker-Failure.md) | SEV-3 → SEV-4 | Packet loss on a DC1 uplink breaks VDI authentication; traffic rerouted, optic replaced |

---

[← Back to README](../README.md)
