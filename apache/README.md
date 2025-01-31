# Apache

Apache HTTP Server is one of the most widely used web servers, powering millions of websites worldwide. It provides robust logging capabilities, recording access requests, errors, and security-related events. These logs are essential for analyzing web traffic, diagnosing issues, identifying security threats, and improving server performance.

## Files

- **apache_access.log** – Raw access log file.
- **apache_access_parsed.csv** – Parsed log file containing the following fields:  
  ```LogID, Timestamp, ClientIP, HTTPMethod, StatusCode, RequestPath, Referer, UserAgent```
- **apache_access_types.csv** – Indexed list of unique HTTP request types found in the access logs.
- **apache_error.log** – Raw error log file.
- **apache_error_parsed.csv** – Parsed error log file with the following fields:  
  ```LogID, Timestamp, LogLevel, Message```
- **apache_error_types.csv** – Indexed list of unique error message types found in the error logs.

This dataset is useful for web security research, detecting malicious behavior, optimizing server performance, and training AI-powered monitoring tools.

## About this Repo

[Rootly](https://rootly.com/) is an AI-powered on-call and incident response platform trusted by companies like Canva, Cisco, LinkedIn and NVIDIA. As part of our effort to constantly improve our AI features and to give back to the community, we are maintaining a dataset of system logs  – both access and error – openly accessible for researching, benchmarking and training AI-powered tools. Our dataset are logs from real production environments.

If you use this dataset, please cite this repository. Contributions are welcome via PRs. ❤️
