cmake_minimum_required(VERSION 3.16)

project(DataVisualizer C)

set(CMAKE_C_STANDARD 11)

add_executable(app
    src/main.c
    external/glad/glad.c
)

target_include_directories(app PRIVATE
    external/glad
    libs/glfw-3.4/include
)

target_link_directories(app PRIVATE
    libs/glfw-3.4/build/src
)

target_link_libraries(app
    glfw3
    GL
    dl
    pthread
    m
)
