# Implementation plan

## Phase 0 — Foundations

> Starting Blocks

1. Write a small vec3 math module (add, sub, scale, length, normalize, random jitter). Everything downstream depends on this. Ensure this is expandavle if necessary!

2. Define the VizGraph data contract — a generic representation of "nodes with positions/velocities" and "edges between node IDs," decoupled from any specific data structure. This is the single interface every other subsystem will talk to.

3. Decide now: when a data structure changes (insert/delete), do you rebuild the whole VizGraph from scratch, or update it incrementally? This decision shapes the adapter and physics code you write later, so settle it before building further.

## Phase 1 — First adapter (no graphics yet)

1. Pick the simplest structure (linked list) and write the extraction function: walk the real structure, populate a VizGraph.

2. Verify by printing node count/positions to stdout — no rendering needed yet. This proves the adapter layer works in isolation.

## Phase 2 — Physics/layout

1. Implement the force-directed simulation step: repulsion between all node pairs, spring attraction along edges, a weak centering force, and velocity damping.

2. Integrate positions each frame (simple Euler is fine to start).

3. Test again via stdout: run the simulation for N steps on the linked-list VizGraph and confirm nodes spread out and settle rather than exploding or freezing. Tune force constants here before touching graphics — much faster to iterate this way.

## Phase 3 — Minimal rendering

1. Get a basic OpenGL pipeline running: shader loading, a camera, a single hardcoded sphere on screen. Confirm your GLFW/glad/CMake setup actually produces a window with a lit 3D object — this validates your whole render pipeline in isolation from the visualization logic.

2. Add an orbit camera (mouse drag to rotate around the scene, scroll to zoom).

3. Switch to instanced rendering for the sphere: one mesh uploaded once, per-node position/color pulled from the VizGraph each frame, drawn in a single draw call.

4. Add edge rendering (either GL_LINES or instanced thin cylinders — cylinders look better and reuse your instancing pipeline, but are more work).

## Phase 4 — Wire it together

1. Connect Phase 1–3: every frame, run the physics step on the VizGraph, then render its current node/edge state. At this point you should see your linked list floating and settling into a line-like shape on screen.

2. Confirm the loop is stable at 60fps with a modest node count before moving on.

## Phase 5 — Remaining adapters

1. Write extraction functions for binary tree, ternary tree, n-ary tree, and graph, following the same pattern as the linked list adapter.

2. Test each one visually using the pipeline you already built — no new rendering code needed, only new adapters.

## Phase 6 — UI controls

1. Pick and integrate an immediate-mode GUI library (Nuklear for a pure-C dependency, or Dear ImGui via cimgui bindings if you don't mind a C++ piece in the build).

2. Add a basic panel: choose structure type, add node, remove node.

3. Wire these buttons to actually mutate the real data structure, then re-extract (or incrementally update) the VizGraph so the visualization reflects the change live.

4. Add structure-specific operations as buttons (e.g. tree rebalance, graph BFS/DFS with animated traversal highlighting).

## Phase 7 — Polish (ongoing, not blocking)

1. Visual refinement: node coloring by state (e.g. highlight during traversal), labels/values on nodes, lighting quality.

2. Performance: only worry about Barnes-Hut or spatial partitioning for repulsion if you actually hit node counts where O(n²) becomes a problem.

3. Extensibility pass: once a second or third structure type is visualized end-to-end, look back at the adapter interface and confirm it's actually generic enough for structures you haven't built yet (heaps, hash tables, tries, etc.).



> At a later point implement gravity so the nodes fall to the ground in 3d space