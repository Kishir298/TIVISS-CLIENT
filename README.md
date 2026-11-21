# T.I.V.I.S.S. — client library

**T.I.V.I.S.S.** ("Though I'm Vanquished, I'm Still Stronger") is an
independent AI agent of the **R.I.S.A.R.M.S.** ecosystem. This repository
holds its **client-side library** — the code that runs inside RISARMS-ui and
CORE-CLIENT to talk to the TIVISS host.

| Piece | Repository |
| --- | --- |
| Agent host runtime (identity, memory, permissions, CLI) | `Kishir298/TIVISS-HOST` |
| Client library embedded in desktop/device apps | `Kishir298/TIVISS-CLIENT` (this repository) |

## Status

**v0.1.0 — scaffold.** The repository ships a versioned package, the
`tiviss-client` command (`version`, `doctor`) and CI on Python 3.10–3.14.
It contains **no transport, protocol or security code yet**; those layers are
planned, tracked in RISARMS-DOCS, and will land here as reviewed, tested
commits.

Planned (not implemented):

- device-side transport client shared by RISARMS-ui and CORE-CLIENT
- security-protocol client that talks to the `tiviss-securityd` policy daemon
  published by `Kishir298/TIVISS-HOST`
- offline-capable identity/session handling for desktop embedders

## Install

```bash
python -m pip install -e ".[test]"
```

Requires Python 3.10 or newer. The package has no runtime dependencies.

## Usage

```bash
tiviss-client version
tiviss-client doctor            # environment checks (exit 1 on failure)
tiviss-client doctor --root ..  # also reports a sibling TIVISS-HOST checkout
```

## Development

```bash
ruff check --select E9,F,I tiviss_client tests
python -m pytest -q
```

CI runs the lint gate, the suite and a CLI smoke test on every push to
`main`, `feat/**` and `fix/**`, and on pull requests to `main`.

## License

MIT — see [LICENSE](LICENSE).
