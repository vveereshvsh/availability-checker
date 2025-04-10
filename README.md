
# Availability Checker

This project is an availability checker for a list of endpoints. It checks the availability of each endpoint at regular intervals and logs the results.

## Summary of Key Issues Identified and Changes Made:

The original code had several issues that impacted its functionality, reliability, and maintainability. These were identified during a code review, and the following changes were made to improve the code:

1. **Missing Domain and Endpoint Variables**:
   - The code had unreferenced variables (`domain`, `endpoint`) that caused runtime errors. These variables were either used before being defined or referenced without being assigned values. 
   - **Change**: Corrected variable usage, ensuring they were defined and referenced properly to avoid errors.

2. **Invalid Endpoint Handling**:
   - The code didn't handle invalid or missing endpoints gracefully, which could lead to unexpected crashes.
   - **Change**: Added validation for the presence and structure of endpoint data before processing. Introduced error handling around endpoint requests.

3. **Hardcoded Configuration**:
   - Configuration values like check intervals and URL paths were hardcoded in the script, which reduces flexibility.
   - **Change**: Introduced configuration through a YAML file, allowing users to easily modify endpoints and settings without changing the script.

4. **Improper Logging**:
   - Logs didn’t provide enough detail to trace the flow or issues in the system effectively.
   - **Change**: Improved logging to include the status, latency, availability of endpoints, and cumulative availability in a readable format.

5. **Inefficient Sleep Mechanism**:
   - The sleep mechanism used after each cycle was inefficient, potentially causing unnecessary delays in the execution loop.
   - **Change**: Optimized the sleep interval to ensure that checks happen at the desired frequency without unnecessary waiting.

## Installation Instructions

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Running the Code

1. Ensure you have a valid configuration YAML file, such as `sample.yaml`.

2. Run the script with the YAML file:

   ```bash
   python main.py sample.yaml
   ```

   This will start the availability check loop, and the results will be logged.

## Configuration

The script expects a configuration file in YAML format, which should include a list of endpoints to check. Here's an example `sample.yaml`:

```yaml
endpoints:
  - name: "Fetch Rewards API"
    url: "https://api.fetchrewards.com"
  - name: "Example Service"
    url: "https://example.com"
```

## Code Overview

### `main.py`

- The main script that loads configuration from a YAML file, checks the endpoints, and logs the results.
- It supports dynamic checking of endpoints at regular intervals and logs the cumulative availability.

### `checker.py`

- This file contains the logic for checking the availability of an endpoint by sending a request to the URL and returning the status, latency, and availability.

### `tracker.py`

- This file contains the `AvailabilityTracker` class, which tracks the cumulative availability of each domain and provides methods for updating and retrieving availability data.

### `utils.py`

- This file contains utility functions, such as `load_config()` for loading the YAML configuration file and `normalize_domain()` for formatting endpoint URLs.

## Issues Addressed

The following issues were identified in the code and have been resolved:
- Ensuring all variables are correctly referenced and defined.
- Handling invalid or missing endpoints to prevent crashes.
- Replacing hardcoded configurations with external YAML files for easier management.
- Enhancing logging for better visibility into system performance.
- Optimizing the sleep mechanism to avoid unnecessary delays.

## Future Improvements

1. Add support for different HTTP methods (POST, PUT, etc.).
2. Implement retry mechanisms for failed endpoint checks.
3. Add notifications or alerts when certain thresholds are crossed (e.g., when availability falls below a certain percentage).

---

