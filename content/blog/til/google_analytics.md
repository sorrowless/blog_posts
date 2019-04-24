Title: Google Analytics.
Date: 2019-04-24 17:59
Authors: sbog
Slug: google_analytics
Tags: til, analytics
Lang: en

## Google analytics in Pelican

Today I learn how GA works with Pelican. That's actually pretty easy - one just
need to register on [Google Analytics website][1] and get an unique identifier
which will look like `XX-XXXXXXXXXX-X` and put it into Pelican's `publishconf.py`.
That's it, just run

```
> pelican content -s publishconf.py
```

and you're done - all new pages will have GA identifier in it and you'll be able
to look at the visitors count in your GA account.

[1]: https://analytics.google.com
