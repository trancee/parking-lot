#!/usr/bin/env python

import pytest
import sys


if __name__ == '__main__':
    pytest_args = ['-x', '--cov-report', 'html', '--cov', 'app', 'tests/']

    err_no = pytest.main(pytest_args)
    sys.exit(err_no)
