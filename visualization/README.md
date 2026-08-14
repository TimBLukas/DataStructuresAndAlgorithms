Data Structures Visualization (C/OpenGL)

A minimal C-based visualization app that uses GLFW + GLAD for rendering data structures (linked lists, trees, graphs).

Quick build (Linux, deps: cmake, build-essential, libgl1-mesa-dev)

1. From the visualization/ directory:

   mkdir -p build && cd build
   cmake ..
   make -j

2. Run:

   ./app

Notes
- The repository bundles a copy of GLFW under libs/glfw-3.4; if your system already provides GLFW development files the linker may pick those instead.
- If build fails due to missing OpenGL headers, install your platform's OpenGL dev packages (e.g., libgl1-mesa-dev on Debian/Ubuntu).
- The CMakeLists.txt now collects all src/*.c files and exposes src/ include paths.

Development
- Implement src/math/vec3.c utilities first, then adapters under src/structures to populate a central VizGraph representation.
- Use the plan.md in this directory for a phased roadmap.

License: See repository root for license information.
