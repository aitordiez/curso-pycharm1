class AfinacionesException(Exception):
    def __init__(self,mensaje):
        self.mensaje = mensaje