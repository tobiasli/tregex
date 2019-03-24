"""tregex is a package for handling regular expressions and other string-related tasks more smoothly.

>>> import tregex as tr
>>>
>>> t = tr.to_tuple(pattern='([^;]+?)@(.+?)\.([^;]+)', string='john.smith@somewhere.co.uk; hackzor@coolface.com')
>>> assert t[0][1] == 'somewhere'
>>> assert t[1][2] == 'com'
>>>
>>> pattern = '(?P<name>[^;]+?)@(?P<address>.+?)\.(?P<domain>[^;]+)'
>>> t = tr.to_dict(pattern=pattern, string='john.smith@somewhere.co.uk; hackzor@coolface.com')
>>> assert t[0]['name'] == 'john.smith'
>>> assert t[1]['address'] == 'coolface'
>>>
>>> t = tr.to_object(pattern=pattern, string='john.smith@somewhere.co.uk; hackzor@coolface.com')
>>> assert t[0].name == 'john.smith'
>>> assert t[1].address == 'coolface'
"""
from tregex.tregex import TregexCompiled
from tregex.tregex import to_tuple, to_dict, to_object
from tregex.tregex import similarity, find, find_best, find_scores

__all__ = ['TregexCompiled', 'to_tuple', 'to_dict', 'to_object', 'similarity', 'find', 'find_best', 'find_scores']
