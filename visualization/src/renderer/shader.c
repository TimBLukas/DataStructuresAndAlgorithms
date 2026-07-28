#include "shader.h"

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/**
* USAGE:
* #include "renderer/shader.h" 
* Shader shader = shader_create(
*     "shaders/basic.vert",
*     "shaders/basic.frag"
* );
* 
* shader_use(&shader);
* 
* // Render...
* 
* shader_destroy(&shader);
*/

static char* read_file(const char* path)
{
        FILE* file = fopen(path, "rb");

        if (file == NULL) {
                printf("ERROR::SHADER::FILE_NOT_FOUND\n");
                return NULL;
        }

        fseek(file, 0, SEEK_END);
        long length = ftell(file);
        rewind(file);

        char* buffer = malloc(length + 1);

        if (buffer == NULL) {
                fclose(file);
                return NULL;
        }

        fread(buffer, 1, length, file);
        buffer[length] = '\0';

        fclose(file);

        return buffer;
}


Shader shader_create(const char* vertex_path,
                     const char* fragment_path)
{
    Shader shader;
    shader.ID = 0;

    char* vertex_source = read_file(vertex_path);
    char* fragment_source = read_file(fragment_path);

    if (vertex_source == NULL || fragment_source == NULL) {
        free(vertex_source);
        free(fragment_source);
        return shader;
    }

    GLint success;
    GLchar info_log[512];

    //--------------------------
    // Vertex Shader
    //--------------------------

    GLuint vertex_shader = glCreateShader(GL_VERTEX_SHADER);

    glShaderSource(vertex_shader, 1,
                   (const GLchar* const*)&vertex_source,
                   NULL);

    glCompileShader(vertex_shader);

    glGetShaderiv(vertex_shader,
                  GL_COMPILE_STATUS,
                  &success);

    if (!success) {
        glGetShaderInfoLog(vertex_shader,
                           sizeof(info_log),
                           NULL,
                           info_log);

        printf("ERROR::VERTEX_SHADER\n%s\n", info_log);
    }

    //--------------------------
    // Fragment Shader
    //--------------------------
    GLuint fragment_shader = glCreateShader(GL_FRAGMENT_SHADER);

    glShaderSource(fragment_shader, 1,
                   (const GLchar* const*)&fragment_source,
                   NULL);

    glCompileShader(fragment_shader);

    glGetShaderiv(fragment_shader,
                  GL_COMPILE_STATUS,
                  &success);

    if (!success) {
        glGetShaderInfoLog(fragment_shader,
                           sizeof(info_log),
                           NULL,
                           info_log);

        printf("ERROR::FRAGMENT_SHADER\n%s\n", info_log);
    }

    //--------------------------
    // Shader Program
    //--------------------------

    shader.ID = glCreateProgram();

    glAttachShader(shader.ID, vertex_shader);
    glAttachShader(shader.ID, fragment_shader);

    glLinkProgram(shader.ID);

    glGetProgramiv(shader.ID,
                   GL_LINK_STATUS,
                   &success);

    if (!success) {
        glGetProgramInfoLog(shader.ID,
                            sizeof(info_log),
                            NULL,
                            info_log);

        printf("ERROR::SHADER_PROGRAM\n%s\n", info_log);
    }

    glDeleteShader(vertex_shader);
    glDeleteShader(fragment_shader);

    free(vertex_source);
    free(fragment_source);

    return shader;
}


void shader_use(const Shader* shader) 
{
    glUseProgram(shader->ID);
}


void shader_set_bool(const Shader* shader,
                     const char* name,
                     int value) 
{
    glUniform1i(
        glGetUniformLocation(shader->ID, name),
        value
    );
}


void shader_set_int(const Shader* shader,
                    const char* name,
                    int value)
{
    glUniform1i(
        glGetUniformLocation(shader->ID, name),
        value
    );
}


void shader_set_float(const Shader* shader,
                      const char* name,
                      float value)
{
    glUniform1f(
        glGetUniformLocation(shader->ID, name),
        value
    );
}


void shader_destroy(Shader* shader)
{
    glDeleteProgram(shader->ID);
    shader->ID = 0;
}
