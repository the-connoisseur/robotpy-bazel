load("@rules_pkg//:pkg.bzl", "pkg_tar")
load("@rules_python//python:defs.bzl", "py_binary")
load("@robotpy_bazel_pip_deps//:requirements.bzl", "requirement")

py_binary(
    name = "multi_platform_support_test",
    srcs = ["multi_platform_support_test.py"],
    main = "multi_platform_support_test.py",
    deps = [
      requirement("cryptography"),
    ],
)

pkg_tar(
    name = "multi_platform_support_test_tar",
    srcs = [":multi_platform_support_test"],
    include_runfiles = True,
    extension = "tar.gz",
)
