## OpenSSH
OpenSSH (Open Secure Shell) is a widely used suite of secure networking tools based on the SSH (Secure Shell) protocol. It ensures encrypted communication over unsecured networks, supporting secure remote access, file transfers, and tunneling. These logs capture authentication attempts, connection events, and security-related activities, making them valuable for security research, incident response, and SRE automation.

### Files
- **auth.log** – Raw log file.
- **openssh_access_parsed.csv** – Parsed log file with the following fields:  
  `LineNumber`, `Timestamp`, `Host`, `PID`, `Message`
- **openssh_action_types.csv** – Indexed list of unique log event types extracted from the log file.

This dataset is useful for analyzing SSH access patterns, identifying malicious activities, and improving automated security monitoring.

### About this repo
[Rootly](https://rootly.com/) is an AI-powered on-call and incident response platform trusted by companies like Canva, Cisco, LinkedIn and NVIDIA. As part of our effort to constantly improve our AI features and to give back to the community, we are maintaining a dataset of system logs  – both access and error – openly accessible for researching, benchmarking and training AI-powered tools. Our dataset are logs from real production environments.

Please cite us this repo if you use our dataset and feel free to contribute by submitting a PR. ❤️
