#!/usr/bin/env python

"""Example extractor based on the clowder code.""" 
import logging 
import subprocess
import json
import random
import subprocess
import stat

from pyclowder.extractors import Extractor
import pyclowder.datasets 
import pyclowder.files
import pyclowder.clowder 
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

        #Using the clowder module to directly interact with clowder
        self.clowder = pyclowder.clowder.Clowder()
        
        
    """Tell the clowder not to download the file"""
    # def check_message(self, connector, host, secret_key, resource, parameters):
        # """The extractor to not download the file."""
        # return CheckMessage.bypass

    
    def process_message(self, connector, host, secret_key, resource, parameters):

        #Get info from JSON model run request file
        logger = logging.getLogger(__name__)
        inputfile = resource["local_paths"][0]
        file_id = resource['id']

        with open(inputfile) as request_info: 
            data = json.load(request_info)
            #TODO: Need to perform error check
            title = data["title"] 
            logger.debug("Dataset names is " + title)
            result_names = data["outputs"]

        #TODO: Error checking for already existed file 
        #Get the direcory addres from the JOBDIR environmental variable
        #Create the model run job directory on the disk also in the clowder
        description = "this is a test purpose dataset"
        uuid = self.clowder.create_dataset(title, description)
	uuid = uuid['id']
        result_dir = os.environ.get("JOBDIR") + "/" + str(uuid)
        if not os.path.isdir(result_dir):
            os.makedirs(result_dir)
        #Call the actual model run program and put results into job dir
        for result_file_name in result_names:
            result_file_path = result_dir + "/" + result_file_name
            logger.debug("Newly created file has path " + result_file_path)
            with open(result_file_path, 'w+') as f:
                for i in range(100):
                    f.write(str(random.random()))
        #Put module results to the clowder 
        for result_file_name in result_names:
            result_file_path = result_dir + "/" + result_file_name
            self.clowder.add_file(title, result_file_path)

        #TODO:Store the results' metadata and push to clowder 
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
