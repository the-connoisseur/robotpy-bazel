load("@rules_python//python/uv:lock.bzl", "lock")

# This generates a universal lock file, which ensures consistent and
# reproducible dependency installations across different platforms, operating
# systems, architectures, and Python versions. It encapsulates all possible
# dependencies across diverse systems.
lock(
    name = "requirements_lock",
    srcs = ["requirements.in"],
    out = "requirements_lock.txt",
    universal = True,
)
