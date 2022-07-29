import grpc
from concurrent import futures
import products_pb2_grpc as pb2_grpc
import products_pb2 as pb2

import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("./venv/serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()


class ProductInfoServicer(pb2_grpc.ProductInfoServicer):
    def GetProductInfo(self, request, context):
        dbData = db.collection('products').document(request.id).get().to_dict()
        response = pb2.Product(id=request.id, imageURL=dbData['imageURL'], productName=dbData['productName'],
                               productDescription=dbData['productDescription'],
                               productReleaseDate=dbData['productReleaseDate'],
                               productPrice=dbData['productPrice'])
        return response

    def GetAllProductsInfo(self, request, context):
        dbData = db.collection('products').get()
        resList = []
        for doc in dbData:
            tempDoc = doc.to_dict()
            resList.append(pb2.Product(id=doc.id, imageURL=tempDoc['imageURL'], productName=tempDoc['productName'],
                                       productDescription=tempDoc['productDescription'],
                                       productReleaseDate=tempDoc['productReleaseDate'],
                                       productPrice=tempDoc['productPrice']))
        response = pb2.Products()
        response.products.extend(resList)
        return response

    def AddProduct(self, request, context):
        docID = request.id
        data = {'imageURL': request.imageURL,
                'productName': request.productName,
                'productDescription': request.productDescription,
                'productReleaseDate': request.productReleaseDate,
                'productPrice': request.productPrice}
        try:
            db.collection('products').document(docID).set(data)
        except:
            return pb2.Success(success=False)
        return pb2.Success(success=True)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_ProductInfoServicer_to_server(ProductInfoServicer(), server)
    print("API Server 3009 numaralı port üzerinden çalışıyor...")
    server.add_insecure_port('[::]:3009')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
