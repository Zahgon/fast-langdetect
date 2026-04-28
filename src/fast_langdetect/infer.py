# -*- coding: utf-8 -*-
"""
FastText based language detection module.
"""
import logging
import os
import platform
import re
import shutil
import tempfile
from pathlib import Path
from typing import Dict, List, Optional, Union, Any, Literal
import fasttext
from robust_downloader import download
logger = logging.getLogger(__name__)
# Use system temporary directory as default cache directory
DEFAULT_CACHE_DIR = Path(tempfile.gettempdir()) / "fasttext-langdetect"
CACHE_DIRECTORY = os.getenv("FTLANG_CACHE", str(DEFAULT_CACHE_DIR))
FASTTEXT_LARGE_MODEL_URL = (
    "https://dl.fbaipublicfiles.com/fasttext/supervised-models/lid.176.bin"
)
FASTTEXT_LARGE_MODEL_NAME = "lid.176.bin"
_LOCAL_SMALL_MODEL_PATH = Path(__file__).parent / "resources" / "lid.176.ftz"
class FastLangdetectError(Exception):
    """Base exception for library-specific failures."""
    pass
class ModelLoadError(FastLangdetectError):
    """Raised when a FastText model fails to load."""
    pass
class ModelDownloader:
    """Model download handler."""
    @staticmethod
    def download(url: str, save_path: Path, proxy: Optional[str] = None) -> None:
        pass
class ModelLoader:
    """Model loading handler."""
    def __init__(self, cache_dir: str = CACHE_DIRECTORY):
        pass
    def _get_model_path(self, model_name: str) -> Path:
        pass
    def load_model(
        self,
        model_name: str = "small",
        download_proxy: Optional[str] = None,
    ) -> fasttext.FastText._FastText:
        pass
class LangDetectConfig:
    """Configuration for language detection."""
    def __init__(
        self,
        model: str = "small",
        cache_dir: str = CACHE_DIRECTORY,
        download_proxy: Optional[str] = None,
    ):
        pass
class LangDetector:
    """Language detection engine."""
    def __init__(self, config: Optional[LangDetectConfig] = None):
        pass
    def _ensure_model(self) -> None:
        pass
    def detect(
        self,
        text: str,
        *,
        k: int = 1,
        threshold: float = 0.0,
        model: Optional[str] = None,
    ) -> List[Dict[str, Any]]:
        pass
_default_detector = LangDetector()
def detect(
    text: str,
    *,
    k: int = 1,
    threshold: float = 0.0,
    model: str = "small",
    low_memory: bool = True,
) -> List[Dict[str, Any]]:
    pass
