//
// Created by binlee on 2022/12/26.
//

#include "jni.h"
{imported-headers}
#include "../../../../AlgoBase/commonAI/src/main/jni/XYAIStructExchange.h"
#include "../../../../AlgoBase/commonAI/src/main/jni/method_tracer.h"

#define TAG "{module-name}"

{algo-nss}

jobject Q{module-name}_Init(JNIEnv *env, jclass clazz, jstring model_path) {
  ScopedString path(env, model_path);
  ALOGD(TAG, "%s model path: %s", __func__, path.c_str())

  auto ir = new {itf-name}();
  FUNC_ENTER(__func__, (long) ir)
  int res = ir->Init(path.c_str());
  FUNC_EXIT(env, __func__, res, {ai-type}, AV)
  if (res != XYAI_NO_ERROR) {
    ALOGE(TAG, "%s error: 0x%x", __func__, res)
  }
  return XYAIInitResultC2J(env, res, res == XYAI_NO_ERROR ? (long) ir : 0);
}

jint Q{module-name}_SetProp(JNIEnv *env, jclass clazz, jlong handle, jint key, jlong value) {
  auto ir = ({itf-name} *) handle;
  int res =  ir->SetProp(key, (void *) value);
  ALOGD(TAG, "%s, res: 0x%x", __func__, res)
  return res;
}

jint Q{module-name}_ForwardProcess(JNIEnv *env, jclass clazz, jlong handle) {
  auto ir = ({itf-name} *) handle;
  FUNC_ENTER(__func__ , handle)
  int res = ir->ForwardProcess();
  FUNC_EXIT(env, __func__, res, {ai-type}, AV)
  return res;
}

jint Q{module-name}_GetProp(JNIEnv *env, jclass clazz, jlong handle, jint key, jlong value) {
  auto ir = ({itf-name} *) handle;
  int res = ir->GetProp(key, (void *) value);
  ALOGD(TAG, "%s, res: 0x%x", __func__, res)
  return res;
}

jstring Q{module-name}_GetVersion(JNIEnv *env, jclass clazz) {
  auto ir = std::unique_ptr<{itf-name}>(new {itf-name}());
  return env->NewStringUTF(ir->GetAISDKVersion());
}

void Q{module-name}_Release(JNIEnv *env, jclass clazz, jlong handle) {
  auto ir = ({itf-name} *) handle;
  ir->Release();
}

jint Q{module-name}_Forward4J(JNIEnv *env, jclass clazz, jlong handle, jobject input, jint width, jint height, jobject output) {
  ALOGE(TAG, "%s enter", __func__)
  auto ir = ({itf-name} *) handle;
  auto frame = std::unique_ptr<XYAIFrameInfo>(AIFrameInfoJ2C(env, input));
  ALOGE(TAG, "%s input w: %d, h: %d, fmt: %d, pCache: %p", __func__, frame->width, frame->height, frame->format, frame->pCache)
  int res = ir->SetProp(RESTORE_INPUT_IMG, frame.get());
  ALOGE_IF(TAG, res != 0, "SetProp(RESTORE_INPUT_IMG) failed: 0x%x", res)

  ALOGE(TAG, "%s expected w: %d, h: %d, fmt: %d", __func__, width, height, frame->format)
  res = ir->SetProp(RESTORE_EXPECTED_WID, &width);
  ALOGE_IF(TAG, res != 0, "SetProp(RESTORE_EXPECTED_WID) failed: 0x%x", res)
  res = ir->SetProp(RESTORE_EXPECTED_HEI, &height);
  ALOGE_IF(TAG, res != 0, "SetProp(RESTORE_EXPECTED_HEI) failed: 0x%x", res)

  res = ir->SetProp(RESTORE_EXPECTED_FMT, &frame->format);
  ALOGE_IF(TAG, res != 0, "SetProp(RESTORE_EXPECTED_FMT) failed: 0x%x", res)
  res = ir->ForwardProcess();
  ALOGE_IF(TAG, res != 0, "ForwardProcess() failed: 0x%x", res)
  XYAIFrameInfo result = {};
  res = ir->GetProp(RESTORE_OUTPUT_IMG, &result);
  ALOGE_IF(TAG, res != 0, "GetProp(RESTORE_OUTPUT_IMG) failed: 0x%x", res)
  ALOGE(TAG, "%s output w: %d, h: %d, fmt: %d, pCache: %p", __func__, result.width, result.height, result.format, result.pCache)
  if (res == XYAI_NO_ERROR) {
    AIFrameInfoC2J(env, &result, output);
  }
  ALOGE(TAG, "%s exit: %d", __func__, res)
  return res;
}

JNINativeMethod g{module-name}Methods[] = {
  {"nativeInit", "(Ljava/lang/String;)Lcom/quvideo/mobile/component/common/AIInitResult;", (void *) Q{module-name}_Init},
  {"nativeSetProp", "(JIJ)I", (void *) Q{module-name}_SetProp},
  {"nativeForwardProcess", "(J)I", (void *) Q{module-name}_ForwardProcess},
  {"nativeGetProp", "(JIJ)I", (void *) Q{module-name}_GetProp},
  {"nativeGetVersion", "()Ljava/lang/String;", (void *) Q{module-name}_GetVersion},
  {"nativeRelease", "(J)V", (void *) Q{module-name}_Release},
  {"nativeForward4J",
    "(JLcom/quvideo/mobile/component/common/AIFrameInfo;IILcom/quvideo/mobile/component/common/AIFrameInfo;)I",
   (void *) Q{module-name}_Forward4J},
};

jint JNI_OnLoad(JavaVM* vm, void* reserved) {
  JNIEnv *env = nullptr;
  int res = vm->GetEnv((void **) &env, JNI_VERSION_1_6);
  if (res != JNI_OK || env == nullptr) {
    return JNI_ERR;
  }
  jclass clazz = env->FindClass("com/quvideo/mobile/component/{pkg-name}/Q{module-name}");
  env->RegisterNatives(clazz, g{module-name}Methods, sizeof(g{module-name}Methods) / sizeof(JNINativeMethod));
  env->DeleteLocalRef(clazz);
  return JNI_VERSION_1_6;
}

void JNI_OnUnload(JavaVM* vm, void* reserved) {
  JNIEnv *env = nullptr;
  int res = vm->GetEnv((void **) &env, JNI_VERSION_1_6);
  if (res != JNI_OK || env == nullptr) {
    return;
  }
  jclass clazz = env->FindClass("com/quvideo/mobile/component/{pkg-name}/Q{module-name}");
  env->UnregisterNatives(clazz);
  env->DeleteLocalRef(clazz);
}