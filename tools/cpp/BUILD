package(default_visibility = ["//visibility:public"])

load(":cc_toolchain_config.bzl", "cc_toolchain_config")

filegroup(name = "empty")

filegroup(
    name = "all_files",
    srcs = [
        "//tools/cpp/jetson_linux:tool_wrappers",
        "@aarch64_glibc_stable_2022-08-1//:compiler_pieces",
    ],
)

filegroup(
    name = "ar_files",
    srcs = [
        "//tools/cpp/jetson_linux:ar",
        "@aarch64_glibc_stable_2022-08-1//:compiler_pieces",
    ],
)

filegroup(
    name = "compiler_files",
    srcs = [
        "//tools/cpp/jetson_linux:as",
        "//tools/cpp/jetson_linux:gcc",
        "//tools/cpp/jetson_linux:ld",
        "@aarch64_glibc_stable_2022-08-1//:compiler_pieces",
    ],
)

filegroup(
    name = "linker_files",
    srcs = [
        "//tools/cpp/jetson_linux:ar",
        "//tools/cpp/jetson_linux:gcc",
        "//tools/cpp/jetson_linux:ld",
        "@aarch64_glibc_stable_2022-08-1//:compiler_pieces",
    ],
)

cc_toolchain_config(name = "jetson_linux_toolchain_config")

cc_toolchain(
    name = "jetson_linux_toolchain",
    toolchain_identifier = "linux_aarch64-toolchain",
    toolchain_config = ":jetson_linux_toolchain_config",
    all_files = ":all_files",
    ar_files = ":ar_files",
    as_files = ":compiler_files",
    compiler_files = ":compiler_files",
    linker_files = ":linker_files",
    dwp_files = ":empty",
    objcopy_files = "//tools/cpp/jetson_linux:objcopy",
    strip_files = "//tools/cpp/jetson_linux:strip",
    supports_param_files = 0,
)

toolchain(
    name = "cc_toolchain_for_jetson_linux",
    toolchain = ":jetson_linux_toolchain",
    toolchain_type = "@bazel_tools//tools/cpp:toolchain_type",
    exec_compatible_with = [
        "@platforms//cpu:x86_64",
        "@platforms//os:linux",
    ],
    target_compatible_with = [
        "@platforms//cpu:aarch64",
        "@platforms//os:linux",
    ],
)
