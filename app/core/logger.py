import logging
import json


class JsonFormatter(
    logging.Formatter
):

    def format(
        self,
        record,
    ):

        return json.dumps(
            {
                "level": record.levelname,
                "message": record.getMessage(),
            }
        )


logger = logging.getLogger(
    "pygate"
)

logger.setLevel(
    logging.INFO
)

handler = logging.StreamHandler()

handler.setFormatter(
    JsonFormatter()
)

logger.addHandler(
    handler
)
