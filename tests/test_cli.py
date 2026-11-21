import pytest

from tiviss_client import __version__
from tiviss_client.cli import main


def test_version_command(capsys):
    assert main(["version"]) == 0
    out = capsys.readouterr().out
    assert out.startswith(f"tiviss-client {__version__} (python ")


def test_doctor_passes_on_supported_python(capsys, tmp_path):
    assert main(["doctor", "--root", str(tmp_path)]) == 0
    out = capsys.readouterr().out
    assert "[ok] python" in out
    assert f"[ok] tiviss_client {__version__}" in out
    assert "[--] TIVISS-HOST sibling checkout not present" in out


def test_doctor_reports_workspace_sibling(capsys, tmp_path):
    (tmp_path / "TIVISS-HOST").mkdir()
    (tmp_path / "TIVISS-HOST" / "pyproject.toml").write_text("[project]\n", encoding="utf-8")
    assert main(["doctor", "--root", str(tmp_path)]) == 0
    assert "[ok] TIVISS-HOST sibling checkout (workspace)" in capsys.readouterr().out


def test_help_exits_zero():
    with pytest.raises(SystemExit) as excinfo:
        main(["--help"])
    assert excinfo.value.code == 0


def test_subcommand_is_required():
    with pytest.raises(SystemExit) as excinfo:
        main([])
    assert excinfo.value.code == 2
