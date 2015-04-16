import platform
if platform.system() == "Windows":
    import wincertstore
    import atexit
    import ssl

    certfile = wincertstore.CertFile()
    certfile.addstore("CA")
    certfile.addstore("ROOT")
    atexit.register(certfile.close) # cleanup and remove files on shutdown
    def where():
        return certfile
else:
    import ssl
    def where():
        return ssl.get_default_verify_paths().openssl_cafile
