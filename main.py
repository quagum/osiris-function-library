import grpc
from concurrent import futures
from core_management import core_management_pb2
from core_management import core_management_pb2_grpc
from core_management.server import util
from core_management.server.data_store import function_library

class CoreManagementServicer(core_management_pb2_grpc.CoreManagementServicer):
    def AddFunction(self, request, context):
        success, message = util.addFunctionToLibrary(request.function_name, request.code, request.runtime_env, request.version)
        return core_management_pb2.AddFunctionResponse(success=success, message=message)
    
    def ArchiveFunction(self, request, context):
        success, message = util.archiveFunction(request.function_name)
        return core_management_pb2.ArchiveFunctionResponse(success=success, message=message)
    
    def ListFunctions(self, request, context):
        # Call the utility function to get the list of functions
        functions = util.listFunctionsInLibrary()
        function_messages = [
            core_management_pb2.Function(
                name=func["name"],
                code=func["code"],
                runtime_env=func["runtime_env"],
                version=func["version"]
            ) for func in functions
        ]
        return core_management_pb2.ListFunctionsResponse(functions=function_messages)

    def GetFunctionDetails(self, request, context):
        # Call the utility function to get details of a specific function
        func = util.getFunctionDetails(request.function_name)
        if func:
            return core_management_pb2.GetFunctionDetailsResponse(
                function=core_management_pb2.Function(
                    name=func["name"],
                    code=func["code"],
                    runtime_env=func["runtime_env"],
                    version=func["version"]
                )
            )
        else:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("Function not found")
            return core_management_pb2.GetFunctionDetailsResponse()

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    core_management_pb2_grpc.add_CoreManagementServicer_to_server(CoreManagementServicer(), server)
    server.add_insecure_port('[::]:1500')
    server.start()
    print("Server is running on port 1500...")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
