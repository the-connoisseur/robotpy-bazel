load("@com_github_mvukov_rules_ros2//ros2:launch.bzl", "ros2_launch")
load("@com_github_mvukov_rules_ros2//ros2:test.bzl", "ros2_test")
load("@robotpy_bazel_pip_deps//:requirements.bzl", "requirement")
load("@rules_pkg//:pkg.bzl", "pkg_tar")
load("@rules_python//python:defs.bzl", "py_binary")

cc_binary(
    name = "hello_world",
    srcs = ["hello_world.cc"],
)

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

py_binary(
    name = "talker",
    srcs = ["talker.py"],
    python_version = "3.11",
    deps = [
        "@ros2_common_interfaces//:py_std_msgs",
        "@ros2_rclpy//:rclpy",
    ],
)

py_binary(
    name = "listener",
    srcs = ["listener.py"],
    python_version = "3.11",
    deps = [
        "@ros2_common_interfaces//:py_std_msgs",
        "@ros2_rclpy//:rclpy",
    ],
)

ros2_launch(
    name = "chatter",
    launch_file = "chatter.launch.py",
    nodes = [
        ":talker",
        ":listener",
    ],
)

ros2_test(
    name = "talker_test",
    size = "small",
    launch_file = "talker_test.py",
    nodes = [
        ":talker",
    ],
    deps = [
        "@ros2_common_interfaces//:py_std_msgs"
    ],
)
