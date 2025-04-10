import argparse
import sys
import time
import logging
from checker import check_endpoint
from tracker import AvailabilityTracker
from utils import load_config, normalize_domain

# Set up logging configuration
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s: %(message)s"
)

CHECK_INTERVAL_SECONDS = 15


def main():
    # Set up argument parsing
    parser = argparse.ArgumentParser(description="Endpoint Availability Checker")
    parser.add_argument("config", help="Path to the YAML configuration file")
    args = parser.parse_args()

    try:
        # Load the endpoints from the provided YAML config file
        endpoints = load_config(args.config)
        tracker = AvailabilityTracker()

        logging.info(f"Loaded {len(endpoints)} endpoints from config.")

    except Exception as e:
        logging.error(f"Failed to load configuration: {e}")
        sys.exit(1)

    # Loop indefinitely to check the availability of endpoints
    while True:
        cycle_start = time.time()

        # Iterate through all the endpoints
        for endpoint in endpoints:
            try:
                result = check_endpoint(endpoint)
                domain = normalize_domain(endpoint["url"])
                tracker.update(domain, result["available"])
                logging.info(
                    f"[{domain}] {result['status']} - {result['latency']}ms - Available: {result['available']}")

            except Exception as e:
                logging.error(f"Error checking endpoint {endpoint['url']}: {e}")

        # Log the cumulative availability by domain
        for domain, availability in tracker.get_all().items():
            logging.info(f"[{domain}] Cumulative Availability: {availability:.2f}")

        # Ensure the cycle runs every CHECK_INTERVAL_SECONDS
        cycle_duration = time.time() - cycle_start
        time.sleep(max(0, CHECK_INTERVAL_SECONDS - cycle_duration))


if __name__ == "__main__":
    main()
