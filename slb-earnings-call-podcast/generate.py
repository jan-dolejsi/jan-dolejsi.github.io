from datetime import datetime
import pytz
from feedgen.feed import FeedGenerator
fg = FeedGenerator()
fg.load_extension('podcast')
fg.podcast.itunes_category('SLB', 'Earnings')
fg.title("SLB Earnings Conference Calls")
fg.logo('https://investorcenter.slb.com/sites/g/files/knoqqb79571/files/Favicon-blue.png')
fg.link(link={'href': "http://slb.com", 'rel': 'self'})
fg.description("SLB (also known as Schlumberger Limited) (NYSE:SLB) is a global technology company, driving energy innovation for a balanced planet.")
fg.link(href='https://jan-dolejsi.github.io/slb-earnings-call-podcast/schlumberger-earnings-conference-calls-podcast.xml', rel='self' )
fg.language('en')
fg.pubDate(datetime.today().replace(tzinfo=pytz.utc))

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