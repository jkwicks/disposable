# Disposable demonstration guidance

This repository is a synthetic standard-library fixture. Issue edits are limited
to demo.py and tests/test_demo.py. Preserve the baseline test and all tests from
prerequisite issues. Do not change tools/check_demo.py or these instructions.

Required verification: `python3 tools/check_demo.py`.
## Worker policy

Use Munsin structured verification requests to run the check through the broker.
Do not claim a check passed without supervisor evidence. Do not install anything,
read secrets, use app network access, or create external resources. No merge,
deployment, force push or direct PR creation by the worker is permitted.
