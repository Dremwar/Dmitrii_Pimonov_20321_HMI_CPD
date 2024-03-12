from concurrent import futures
import logging
import threading

from google.protobuf import any_pb2
#from google.rpc import code_pb2
#from google.rpc import error_details_pb2
#from google.rpc import status_pb2
import grpc
from grpc_status import rpc_status

import helloworld_pb2
import helloworld_pb2_grpc


def create_greet_limit_exceed_error_status(name):
    detail = any_pb2.Any()
    detail.Pack(
        error_details_pb2.QuotaFailure(
            violations=[
                error_details_pb2.QuotaFailure.Violation(
                    subject="name: %s" % name,
                    description="Limit one greeting per person",
                )
            ],
        )
    )
    return status_pb2.Status(
        code=code_pb2.RESOURCE_EXHAUSTED,
        message="Request limit exceeded.",
        details=[detail],
    )


class LimitedGreeter(helloworld_pb2_grpc.GreeterServicer):
    def __init__(self):
        self._lock = threading.RLock()
        self._greeted = set()

    def SayHello(self, request, context):
        with self._lock:
            if request.name in self._greeted:
                rich_status = create_greet_limit_exceed_error_status(
                    request.name
                )
                context.abort_with_status(rpc_status.to_status(rich_status))
            else:
                self._greeted.add(request.name)
        return helloworld_pb2.HelloReply(message="Hello, %s!" % request.name)


def create_server(server_address):
    server = grpc.server(futures.ThreadPoolExecutor())
    helloworld_pb2_grpc.add_GreeterServicer_to_server(LimitedGreeter(), server)
    port = server.add_insecure_port(server_address)
    return server, port


def serve(server):
    server.start()
    server.wait_for_termination()


def main():
    server, unused_port = create_server("[::]:50051")
    serve(server)


if __name__ == "__main__":
    logging.basicConfig()
    main()