load("@bazel_tools//tools/cpp:cc_toolchain_config_lib.bzl", "tool_path")

def _impl(ctx):
    tool_paths = [
        tool_path(
            name = "gcc",
            path = "aarch64_glibc_stable_2022-08-1_gcc",
        ),
        tool_path(
            name = "ld",
            path = "aarch64_glibc_stable_2022-08-1_ld",
        ),
        tool_path(
            name = "ar",
            path = "aarch64_glibc_stable_2022-08-1_ar",
        ),
        tool_path(
            name = "as",
            path = "aarch64_glibc_stable_2022-08-1_as",
        ),
        tool_path(
            name = "cpp",
            path = "aarch64_glibc_stable_2022-08-1_cpp",
        ),
        tool_path(
            name = "nm",
            path = "aarch64_glibc_stable_2022-08-1_nm",
        ),
        tool_path(
            name = "objcopy",
            path = "aarch64_glibc_stable_2022-08-1_objcopy",
        ),
        tool_path(
            name = "objdump",
            path = "aarch64_glibc_stable_2022-08-1_objdump",
        ),
        tool_path(
            name = "strip",
            path = "aarch64_glibc_stable_2022-08-1_strip",
        ),
    ]

    return cc_common.create_cc_toolchain_config_info(
        ctx = ctx,
        cxx_builtin_include_directories = [
            "%package(@aarch64_glibc_stable_2022-08-1//aarch64-buildroot-linux-gnu/include/c++)%",
            "%package(@aarch64_glibc_stable_2022-08-1//aarch64-buildroot-linux-gnu/sysroot/usr/include)%",
        ],
        toolchain_identifier = "aarch64-linux-toolchain",
        host_system_name = "local",
        target_system_name = "orin",
        target_cpu = "aarch64",
        target_libc = "unknown",
        compiler = "gcc",
        abi_version = "unknown",
        abi_libc_version = "unknown",
        tool_paths = tool_paths,
    )

cc_toolchain_config = rule(
    implementation = _impl,
    attrs = {},
    provides = [CcToolchainConfigInfo],
)
