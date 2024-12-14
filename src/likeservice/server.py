from concurrent import futures
import grpc
from grpc_reflection.v1alpha import reflection
import likeservice_pb2
import likeservice_pb2_grpc

# In-memory data store for likes
likes_data = {}

class LikesService(likeservice_pb2_grpc.LikesServiceServicer):
    def GetLikes(self, request, context):
        product_id = request.product_id
        likes = likes_data.get(product_id, 0)
        return likeservice_pb2.GetLikesResponse(likes_count=likes)

    def AddLike(self, request, context):
        product_id = request.product_id
        if product_id in likes_data:
            likes_data[product_id] += 1
        else:
            likes_data[product_id] = 1
        return likeservice_pb2.AddLikeResponse(success=True)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    likeservice_pb2_grpc.add_LikesServiceServicer_to_server(LikesService(), server)

    # Enable reflection
    SERVICE_NAMES = (
        likeservice_pb2.DESCRIPTOR.services_by_name['LikesService'].full_name,
        reflection.SERVICE_NAME,
    )
    reflection.enable_server_reflection(SERVICE_NAMES, server)

    server.add_insecure_port("[::]:8080")
    print("Likeservice is running on port 8080 with reflection enabled...")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
