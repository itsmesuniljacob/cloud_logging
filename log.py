#!./venv/bin/python
from google.cloud import logging
from google.cloud.logging import DESCENDING
import pprint
import argparse
import os

os.environ['GCLOUD_PROJECT'] = 'core-commerce-dev'
FILTER = 'resource.type="k8s_container"                                     \
          AND resource.labels.cluster_name="management-dev-gke-cluster"     \
          AND resource.labels.namespace_name="promotion-definition"        \
          AND jsonPayload.request_id="1405f6fc-9041-443c-b16b-6e9f703e1d7f"'

# [START logging_list_log_entries]
def list_entries():
    """Lists the most recent entries for a given logger."""
    logging_client = logging.Client()
    # logger = logging_client.logger(logger_name)

    print("Listing entries for logger {}:".format('test'))

    for entry in logging_client.list_entries(filter_=FILTER, order_by=DESCENDING,page_size=5):
        timestamp = entry.timestamp.isoformat()
        print("* {}: {}".format(timestamp, entry.payload))

list_entries()
# [END logging_list_log_entries]


# if __name__ == "__main__":
#     parser = argparse.ArgumentParser(
#         description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
#     )
#     parser.add_argument("logger_name", help="Logger name", default="example_log")
#     subparsers = parser.add_subparsers(dest="command")
#     subparsers.add_parser("list", help=list_entries.__doc__)
    # subparsers.add_parser("write", help=write_entry.__doc__)
    # subparsers.add_parser("delete", help=delete_logger.__doc__)

    # args = parser.parse_args()
    #
    # if args.command == "list":
    #     list_entries(args.logger_name)
    # elif args.command == "write":
    #     write_entry(args.logger_name)
    # elif args.command == "delete":
    #     delete_logger(args.logger_name)
