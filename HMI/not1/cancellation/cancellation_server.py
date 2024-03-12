from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import argparse
from concurrent import futures
import logging
import threading

import grpc
import re

import hash_name_pb2
import hash_name_pb2_grpc

_LOGGER = logging.getLogger(__name__)
_SERVER_HOST = "localhost"

_DESCRIPTION = "A server for finding hashes similar to names."


class HashFinder(hash_name_pb2_grpc.HashFinderServicer):
    def __init__(self, maximum_hashes):
        super(HashFinder, self).__init__()
        self._maximum_hashes = maximum_hashes

    def Find(self, request, context):
        stop_event = threading.Event()

        def on_rpc_done():
            _LOGGER.debug("Attempting to regain servicer thread.")
            stop_event.set()

        context.add_callback(on_rpc_done)
        candidates = []
        try:
            candidates = list(search.search(request.desired_name,request.ideal_hamming_distance,stop_event,self._maximum_hashes,))
        except search.ResourceLimitExceededError:
            _LOGGER.info("Cancelling RPC due to exhausted resources.")
            context.cancel()
        _LOGGER.debug("Servicer thread returning.")
        if not candidates:
            return hash_name_pb2.HashNameResponse()
        return candidates[-1]

    def FindRange(self, request, context):
        stop_event = threading.Event()

        def on_rpc_done():
            _LOGGER.debug("Attempting to regain servicer thread.")
            stop_event.set()

        context.add_callback(on_rpc_done)
        secret_generator = search.search(
            request.desired_name,
            request.ideal_hamming_distance,
            stop_event,
            self._maximum_hashes,interesting_hamming_distance=request.interesting_hamming_distance,)
        try:
            for candidate in secret_generator:
                yield candidate
        except search.ResourceLimitExceededError:
            _LOGGER.info("Cancelling RPC due to exhausted resources.")
            context.cancel()
        _LOGGER.debug("Regained servicer thread.")


def _running_server(port, maximum_hashes):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=1), maximum_concurrent_rpcs=1)
    hash_name_pb2_grpc.add_HashFinderServicer_to_server(HashFinder(maximum_hashes), server)
    address = "{}:{}".format(_SERVER_HOST, port)
    actual_port = server.add_insecure_port(address)
    server.start()
    print("Server listening at '{}'".format(address))
    return server


def main():
    parser = argparse.ArgumentParser(description=_DESCRIPTION)
    parser.add_argument(
        "--port",
        type=int,
        default=50051,
        nargs="?",
        help="The port on which the server will listen.")
    parser.add_argument(
        "--maximum-hashes",
        type=int,
        default=1000000,
        nargs="?",
        help="The maximum number of hashes to search before cancelling.")
    args = parser.parse_args()
    server = _running_server(args.port, args.maximum_hashes)
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig()
    main()