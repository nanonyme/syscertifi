import platform
if platform.system() == "Windows":
    import wincertstore
    import atexit
    import ssl

    certfile = wincertstore.CertFile()
    atexit.register(certfile.close) # cleanup and remove files on shutdown
    certfile.addstore("CA")
    certfile.addstore("ROOT")
    def where():
        return certfile.name
else:
    import ssl
    def where():
        return ssl.get_default_verify_paths().openssl_cafile
