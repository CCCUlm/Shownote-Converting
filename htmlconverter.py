#!/usr/bin/python3

# Copyright (c) 2011 Matthias Matousek <m@tou.io>
# 
# Permission to use, copy, modify, and distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
# 
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
# ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
# OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.

from shownoteparser import parse_shownotes

s = parse_shownotes()

print('<ul>')
for note in s:
    if note[1] == '??':
        print('<li>' 
                + note[0] + ' '
                + note[1] + ' '
                + note[2] 
                + '</li>')
    else:
        print('<li>' 
                + note[0] 
                + ' <a href="' 
                + note[1] 
                + '">' 
                + note[2] 
                + '</a></li>')
print('</ul>')
