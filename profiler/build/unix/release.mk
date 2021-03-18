CFLAGS := -O3 -g0
DEFINES := -DNDEBUG
BUILD := release

include ../../../common/unix-release.mk
include build.mk
