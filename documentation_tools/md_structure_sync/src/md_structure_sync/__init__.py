"""Markdown structure synchronization tool."""

from md_structure_sync.models import Config, SyncResult
from md_structure_sync.sync import sync_file, sync_directory

__all__ = ["sync_file", "sync_directory", "Config", "SyncResult"]
__version__ = "0.1.0"
