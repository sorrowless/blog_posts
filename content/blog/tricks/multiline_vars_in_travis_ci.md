Title: How to set multiline variable in Travis CI UI
Date: 2020-09-06 14:51
Authors: sbog
Slug: multiline_vars_travis
Tags: travis, ci, variables, tricks
Lang: en

Sometimes there is a need to set multiline Travis CI variable. Example is
private SSH key to access target host from CI. Easy way to do so is:

* first, swap all line carriers with '\n' symbols.
* second, enclose whole line into $'<data here>' symbols

Result will looks like `$'-----BEGIN CERTIFICATE-----\nNKOQ1z...\n-----END CERTIFICATE-----'`,
which gives you proper formatting when you read that variable in CI session.
