import grpc
from concurrent import futures
import core_management_pb2
import core_management_pb2_grpc
import util
# Placeholder database
function_library = {}

class CoreManagementServicer(core_management_pb2_grpc.CoreManagementServicer):
    def AddFunction(self, request, context):
        success, message = util.addFunctionToLibrary(request.function_name, request.code, request.runtime_env, request.version)
        return core_management_pb2.AddFunctionResponse(success=success, message=message)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    core_management_pb2_grpc.add_CoreManagementServicer_to_server(CoreManagementServicer(), server)
    server.add_insecure_port('[::]:1500')
    server.start()
    print("Server is running on port 1500...")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
