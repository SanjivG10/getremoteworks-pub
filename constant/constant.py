JOB_DATA = {
    "remote_ok": {
        "link":"https://remoteok.com/?&action=get_jobs&offset=",
        "selectors":{
            "job_list":"tr",
            "each_content":"script"
        }
    },
    "weworkremotely": {
        "link":"https://weworkremotely.com",
        "selectors": {
            "job_list":"article ul li",
            "each_content": {
                "title": ".title" ,
                "company":".company:nth-child(1)",
                "employmentType": "br+ .company",
                "location":".region",
                "date_posted": "time",
                "category":"h2 a:nth-child(1)",
                "link":'li a[href^="/remote-jobs/"]'
            }
        }
    }
}