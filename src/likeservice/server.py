from concurrent import futures
import grpc
from grpc_reflection.v1alpha import reflection
from protos import likeservice_pb2
from protos import likeservice_pb2_grpc

# In-memory data store for likes
likes_data = {}
session_likes = {}

class LikesService(likeservice_pb2_grpc.LikesServiceServicer):
    def GetLikes(self, request, context):
        product_id = request.product_id
        likes = likes_data.get(product_id, 0)
        return likeservice_pb2.GetLikesResponse(likes_count=likes)

    def AddLike(self, request, context):
        product_id = request.product_id
        session_id = request.session_id  # Pass session_id in the request

        if session_id in session_likes and product_id in session_likes[session_id]:
            return likeservice_pb2.AddLikeResponse(success=False, message="Already liked")

        if product_id in likes_data:
            likes_data[product_id] += 1
        else:
            likes_data[product_id] = 1

        # Track the like for the session
        if session_id not in session_likes:
            session_likes[session_id] = set()
        session_likes[session_id].add(product_id)

        return likeservice_pb2.AddLikeResponse(success=True)
    
    def HasLiked(self, request, context):
        product_id = request.product_id
        session_id = request.session_id

        # Check if the session has liked the product
        if session_id in session_likes and product_id in session_likes[session_id]:
            return likeservice_pb2.HasLikedResponse(liked=True)
        return likeservice_pb2.HasLikedResponse(liked=False)



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
