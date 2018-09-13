#!/usr/bin/env python
# -*- coding: utf-8 -*-
import lib
import logging
import sys

class FIM_scan():
    def __init__(self):
        config = lib.ConfigHelper()
        self.fimscanner = lib.ServerController(config)
        self.read = lib.FileController()
        self.count = 0

    def run(self):
        self.agents = self.read.load_file()
        for agent in self.agents:
            self.scan = self.fimscanner.run_fim_scan(agent)
            print "FIM scan run on server: %s" % agent

def main():
    sys.stdout = lib.Logger(logging.info)
    sys.stderr = lib.Logger(logging.warning)
    run_fim_scan = FIM_scan()
    run_fim_scan.run()

if __name__ == "__main__":
    main()
