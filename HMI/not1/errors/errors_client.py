from __future__ import print_function

import logging

from google.rpc import error_details_pb2
import grpc
from grpc_status import rpc_status

from examples.protos import helloworld_pb2
from examples.protos import helloworld_pb2_grpc

_LOGGER = logging.getLogger(__name__)


def process(stub):
    try:
        response = stub.SayHello(helloworld_pb2.HelloRequest(name="Alice"))
        _LOGGER.info("Call success: %s", response.message)
    except grpc.RpcError as rpc_error:
        _LOGGER.error("Call failure: %s", rpc_error)
        status = rpc_status.from_call(rpc_error)
        for detail in status.details:
            if detail.Is(error_details_pb2.QuotaFailure.DESCRIPTOR):
                info = error_details_pb2.QuotaFailure()
                detail.Unpack(info)
                _LOGGER.error("Quota failure: %s", info)
            else:
                raise RuntimeError("Unexpected failure: %s" % detail)


def main():
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = helloworld_pb2_grpc.GreeterStub(channel)
        process(stub)


if __name__ == "__main__":
    logging.basicConfig()
    main()