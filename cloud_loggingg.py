import os
import pprint
from google.cloud import logging_v2

from google.cloud.logging import ASCENDING
from google.cloud.logging import DESCENDING

os.environ['GCLOUD_PROJECT'] = 'core-commerce-dev'

pp = pprint.PrettyPrinter(indent=1)

FILTER = 'resource.type="k8s_container" AND resource.labels.cluster_name="management-dev-gke-cluster" AND resource.labels.namespace_name="promotion-definition"'

client = logging_v2.Client()

iterator = client.list_entries(filter_=FILTER, order_by=DESCENDING)
page = next(iterator)
# for page in iterator.pages:
#   print('    Page number: %d' % (iterator.page_number,))
#   print('  Items in page: %d' % (page.num_items,))
#   print('Items remaining: %d' % (page.remaining,))
#   print('Next page token: %s' % (iterator.next_page_token,))
#   print('----------------------------')
for entry in page:
    print(entry)
