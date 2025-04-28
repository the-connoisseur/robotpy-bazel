load("@robotpy_bazel_pip_deps//:requirements.bzl", "requirement")
load("@rules_python//python:defs.bzl", "py_binary")

py_binary(
    name = "python_version",
    srcs = ["python_version.py"],
    main = "python_version.py",
    # Change this to the version you want to test. See MODULE.bazel for supported versions.
    python_version = "3.13",
)
py_binary(
    name = "format_py",
    srcs = ["format_py.py"],
    main = "format_py.py",
    deps = [
        requirement("black"),
    ],
)
