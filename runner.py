#!/usr/bin/env python
# -*- coding: utf-8 -*-
import lib

class FIM_scan():
    def __init__(self):
        self.output = []
        config = lib.ConfigHelper()
        self.fimscanner = lib.ServerController(config)
        self.read = lib.FileController()
        self.count = 0

    def run(self):
        self.agents = self.read.load_file()
        for agent in self.agents:
            self.scan = self.fimscanner.run_fim_scan(agent)
            self.output.append(self.scan)

#        print(self.output)

def main():
    run_fim_scan = FIM_scan()
    run_fim_scan.run()

if __name__ == "__main__":
    main()
