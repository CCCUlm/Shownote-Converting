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

import sys



def parse_shownotes(shownotestream=sys.stdin):

    shownotes = []

    for line in shownotestream:
        line = line.split(' ')
        time = line[0]
        link = line[1]
        description = ''
        for rest in line[2:]:
            description = description + rest + ' '

        shownotes.append((time, link, description.strip()))

    return shownotes




if __name__ == "__main__":
    parse_shownotes(sys.stdin)
