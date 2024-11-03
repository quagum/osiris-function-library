import grpc
import pytest
import time
from concurrent import futures
import threading
import core_management_pb2_grpc
import core_management_pb2
from server.server import CoreManagementServicer  # Ensure correct import

#runs server in a thread
def run_server(stop_event):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    core_management_pb2_grpc.add_CoreManagementServicer_to_server(CoreManagementServicer(), server)
    server.add_insecure_port('[::]:1500')
    server.start()

    try:
        while not stop_event.is_set():
            time.sleep(1)
    finally:
        server.stop(0)

@pytest.fixture(scope='module', autouse=True)
def grpc_server():
    stop_event = threading.Event()
    server_thread = threading.Thread(target=run_server, args=(stop_event,))
    server_thread.start()

    # Wait a moment for the server to start
    time.sleep(1)

    yield  # Run the tests

    # Cleanup: stop the server
    stop_event.set()  # Signal the server to stop
    server_thread.join()  # Wait for the server thread to finish

@pytest.fixture
def grpc_channel():
    # Create a gRPC channel
    channel = grpc.insecure_channel('localhost:1500')
    yield channel
    channel.close()


'''UNIT TESTS BELOW'''

def test_add_function(grpc_channel):
    stub = core_management_pb2_grpc.CoreManagementStub(grpc_channel)

    request = core_management_pb2.AddFunctionRequest(
        function_name="test_function",
        code="def test(): pass",
        runtime_env="python3.9",
        version="1.0"
    )

    response = stub.AddFunction(request)

    assert response.success is True

