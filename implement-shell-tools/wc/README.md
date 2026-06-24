# Implement `wc`

You should already be familiar with the `wc` command line tool.

Your task is to implement your own version of `wc`.

It must act the same as `wc` would, if run from the directory containing this README.md file, for the following command lines:

* `wc sample-files/*`
* `wc -l sample-files/3.txt`
* `wc -w sample-files/3.txt`
* `wc -c sample-files/3.txt`
* `wc -l sample-files/*`
* `wc -w -l sample-files/3.txt`
* `wc -w -l sample-files/*`

Matching any additional behaviours or flags are optional stretch goals.

We recommend you start off supporting no flags for one file, then add support for multiple files, then add support for the flags.
