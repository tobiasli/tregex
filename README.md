# tregex
[![Build Status](https://travis-ci.org/tobiasli/tregex.svg?branch=master)](https://travis-ci.org/tobiasli/tregex) [![Coverage Status](https://coveralls.io/repos/github/tobiasli/tregex/badge.svg?branch=master)](https://coveralls.io/github/tobiasli/tregex?branch=master)

tregex is a wrapper around Python regular expressions that makes usage smoother and more user friendly.

* <b>to_dict(pattern, string)</b>: Takes a pattern with named capture groups and returns a dictionary.

* <b>to_object(pattern, string)</b>: Takes a pattern with named capture groups and returns a generic class with named groups as properties (future: DataClass in python 3.7).

If the user has a pattern with named groups, but only wants a simple match, <b>find</b> will only return the matched string. If the user has a pattern with named groups, but only wants group match, <b>group</b> will only return the grouped tuples.

<b>similarity</b>: Takes two strings and returns a score based on how similar the two strings are. Uses difflib.