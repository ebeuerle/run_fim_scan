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
        sys.tracebacklimit = 0

    def run(self):
        self.agents = self.read.load_file()
        for agent in self.agents:
            print "FIM scan run attempt on server: %s" % agent
            self.scan = self.fimscanner.run_fim_scan(agent)

def main():
    sys.stdout = lib.Logger(logging.info)
    sys.stderr = lib.Logger(logging.warning)
    run_fim_scan = FIM_scan()
    run_fim_scan.run()

if __name__ == "__main__":
    main()
