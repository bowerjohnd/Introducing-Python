from jsonrpcserver import method, serve, Success

@method
def double(num) :
    return Success(num * 2)     # book version is deprecated, newer jsonrpcserver/client requires return wrapped in Success object

if __name__ == "__main__" :
    serve()