load("@rules_python//python:defs.bzl", "py_binary")
load("@pip//:requirements.bzl", "requirement")

py_binary(
    name = "robot",
    srcs = ["robot.py"],
    main = "robot.py",
    deps = [
        requirement("wpilib"),
    ],
)
