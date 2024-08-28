import logging

def setup_logger(nombre='biblioteca_logger', archivo='biblioteca.log'):
    logger = logging.getLogger(nombre)
    logger.setLevel(logging.INFO)

    # Crear un handler para escribir en un archivo
    fh = logging.FileHandler(archivo)
    fh.setLevel(logging.INFO)

    # Crear un handler para la consola
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)

    # Crear formato para los logs
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)

    # Agregar handlers al logger
    logger.addHandler(fh)
    logger.addHandler(ch)

    return logger
