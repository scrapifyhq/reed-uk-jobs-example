import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });

const run = await client.actor('scrapefy/reed-jobs-scraper-uk').call({
    keywords: ['python developer'],
    locations: ['London'],
    minSalary: 50000,
    hideJobsWithoutSalary: true,
    permanent: true,
    maxAgeDays: 7,
    maxItems: 50,
});

const { items } = await client.dataset(run.defaultDatasetId).listItems();
for (const job of items) {
    console.log(job.title, '|', job.company, '|', job.salaryFrom, '-', job.salaryTo, job.salaryPeriod);
}
