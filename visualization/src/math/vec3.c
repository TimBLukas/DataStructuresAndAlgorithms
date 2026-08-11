#include "vec3.h"

#include <math.h>
#include <stdlib.h>

Vec3 vec3_add(const Vec3 *v1, const Vec3 *v2) {
    Vec3 result;

    result.x = v1->x + v2->x;
    result.y = v1->y + v2->y;
    result.z = v1->z + v2->z;

    return result;
}

Vec3 vec3_sub(const Vec3 *v1, const Vec3 *v2) {
    Vec3 result;

    result.x = v1->x - v2->x;
    result.y = v1->y - v2->y;
    result.z = v1->z - v2->z;

    return result;
}

Vec3 vec3_scale(const Vec3 *v, float factor) {
    Vec3 result;

    result.x = v->x * factor;
    result.y = v->y * factor;
    result.z = v->z * factor;

    return result;
}

float vec3_length(const Vec3 *v) {
    return sqrtf(v->x * v->x + v->y * v->y + v->z * v->z);
}

Vec3 vec3_normalize(const Vec3 *v) {
    Vec3 result;

    float length = vec3_length(v);

    if (length == 0.0f) {
        result.x = 0.0f;
        result.y = 0.0f;
        result.z = 0.0f;
        return result;
    }

    result.x = v->x / length;
    result.y = v->y / length;
    result.z = v->z / length;

    return result;
}

float random_float(float range) {
    return -range + ((float)rand() / (float)RAND_MAX) * (2.0f * range);
}

void vec3_random_jitter(Vec3 *v, float jitter) {
    v->x += random_float(jitter);
    v->y += random_float(jitter);
    v->z += random_float(jitter);
}
