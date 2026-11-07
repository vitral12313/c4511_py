import logging

logging.basicConfig(level=logging.DEBUG,
                    filename="logs_p81.log",
                    filemode="w",
                    format="We have logging message: %(asctimes:%(levelname)s - %()message)s"
                    )


try:
    print(10/10)
except Exception:
    logging.exception("Exception")
    