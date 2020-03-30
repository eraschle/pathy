import pytest
from pathlib import Path
import tempfile
import shutil
from gcspath import use_fs


@pytest.fixture()
def with_fs():
    tmp_dir = tempfile.mkdtemp()
    yield Path(tmp_dir)
    shutil.rmtree(tmp_dir)
    # Turn off FS adapter
    use_fs(False)