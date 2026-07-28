#ifndef SHADER_H
#define SHADER_H

#include "../../external/glad/glad/glad.h"



typedef struct Shader
{
        unsigned int ID;
} Shader;


/* Creates a shader program from two GLSL files */
Shader shader_create(const char* vertex_path, const char* fragment_path);


/* Activates the shader program */
void shader_use(const Shader* shader);


/* Uniform helpers */
void shader_set_bool(const Shader* shader, const char* name, int value);
void shader_set_int(const Shader* shader, const char* name, int value);
void shader_set_float(const Shader* shader, const char* name, float value);


/* Deletes the OpenGL program */
void shader_destroy(Shader* shader);

#endif
