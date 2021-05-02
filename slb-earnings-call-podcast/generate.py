from datetime import datetime
from feedgen.feed import FeedGenerator
fg = FeedGenerator()
fg.load_extension('podcast')
fg.podcast.itunes_category('Schlumberger', 'Earnings')
fg.title("Schlumberger Earnings Conference Calls")
fg.logo('https://www.slb.com/-/media/images/logo/logo-white.ashx') # this is an svg white on black image
fg.link(link={'href': "http://slb.com", 'rel': 'self'})
fg.description("Schlumberger (SLB: NYSE) is a technology company that partners with customers to access energy. Our people, representing over 160 nationalities, are providing leading digital solutions and deploying innovative technologies to enable performance and sustainability for the global energy industry. With expertise in more than 120 countries, we collaborate to create technology that unlocks access to energy for the benefit of all.")
fg.link(href='https://jan-dolejsi.github.io/slb-earnings-call-podcast/schlumberger-earnings-conference-calls-podcast.xml', rel='self' )
fg.language('en')

# https://investorcenter.slb.com/events/event-details/q4-2020-schlumberger-earnings-conference-call
# https://earningscast.com/SLB/20201016

import csv
with open('episodes.csv', newline='') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        if csvreader.line_num == 1:
            # print(', '.join(row))
            # header
            pass
        else:
            print('Exporting', row[1], '-', row[2])
            fe = fg.add_entry()
            fe.id(row[3])
            fe.title(row[1])
            fe.description(row[2])
            fe.enclosure(row[3], row[4], 'audio/mpeg')
            fe.link(link={'href': row[5]})
            fe.pubDate(row[0] + "T00:00:00+00:00")

fg.rss_str(pretty=True)
fg.rss_file('schlumberger-earnings-conference-calls-podcast.xml')