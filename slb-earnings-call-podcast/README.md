# Schlumberger Earnings Call recordings as a podcast

The best part of the earnings call is the questions from the investors.
One can understand from their questions how they measure success and what their expectations are.
But comparing to lot of other audible content, those earning podcasts were always much more tedious to listen to.
While they are all public content, they are not consistently organized into a podcast that would automatically download to my listening queue, when published.
The last attempt that is still recorded in the Google Podcasts [died](https://podcasts.google.com/feed/aHR0cDovL2xpbnV4LmZqZmkuY3Z1dC5jei9-ZG9sZWpzaS9zbGIucnNz?sa=X&ved=0CBQQ27cFahcKEwiAle31lavwAhUAAAAAHQAAAAAQAg) just after 4 episodes, because the source url changed.

Since I do not know whom to ask to fix it (no name shows anywhere), I made my own.
The following link should be accepted by your Podcast player:

[Schlumberger Earnings Call podcast](schlumberger-earnings-conference-calls-podcast.xml)

This article and library were useful in the process:

- <https://blog.lime.link/how-to-self-host-your-podcast/>
- [feedgen](https://feedgen.kiesow.be/) and its [podcast](https://feedgen.kiesow.be/#extensions) extension

## How to run the generation script

In case you want to submit a pull request with a missing episode, or you want to re-use this code, here is how to run it:

1. Install Python 3.7+
2. Clone this repo in GitHub
3. Run `pip install -r requirements.txt
4. Populate the episodes.csv with episodes (and if using for a different podcast feed, change the meta data in `generate.py`)
5. Run `python generate.py` to update the `.xml` file of the feed.
6. Publish the `.xml` file. See [where and how](https://lime.link/blog/where-to-submit-your-podcast/).
7. Enjoy.
