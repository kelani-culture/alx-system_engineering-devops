# Postmortem: User Authentication Service Outage

## Issue Summary
- **Duration:** April 10, 2024, 10:00 AM - April 11, 2024, 2:00 AM (UTC)
- **Impact:** The user authentication service was down for approximately 16 hours, affecting 80% of users who attempted to log in during this time.
- **Root Cause:** A misconfiguration in the load balancer settings led to an overload on the authentication service, causing it to crash.

## Timeline
- **April 10, 2024, 10:00 AM:** Issue detected by monitoring alert indicating high server load.
- **April 10, 2024, 10:15 AM:** I investigated backend servers for potential issues, suspecting database overload.
- **April 10, 2024, 11:00 AM:** Misleading assumption made that database replication lag was the cause; additional investigation commenced.
- **April 10, 2024, 12:30 PM:** Incident escalated to infrastructure team for further analysis.
- **April 10, 2024, 2:00 PM:** Root cause identified as misconfigured load balancer leading to uneven distribution of traffic.
- **April 10, 2024, 4:00 PM:** Load balancer settings adjusted to evenly distribute traffic; authentication service restarted.
- **April 11, 2024, 2:00 AM:** Service fully restored, incident resolved.

## Root Cause and Resolution
- **Root Cause:** Misconfigured load balancer settings caused uneven distribution of traffic, leading to overload on the authentication service.
- **Resolution:** Load balancer settings were adjusted to evenly distribute traffic across backend servers. Additionally, a thorough review of load balancer configurations was conducted to prevent similar issues in the future.

## Corrective and Preventative Measures
- **Improvements/Fixes:**
  - Implement automated checks for load balancer configurations to ensure uniform traffic distribution.
  - Enhance monitoring systems to provide real-time alerts for abnormal server loads.
  - Conduct regular audits of system configurations to identify and rectify potential issues proactively.
- **Tasks:**
  1. Implement automated load balancer configuration checks by April 15, 2024.
  2. Enhance monitoring system to provide real-time alerts for abnormal server loads by April 20, 2024.
  3. Schedule regular audits of system configurations, with the first audit to be completed by April 30, 2024.

