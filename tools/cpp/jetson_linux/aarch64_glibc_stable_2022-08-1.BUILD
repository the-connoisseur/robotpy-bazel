package(default_visibility = ["//visibility:public"])

filegroup(
    name = "gcc",
    srcs = [
        "bin/aarch64-linux-gcc"
    ],
)

filegroup(
    name = "ar",
    srcs = [
        "bin/aarch64-linux-ar"
    ],
)

filegroup(
    name = "as",
    srcs = [
        "bin/aarch64-linux-as"
    ],
)

filegroup(
    name = "cpp",
    srcs = [
        "bin/aarch64-linux-cpp"
    ],
)

filegroup(
    name = "ld",
    srcs = [
        "bin/aarch64-linux-ld"
    ],
)

filegroup(
    name = "nm",
    srcs = [
        "bin/aarch64-linux-nm"
    ],
)

filegroup(
    name = "objcopy",
    srcs = [
        "bin/aarch64-linux-objcopy"
    ],
)

filegroup(
    name = "objdump",
    srcs = [
        "bin/aarch64-linux-objdump"
    ],
)

filegroup(
    name = "strip",
    srcs = [
        "bin/aarch64-linux-strip"
    ],
)

filegroup(
    name = "compiler_pieces",
    srcs = glob([
        "aarch64-buildroot-linux-gnu/**",
        "include/**",
        "lib/gcc/aarch64-buildroot-linux-gnu/**",
        "libexec/gcc/aarch64-buildroot-linux-gnu/**",
    ]),
)

filegroup(
    name = "compiler_components",
    srcs = [
        ":ar",
        ":as",
        ":gcc",
        ":ld",
        ":nm",
        ":objcopy",
        ":objdump",
        ":strip",
    ],
)
