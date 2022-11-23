import logging as log

log.basicConfig(level=log.DEBUG,
                format='%(asctime)s: %(levelname)s [%(filename)s:%(lineno)s] %(message)s',
                datefmt='%I:%M:%S %p',
                handlers=[
                    log.FileHandler('./Logs/curso_orquesta.log'),
                    log.StreamHandler()
                ])

def debug(*message):
    log.debug(message)