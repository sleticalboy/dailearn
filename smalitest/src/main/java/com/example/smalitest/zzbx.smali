.class public final Lcom/example/smalitest/zzbx;
.super Ljava/lang/Object;
.source "zzbx.java"


# static fields
.field private static zza:Ljava/lang/String;


# direct methods
.method public constructor <init>()V
    .registers 1

    .prologue
    .line 17
    invoke-direct {p0}, Ljava/lang/Object;-><init>()V

    return-void
.end method

.method public static declared-synchronized zza(Landroid/content/Context;)Ljava/lang/String;
    .registers 9
    .param p0, "context"    # Landroid/content/Context;

    .prologue
    .line 22
    const-class v4, Lcom/example/smalitest/zzbx;

    monitor-enter v4

    :try_start_3
    const-class v5, Lcom/example/smalitest/zzbx;

    monitor-enter v5
    :try_end_6
    .catchall {:try_start_3 .. :try_end_6} :catchall_3b

    .line 23
    :try_start_6
    sget-object v3, Lcom/example/smalitest/zzbx;->zza:Ljava/lang/String;

    if-nez v3, :cond_2c

    .line 24
    invoke-virtual {p0}, Landroid/content/Context;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object v0

    .line 25
    .local v0, "contentResolver":Landroid/content/ContentResolver;
    if-nez v0, :cond_31

    const/4 v2, 0x0

    .line 26
    .local v2, "tmp":Ljava/lang/String;
    :goto_11
    if-eqz v2, :cond_19

    invoke-static {}, Lcom/example/smalitest/zzbx;->zzb()Z

    move-result v3

    if-eqz v3, :cond_26

    .line 27
    :cond_19
    new-instance v3, Ljava/security/SecureRandom;

    invoke-direct {v3}, Ljava/security/SecureRandom;-><init>()V

    invoke-virtual {v3}, Ljava/security/SecureRandom;->nextLong()J

    move-result-wide v6

    invoke-static {v6, v7}, Ljava/lang/Long;->toHexString(J)Ljava/lang/String;

    move-result-object v2

    .line 29
    :cond_26
    invoke-static {v2}, Lcom/example/smalitest/zzbx;->zzc(Ljava/lang/String;)Ljava/lang/String;

    move-result-object v3

    sput-object v3, Lcom/example/smalitest/zzbx;->zza:Ljava/lang/String;

    .line 31
    .end local v0    # "contentResolver":Landroid/content/ContentResolver;
    .end local v2    # "tmp":Ljava/lang/String;
    :cond_2c
    sget-object v1, Lcom/example/smalitest/zzbx;->zza:Ljava/lang/String;

    .line 32
    .local v1, "str":Ljava/lang/String;
    monitor-exit v5
    :try_end_2f
    .catchall {:try_start_6 .. :try_end_2f} :catchall_38

    .line 33
    monitor-exit v4

    return-object v1

    .line 25
    .end local v1    # "str":Ljava/lang/String;
    .restart local v0    # "contentResolver":Landroid/content/ContentResolver;
    :cond_31
    :try_start_31
    const-string v3, "android_id"

    invoke-static {v0, v3}, Landroid/provider/Settings$Secure;->getString(Landroid/content/ContentResolver;Ljava/lang/String;)Ljava/lang/String;

    move-result-object v2

    goto :goto_11

    .line 32
    .end local v0    # "contentResolver":Landroid/content/ContentResolver;
    :catchall_38
    move-exception v3

    monitor-exit v5
    :try_end_3a
    .catchall {:try_start_31 .. :try_end_3a} :catchall_38

    :try_start_3a
    throw v3
    :try_end_3b
    .catchall {:try_start_3a .. :try_end_3b} :catchall_3b

    .line 22
    :catchall_3b
    move-exception v3

    monitor-exit v4

    throw v3
.end method

.method public static zzb()Z
    .registers 3

    .prologue
    const/4 v2, 0x0

    .line 37
    sget-object v0, Landroid/os/Build;->FINGERPRINT:Ljava/lang/String;

    const-string v1, "generic"

    invoke-virtual {v0, v1}, Ljava/lang/String;->startsWith(Ljava/lang/String;)Z

    move-result v0

    if-nez v0, :cond_3d

    sget-object v0, Landroid/os/Build;->FINGERPRINT:Ljava/lang/String;

    const-string v1, "unknown"

    invoke-virtual {v0, v1}, Ljava/lang/String;->startsWith(Ljava/lang/String;)Z

    move-result v0

    if-nez v0, :cond_3d

    sget-object v0, Landroid/os/Build;->MODEL:Ljava/lang/String;

    const-string v1, "google_sdk"

    invoke-virtual {v0, v1}, Ljava/lang/String;->contains(Ljava/lang/CharSequence;)Z

    move-result v0

    if-nez v0, :cond_3d

    sget-object v0, Landroid/os/Build;->MODEL:Ljava/lang/String;

    const-string v1, "Emulator"

    invoke-virtual {v0, v1}, Ljava/lang/String;->contains(Ljava/lang/CharSequence;)Z

    move-result v0

    if-nez v0, :cond_3d

    sget-object v0, Landroid/os/Build;->MODEL:Ljava/lang/String;

    const-string v1, "Android SDK built for x86"

    invoke-virtual {v0, v1}, Ljava/lang/String;->contains(Ljava/lang/CharSequence;)Z

    move-result v0

    if-nez v0, :cond_3d

    sget-object v0, Landroid/os/Build;->MANUFACTURER:Ljava/lang/String;

    const-string v1, "Genymotion"

    invoke-virtual {v0, v1}, Ljava/lang/String;->contains(Ljava/lang/CharSequence;)Z

    move-result v0

    if-eqz v0, :cond_3e

    .line 40
    :cond_3d
    :goto_3d
    return v2

    :cond_3e
    sget-object v0, Landroid/os/Build;->BRAND:Ljava/lang/String;

    const-string v1, "generic"

    invoke-virtual {v0, v1}, Ljava/lang/String;->startsWith(Ljava/lang/String;)Z

    move-result v0

    if-eqz v0, :cond_52

    sget-object v0, Landroid/os/Build;->DEVICE:Ljava/lang/String;

    const-string v1, "generic"

    invoke-virtual {v0, v1}, Ljava/lang/String;->startsWith(Ljava/lang/String;)Z

    move-result v0

    if-nez v0, :cond_3d

    :cond_52
    const-string v0, "google_sdk"

    sget-object v1, Landroid/os/Build;->PRODUCT:Ljava/lang/String;

    invoke-virtual {v0, v1}, Ljava/lang/String;->equals(Ljava/lang/Object;)Z

    move-result v0

    if-eqz v0, :cond_3d

    goto :goto_3d
.end method

.method private static zzc(Ljava/lang/String;)Ljava/lang/String;
    .registers 10
    .param p0, "str"    # Ljava/lang/String;

    .prologue
    .line 44
    const/4 v0, 0x0

    .local v0, "i":I
    :goto_1
    const/4 v3, 0x3

    if-ge v0, v3, :cond_30

    .line 46
    :try_start_4
    const-string v3, "MD5"

    invoke-static {v3}, Ljava/security/MessageDigest;->getInstance(Ljava/lang/String;)Ljava/security/MessageDigest;

    move-result-object v1

    .line 47
    .local v1, "instance":Ljava/security/MessageDigest;
    invoke-virtual {p0}, Ljava/lang/String;->getBytes()[B

    move-result-object v3

    invoke-virtual {v1, v3}, Ljava/security/MessageDigest;->update([B)V

    .line 48
    const-string v3, "%032X"

    const/4 v4, 0x1

    new-array v4, v4, [Ljava/lang/Object;

    const/4 v5, 0x0

    new-instance v6, Ljava/math/BigInteger;

    const/4 v7, 0x1

    invoke-virtual {v1}, Ljava/security/MessageDigest;->digest()[B

    move-result-object v8

    invoke-direct {v6, v7, v8}, Ljava/math/BigInteger;-><init>(I[B)V

    aput-object v6, v4, v5

    invoke-static {v3, v4}, Ljava/lang/String;->format(Ljava/lang/String;[Ljava/lang/Object;)Ljava/lang/String;
    :try_end_26
    .catch Ljava/lang/ArithmeticException; {:try_start_4 .. :try_end_26} :catch_28
    .catch Ljava/security/NoSuchAlgorithmException; {:try_start_4 .. :try_end_26} :catch_2c

    move-result-object v3

    .line 54
    .end local v1    # "instance":Ljava/security/MessageDigest;
    :goto_27
    return-object v3

    .line 49
    :catch_28
    move-exception v2

    .line 50
    .local v2, "unused":Ljava/lang/ArithmeticException;
    const-string v3, ""

    goto :goto_27

    .line 51
    .end local v2    # "unused":Ljava/lang/ArithmeticException;
    :catch_2c
    move-exception v3

    .line 44
    add-int/lit8 v0, v0, 0x1

    goto :goto_1

    .line 54
    :cond_30
    const-string v3, ""

    goto :goto_27
.end method
