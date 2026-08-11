#ifndef VEC3_H
#define VEC3_H

/*
 * Vector Definition
 */
typedef struct {
    float x;
    float y;
    float z;
} Vec3;

/*
 * Vector functions
 */

Vec3 vec3_add(const Vec3 *v1, const Vec3 *v2);
Vec3 vec3_sub(const Vec3 *v1, const Vec3 *v2);
Vec3 vec3_scale(const Vec3 *v, float factor);

float vec3_length(const Vec3 *v);
Vec3 vec3_normalize(const Vec3 *v);

void vec3_random_jitter(Vec3 *v, float jitter);

#endif
