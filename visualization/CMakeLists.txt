cmake_minimum_required(VERSION 3.16)

project(DataVisualizer C)

set(CMAKE_C_STANDARD 11)
set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -Wall -Wextra -Wpedantic")

# Collect all C sources under src/
file(GLOB_RECURSE SRC_FILES CONFIGURE_DEPENDS "${CMAKE_SOURCE_DIR}/src/*.c")

add_executable(app ${SRC_FILES})

# Include directories for project headers and external deps
target_include_directories(app PRIVATE
    ${CMAKE_SOURCE_DIR}/src
    ${CMAKE_SOURCE_DIR}/src/math
    ${CMAKE_SOURCE_DIR}/src/renderer
    ${CMAKE_SOURCE_DIR}/src/structures
    ${CMAKE_SOURCE_DIR}/src/visualization
    ${CMAKE_SOURCE_DIR}/external/glad
    ${CMAKE_SOURCE_DIR}/libs/glfw-3.4/include
)

# Prefer linking against bundled glfw build if present
if(EXISTS "${CMAKE_SOURCE_DIR}/libs/glfw-3.4/build/src")
    target_link_directories(app PRIVATE ${CMAKE_SOURCE_DIR}/libs/glfw-3.4/build/src)
endif()

# Link libraries (platform: Linux). Adjust if building on other platforms.
target_link_libraries(app
    glfw3
    GL
    dl
    pthread
    m
)

# Installation and build options
option(BUILD_EXAMPLES "Build example app" ON)
if(BUILD_EXAMPLES)
    add_custom_target(run
        COMMAND ${CMAKE_COMMAND} --build ${CMAKE_BINARY_DIR} --target app
        COMMAND $<TARGET_FILE:app>
        DEPENDS app
        WORKING_DIRECTORY ${CMAKE_BINARY_DIR}
    )
endif()
