load("@rules_python//python:defs.bzl", "py_binary")
load("@robotpy_bazel_pip_deps//:requirements.bzl", "requirement")

py_binary(
    name = "robot",
    srcs = ["robot.py"],
    main = "robot.py",
    deps = [
        requirement("wpilib"),
    ],
)
