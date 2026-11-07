import asyncio
import logging

from controller.config import settings


async def main() -> None:
    logging.basicConfig(
        level=settings.log_level,
        format="%(asctime)s %(levelname)s %(name)s %(message)s",
    )

    logger = logging.getLogger(__name__)
    logger.info("Starting %s", settings.app_name)
    logger.info("Environment: %s", settings.environment)

    # The controller lifecycle will be implemented in later phases.
    logger.info("Foundation initialized successfully.")


if __name__ == "__main__":
    asyncio.run(main())
