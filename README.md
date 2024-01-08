# Network Quality Testing Tool

## Introduction
The Network Quality Testing Tool is designed to assess the latency, Round-Trip Time (RTT), and retrieve certification information for a specified target IP or URL.

## Prerequisites
Ensure the following prerequisites are met before using the tool:
- Python > 3
- The `requests` module is installed using pip.
- The SSL module is installed.

## Usage
1. **Initialization:**
   - Create an object of `NetworkQualityTesting()` with the target URL, timeout, and SSL verification parameters.
   ```python
   obj = NetworkQualityTesting(url="https://www.google.com/", timeout=5, verify=false)
   ```

2. **Get Latency:**
   - Retrieve the latency of the target URL.
   ```python
   print(obj.latency())
   ```
3. **Round-Trip Time (RTT):**
   - Retrieve the latency of the target URL.
   ```python
   print(obj.rtt())
   ```
4. **Get Certification Information:**
   - Retrieve the latency of the target URL.
   ```python
   print(obj.cert_info())
   ```    
