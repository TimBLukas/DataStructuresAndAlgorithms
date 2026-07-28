// #include <GL/glext.h>
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

// #include <glad/glad.h>
#include "../external/glad/glad/glad.h"
#include <GLFW/glfw3.h>


void framebuffer_size_callback(GLFWwindow* window, int width, int height);
void processInput(GLFWwindow *window);

// settings
const unsigned int SCR_WIDTH = 800;
const unsigned int SCR_HEIGHT = 600;

const char *vertexShaderSource = "#version 340 core\n"
        "layout (location = 0) in vec3 aPos;\n"
        "void main()\n"
        "{\n"
        "       gl_Position = vec4(aPos.x, aPos.y, aPos.z, 1.0);\n"
        "}\0";

const char* fragmentShaderSource = "#version 340 core\n"
        "out vec4 FragmentColor;\n"
        "void main()\n"
        "{\n"
        "       FragColor = vec4(1.0f, 0.5f, 0.2f, 1.0f);\n"
        "}\n";

int main(int argc, char* argv[])
{
        if (!glfwInit()) {
                printf("Failed to initialize GLFW\n");
                return -1;
        }

        glfwWindowHint(GLFW_CONTEXT_VERSION_MAJOR, 3);
        glfwWindowHint(GLFW_CONTEXT_VERSION_MINOR, 3);
        glfwWindowHint(GLFW_OPENGL_PROFILE, GLFW_OPENGL_CORE_PROFILE);

        GLFWwindow* window = glfwCreateWindow(SCR_WIDTH, SCR_HEIGHT, "Learn OpenGL", NULL,NULL);

        if ( window == NULL ) {
                printf("Failed to create a GLFW window\n");
                glfwTerminate();
                return -1;
        }

        glfwMakeContextCurrent(window);
        if (!gladLoadGLLoader((GLADloadproc)glfwGetProcAddress))
        {
                printf("Failed to initialize GLAD\n");
                return -1;
        }

        glfwSetFramebufferSizeCallback(window, framebuffer_size_callback);


        glViewport(0, 0, 800, 600);

        // shaders

        // psoitive y-axis points in the up-direction and (0,0) coordinates are at the center of the screen
        float vertices[] = {
                -0.5f, -0.5f, 0.0f,
                0.5f, -0.5f, 0.0f,
                0.0f, 0.5f, 0.0f
        };

        // vertex buffer object
        unsigned int VBO;
        glGenBuffers(1, &VBO);
        glBindBuffer(GL_ARRAY_BUFFER, VBO);
        glBufferData(GL_ARRAY_BUFFER, sizeof(vertices), vertices, GL_STATIC_DRAW);

        unsigned int vertexShader;
        vertexShader = glCreateShader(GL_VERTEX_SHADER);
        glShaderSource(vertexShader, 1, &vertexShaderSource, NULL);
        glCompileShader(vertexShader);

        int success;
        char infoLog[512];
        glGetShaderiv(vertexShader, GL_COMPILE_STATUS, &success);
        if( !success ) {
                glGetShaderInfoLog(vertexShader, 512, NULL, infoLog);
                printf("Error::SHADER::VERTEX::COMPILATION_FAILED: %s\n", infoLog);
        }

        unsigned int fragmentShader;
        fragmentShader = glCreateShader(GL_FRAGMENT_SHADER);
        glShaderSource(fragmentShader, 1, &fragmentShaderSource, NULL);
        glCompileShader(fragmentShader);
        glGetShaderiv(fragmentShader, GL_COMPILE_STATUS, &success);
        if(!success) {
                glGetProgramInfoLog(fragmentShader, 512, NULL, infoLog);
                printf("Error::SHADER::FRAGMENT::COMPILATION_FAILED: %s\n", infoLog);
        }

        unsigned int shaderProgram;
        shaderProgram = glCreateProgram();
        glAttachShader(shaderProgram, vertexShader);
        glAttachShader(shaderProgram, fragmentShader);
        glLinkProgram(shaderProgram);
        glGetProgramiv(shaderProgram, GL_LINK_STATUS, &success);
        if(!success) {
                glGetProgramInfoLog(shaderProgram, 512, NULL, infoLog);
                printf("Error::PROGRAM::LINKING_FAILED: %s\n", infoLog);
        }

        glDeleteShader(vertexShader);
        glDeleteShader(fragmentShader);

        glUseProgram(shaderProgram);


        while (!glfwWindowShouldClose(window))
        {
                processInput(window);

                // Rendering code here
                glClearColor(0.2f, 0.3f, 0.3f, 1.0f);
                glClear(GL_COLOR_BUFFER_BIT);

                // render triangle
                
                //
                glfwSwapBuffers(window);
                glfwPollEvents();
        }

        // GLFW: terminate (clear all glfw ressources)
        glfwTerminate();
        return 0;
}


void processInput(GLFWwindow *window) {
        if ( glfwGetKey(window, GLFW_KEY_ESCAPE) == GLFW_PRESS)
                glfwSetWindowShouldClose(window, true);
}

void framebuffer_size_callback(GLFWwindow *window, int width, int height) {
        glViewport(0, 0, width, height);
}
