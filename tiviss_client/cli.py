"""Command line entry point for the TIVISS client library."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from . import __version__

EXIT_OK = 0
EXIT_FAIL = 1
MINIMUM_PYTHON = (3, 10)


def cmd_version(args: argparse.Namespace) -> int:
    print(f"tiviss-client {__version__} (python {sys.version.split()[0]})")
    return EXIT_OK


def cmd_doctor(args: argparse.Namespace) -> int:
    ok = True
    current = sys.version_info[:2]
    supported = current >= MINIMUM_PYTHON
    minimum = f"{MINIMUM_PYTHON[0]}.{MINIMUM_PYTHON[1]}"
    print(f"[{'ok' if supported else 'FAIL'}] python {current[0]}.{current[1]} (need {minimum})")
    ok = ok and supported
    print(f"[ok] tiviss_client {__version__}")
    root = Path(args.root)
    host = root / "TIVISS-HOST" / "pyproject.toml"
    if host.is_file():
        print("[ok] TIVISS-HOST sibling checkout (workspace)")
    else:
        print("[--] TIVISS-HOST sibling checkout not present")
    return EXIT_OK if ok else EXIT_FAIL


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="tiviss-client",
        description="T.I.V.I.S.S. client library command line.",
    )
    parser.add_argument(
        "--version", action="version", version=f"%(prog)s {__version__}"
    )
    sub = parser.add_subparsers(dest="command", required=True)

    version = sub.add_parser("version", help="Show the client library version")
    version.set_defaults(func=cmd_version)

    doctor = sub.add_parser("doctor", help="Check the local client environment")
    doctor.add_argument(
        "--root", default=".", help="Workspace root used to find TIVISS-HOST"
    )
    doctor.set_defaults(func=cmd_doctor)

    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
