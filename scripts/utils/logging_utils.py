"""Consistent logging helpers for command-line QA-AI scripts."""
from __future__ import annotations

import logging
import sys
from typing import TextIO

_DEFAULT_FORMAT = "%(levelname)s %(name)s: %(message)s"


def get_logger(name: str, *, verbose: bool = False, stream: TextIO | None = None) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG if verbose else logging.INFO)
    logger.propagate = False
    if not logger.handlers:
        handler = logging.StreamHandler(stream or sys.stderr)
        handler.setFormatter(logging.Formatter(_DEFAULT_FORMAT))
        logger.addHandler(handler)
    else:
        for handler in logger.handlers:
            handler.setLevel(logging.DEBUG if verbose else logging.INFO)
    return logger


def configure_root_logging(*, verbose: bool = False) -> None:
    logging.basicConfig(
        level=logging.DEBUG if verbose else logging.INFO,
        format=_DEFAULT_FORMAT,
        stream=sys.stderr,
        force=True,
    )


def log_summary(logger: logging.Logger, *, passed: int, failed: int, warnings: int = 0) -> None:
    logger.info("summary: passed=%d failed=%d warnings=%d", passed, failed, warnings)
