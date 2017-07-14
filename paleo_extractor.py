#!/usr/bin/env python

"""Example extractor based on the clowder code."""

import logging
import subprocess

from pyclowder.extractors import Extractor
import pyclowder.api 
import pyclowder.files
import os


class Paleo(Extractor):
    """This whole file serves as a skeleton for modeling run"""
    def __init__(self):
        Extractor.__init__(self)

        # add any additional arguments to parser
        # self.parser.add_argument('--max', '-m', type=int, nargs='?', default=-1,
        #                          help='maximum number (default=-1)')

        # parse command line and load default logging configuration
        self.setup()

        # setup logging for the exctractor
        logging.getLogger('pyclowder').setLevel(logging.DEBUG)
        logging.getLogger('__main__').setLevel(logging.DEBUG)


    """Tell the clowder not to download the file"""
    def check_message(self, connector, host, secret_key, resource, parameters):
        """The extractor to not download the file."""
        return CheckMessage.bypass

    
    def process_message(self, connector, host, secret_key, resource, parameters):
        # Process the file and upload the results
        logger = logging.getLogger(__name__)
        inputfile = resource["local_paths"][0]
        file_id = resource['id']
        
        clowder_base_url = os.environ.get('CLOWDER_URL', '') 
        logger.debug("clowder base url is " + clowder_base_url)
        # call actual program
        # Assuming inputfile is actually a path
        with open(inputfile) as request_info: 
            data = json.load(request_info)
            #TODO: Need to perform error check
            title = data["title"] 
            logger.debug("Dataset names is " + title)
            result_names = data["outputs"]
        description = "this is a test purpose dataset"

        #TODO: we need some error checkings in here
        uuid = pyclowder.api.create_dataset(clowder_base_url, title, description, secret_key = secret_key)
        logger.debug("the uuid is " + str(uuid))
        

        # For testing purpose


        # store results as metadata
        # result = {
        # }
        #What is important here is the metadata
        # metadata = self.get_metadata(result, 'file', file_id, host)
        # logger.debug(metadata)

        # upload metadata
        # pyclowder.files.upload_metadata(connector, host, secret_key, file_id, metadata)


if __name__ == "__main__":
    extractor = Paleo()
    extractor.start()
