import math
import cloudpassage


class ServerController(object):
    def __init__(self, config):
        session = cloudpassage.HaloSession(config.halo_key,
                                           config.halo_secret,
                                           api_host=config.halo_url)
        self.scan = cloudpassage.Scan(session)

    def run_fim_scan(self,agent_id):
        fim_scan_run = self.scan.initiate_scan(agent_id,'fim')
        return fim_scan_run
