#!/usr/bin/env python3

#
# MIT License
#
# Copyright (c) 2020-2021 EntySec
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#

import os

from hatsploit.utils.fs import FSTools

from hatsploit.core.cli.badges import Badges

from hatsploit.core.session.push.echo import Echo
from hatsploit.core.session.push.printf import Printf


class Push(FSTools):
    badges = Badges()

    push_methods = {
        'echo': Echo(),
        'printf': Printf()
    }

    def push(self, file, sender, args=[], push='printf', location='/tmp', linemax=100):
        if push in self.push_methods:
            if self.exists_file(file):
                with open(file, 'rb') as f:
                    self.badges.print_process(f"Uploading {file}...")
                    self.push_methods[push].push(f.read(), sender, args, location, linemax)

                    self.badges.print_process(f"Saving to {location}...")
                    self.badges.print_success(f"Saved to {location}!")
        else:
            self.badges.print_error("Invalid push method!")
