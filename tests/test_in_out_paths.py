import pathlib
from pathio import IOPaths

CONTENT = "content"


def test_create_file(tmp_path):
    """
    This tests that the tmp path operations work on the current system.
    """
    d = tmp_path / "sub"
    d.mkdir()
    p = d / "hello.txt"
    p.write_text(CONTENT)
    assert p.read_text() == CONTENT
    assert len(list(tmp_path.iterdir())) == 1


def test_in_out_paths_works(tmp_path):
    in_dir = tmp_path / "in"
    out_dir = tmp_path / "out"
    in_dir.mkdir()

    txt_file_path = in_dir / "x.txt"
    txt_file_path.write_text(CONTENT)
    assert txt_file_path.read_text() == CONTENT

    in_files = {
        "txt_file": txt_file_path,
        "stream": "-",
    }
    in_dirs = {
        "input_dir": str(in_dir),
    }
    out_dirs = {
        "out_dir": out_dir,
    }
    out_files = {
        "new_txt_file": out_dir / "new.txt",
        "new_txt_file_2": str(out_dir / "new_2.txt"),
    }

    # Create paths container with checks

    paths = IOPaths(
        in_files=in_files,
        in_dirs=in_dirs,
        out_files=out_files,
        out_dirs=out_dirs,
    )

    print(paths)

    # Create output directory
    paths.mk_output_dirs(collection="out_dirs")
    assert out_dir.is_dir()

    assert paths["txt_file"] == pathlib.Path(in_files["txt_file"])
    assert paths["stream"] == "-"
    assert paths["input_dir"] == pathlib.Path(in_dirs["input_dir"])
    assert paths["out_dir"] == pathlib.Path(out_dirs["out_dir"])
    assert paths["new_txt_file"] == pathlib.Path(out_files["new_txt_file"])
    assert paths["new_txt_file_2"] == pathlib.Path(out_files["new_txt_file_2"])


def test_io_paths_creates_out_files_dirs(tmp_path):
    out_dir = tmp_path / "out"

    out_dirs = {
        "out_dir": out_dir,
    }
    out_files = {
        "new_txt_file": out_dir / "subsub" / "new.txt",
        "new_txt_file_2": str(out_dir / "subsub2" / "new_2.txt"),
    }

    # Create paths container with checks

    paths = IOPaths(out_files=out_files, out_dirs=out_dirs)

    print(paths)

    # Create output directory
    paths.mk_output_dirs(collection="out_files")
    assert out_dir.is_dir()
    assert (out_dir / "subsub").is_dir()
    assert (out_dir / "subsub2").is_dir()


def test_io_paths_empty(tmp_path):
    paths = IOPaths()
    paths.set_path("out_dir", tmp_path / "out", "out_dirs")


def test_in_out_paths_fails(tmp_path):
    # TODO Test all the cases where it should raise an error

    # TODO Test duplicates are found correctly
    pass
