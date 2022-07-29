from app.models import ProductAddRequest, products_pb2_grpc as pb2_grpc, products_pb2 as pb2
import grpc

channel = grpc.insecure_channel('localhost:3009')
stub = pb2_grpc.ProductInfoStub(channel)


def GetProductList():
    empty = pb2.Success(success=True)
    products = stub.GetAllProductsInfo(empty)
    return products.products


def GetProductByID(productID):
    prodid = pb2.ProductID(id=productID)
    product = stub.GetProductInfo(prodid)
    return product


def CreateAddingRequest(productID, productName, productDescription, productImageURL, productReleaseDate, productPrice):
    addProductRequest = ProductAddRequest(productID, productName, productDescription, productImageURL,
                                          productReleaseDate, productPrice)
    addProductRequest.ConvertPB2AndSave()
