import os
from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run_input = {
    "keywords": ["python developer"],
    "locations": ["London"],
    "minSalary": 50000,          # GBP per year
    "hideJobsWithoutSalary": True,
    "permanent": True,
    "maxAgeDays": 7,             # exact posting-date cut-off
    "maxItems": 50,              # hard cap on cost
}

run = client.actor("scrapefy/reed-jobs-scraper-uk").call(run_input=run_input)

for job in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(job["title"], "|", job["company"], "|", job["salaryFrom"], "-", job["salaryTo"], job["salaryPeriod"])
