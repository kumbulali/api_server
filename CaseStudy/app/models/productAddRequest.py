import grpc
from app.models import products_pb2_grpc as pb2_grpc, products_pb2 as pb2

channel = grpc.insecure_channel('localhost:3009')
stub = pb2_grpc.ProductInfoStub(channel)


class ProductAddRequest:
    def __init__(self, productID, productName, productDescription, productImageURL, productReleaseDate, productPrice):
        self.productID = productID
        self.productName = productName
        self.productDescription = productDescription
        self.productImageURL = productImageURL
        self.productReleaseDate = productReleaseDate
        self.productPrice = productPrice

    def ConvertPB2AndSave(self):
        pb2Obj = pb2.Product(id=str(self.productID),
                    productName=str(self.productName),
                    productDescription=str(self.productDescription),
                    imageURL=str(self.productImageURL),
                    productReleaseDate=str(self.productReleaseDate),
                    productPrice=float(self.productPrice))
        stub.AddProduct(pb2Obj)

