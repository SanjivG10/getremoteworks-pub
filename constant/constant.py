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
                "employment_type": "br+ .company",
                "location":".region",
                "date_posted": "time",
                "category":"h2 a:nth-child(1)",
                "link":'li a[href^="/remote-jobs/"]'
            }
        }
    },
    "monster": {
        "link":"https://appsapi.monster.io/jobs-svx-service/v2/monster/search-jobs/samsearch/en-US?apikey=",
    },
    "ziprecruiter": {
        "link":"https://www.ziprecruiter.co.uk/Jobs-/Remote?utm_source=zr_trending_hp&page=",
        "selectors": {
            "job_list":"ul.jobList > li",
            "each_content": {
                "title": "ul.jobList li strong" ,
                "link":'ul.jobList a',
                "company":".jobList-introMeta li:nth-child(1)",
                "location":".jobList-introMeta li+ li",
                "date_posted": ".jobList-date",
                "description":".jobList-description"
            } 
        }
    },
    "simplyhired": {
        "link":"https://www.simplyhired.com/search?q=&l=remote",
        "selectors": {
            "job_list":'div[data-testid="searchSerpJob"]',
            "each_content": {
                "title": "h2" ,
                "link":'a',
                "company":'span[data-testid="searchSerpJobLocation"]',
                "date_posted": "p[data-testid='searchSerpJobDateStamp']",
                "description":"p[data-testid='searchSerpJobSnippet']"
            } 
        }
    },
    "euremotejobs":{
        "link": "https://euremotejobs.com/jm-ajax/get_listings/",
        "selectors":{
            "job_list": "li.job_listing",
            "each_content": {
                "title": ".job_listing-title" ,
                "link":'.job_listing-clickbox',
                "company":'.job_listing-company',
                "date_posted": ".job_listing-date",
                "employment_type":".job_listing-type",
                "location":".job_listing-location"
            } 
        }
    }
}