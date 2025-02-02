#!/usr/bin/env python3

#
# MIT License
#
# Copyright (c) 2020-2022 EntySec
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
import datetime

from hatsploit.core.cli.badges import Badges
from hatsploit.lib.config import Config


class Loot:
    badges = Badges()

    loot = Config().path_config['loot_path']

    def create_loot(self):
        self.badges.print_process(f"Creating loot at {self.loot}...")

        if not os.path.isdir(self.loot):
            os.mkdir(self.loot)

    def remove_loot(self, filename):
        if os.path.exists(self.loot + filename):
            self.badges.print_process(f"Removing loot {self.loot}{filename}...")
            os.remove(self.loot + filename)
            self.badges.print_success("Loot successfully removed!")
        else:
            self.badges.print_error("Invalid loot given!")

    def list_loot(self):
        loots = []

        for loot in os.listdir(self.loot):
            loots.append((loot, self.loot + loot, datetime.datetime.fromtimestamp(
                os.path.getmtime(
                    self.loot + loot
                )).astimezone().strftime("%Y-%m-%d %H:%M:%S %Z")
            ))

        return loots
