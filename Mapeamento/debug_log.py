import logging

# Configuração inicial do logger
logger = logging.getLogger("meu_logger")  # Nome personalizado para o logger
logger.setLevel(logging.DEBUG)

# Formato e handler
handler = logging.StreamHandler()
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
handler.setFormatter(formatter)
logger.addHandler(handler)

DEBUG_MODE = True

def debug(*args):
    """
    Macro para exibir mensagens de debug quando o modo de depuração está ativo.
    """
    if DEBUG_MODE:
        logger.debug(" ".join(map(str, args)))
