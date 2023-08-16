// Generated by the protocol buffer compiler.  DO NOT EDIT!
// source: algo_args.proto

#ifndef GOOGLE_PROTOBUF_INCLUDED_algo_5fargs_2eproto
#define GOOGLE_PROTOBUF_INCLUDED_algo_5fargs_2eproto

#include <limits>
#include <string>

#include <google/protobuf/port_def.inc>
#if PROTOBUF_VERSION < 3021000
#error This file was generated by a newer version of protoc which is
#error incompatible with your Protocol Buffer headers. Please update
#error your headers.
#endif
#if 3021012 < PROTOBUF_MIN_PROTOC_VERSION
#error This file was generated by an older version of protoc which is
#error incompatible with your Protocol Buffer headers. Please
#error regenerate this file with a newer version of protoc.
#endif

#include <google/protobuf/port_undef.inc>
#include <google/protobuf/io/coded_stream.h>
#include <google/protobuf/arena.h>
#include <google/protobuf/arenastring.h>
#include <google/protobuf/generated_message_util.h>
#include <google/protobuf/metadata_lite.h>
#include <google/protobuf/generated_message_reflection.h>
#include <google/protobuf/message.h>
#include <google/protobuf/repeated_field.h>  // IWYU pragma: export
#include <google/protobuf/extension_set.h>  // IWYU pragma: export
#include <google/protobuf/map.h>  // IWYU pragma: export
#include <google/protobuf/map_entry.h>
#include <google/protobuf/map_field_inl.h>
#include <google/protobuf/unknown_field_set.h>
// @@protoc_insertion_point(includes)
#include <google/protobuf/port_def.inc>
#define PROTOBUF_INTERNAL_EXPORT_algo_5fargs_2eproto
PROTOBUF_NAMESPACE_OPEN
namespace internal {
class AnyMetadata;
}  // namespace internal
PROTOBUF_NAMESPACE_CLOSE

// Internal implementation detail -- do not use these members.
struct TableStruct_algo_5fargs_2eproto {
  static const uint32_t offsets[];
};
extern const ::PROTOBUF_NAMESPACE_ID::internal::DescriptorTable descriptor_table_algo_5fargs_2eproto;
class AlgoInput;
struct AlgoInputDefaultTypeInternal;
extern AlgoInputDefaultTypeInternal _AlgoInput_default_instance_;
class AlgoInput_IargsEntry_DoNotUse;
struct AlgoInput_IargsEntry_DoNotUseDefaultTypeInternal;
extern AlgoInput_IargsEntry_DoNotUseDefaultTypeInternal _AlgoInput_IargsEntry_DoNotUse_default_instance_;
class AlgoOutput;
struct AlgoOutputDefaultTypeInternal;
extern AlgoOutputDefaultTypeInternal _AlgoOutput_default_instance_;
class AlgoOutput_OargsEntry_DoNotUse;
struct AlgoOutput_OargsEntry_DoNotUseDefaultTypeInternal;
extern AlgoOutput_OargsEntry_DoNotUseDefaultTypeInternal _AlgoOutput_OargsEntry_DoNotUse_default_instance_;
PROTOBUF_NAMESPACE_OPEN
template<> ::AlgoInput* Arena::CreateMaybeMessage<::AlgoInput>(Arena*);
template<> ::AlgoInput_IargsEntry_DoNotUse* Arena::CreateMaybeMessage<::AlgoInput_IargsEntry_DoNotUse>(Arena*);
template<> ::AlgoOutput* Arena::CreateMaybeMessage<::AlgoOutput>(Arena*);
template<> ::AlgoOutput_OargsEntry_DoNotUse* Arena::CreateMaybeMessage<::AlgoOutput_OargsEntry_DoNotUse>(Arena*);
PROTOBUF_NAMESPACE_CLOSE

// ===================================================================

class AlgoInput_IargsEntry_DoNotUse : public ::PROTOBUF_NAMESPACE_ID::internal::MapEntry<AlgoInput_IargsEntry_DoNotUse, 
    std::string, std::string,
    ::PROTOBUF_NAMESPACE_ID::internal::WireFormatLite::TYPE_STRING,
    ::PROTOBUF_NAMESPACE_ID::internal::WireFormatLite::TYPE_STRING> {
public:
  typedef ::PROTOBUF_NAMESPACE_ID::internal::MapEntry<AlgoInput_IargsEntry_DoNotUse, 
    std::string, std::string,
    ::PROTOBUF_NAMESPACE_ID::internal::WireFormatLite::TYPE_STRING,
    ::PROTOBUF_NAMESPACE_ID::internal::WireFormatLite::TYPE_STRING> SuperType;
  AlgoInput_IargsEntry_DoNotUse();
  explicit PROTOBUF_CONSTEXPR AlgoInput_IargsEntry_DoNotUse(
      ::PROTOBUF_NAMESPACE_ID::internal::ConstantInitialized);
  explicit AlgoInput_IargsEntry_DoNotUse(::PROTOBUF_NAMESPACE_ID::Arena* arena);
  void MergeFrom(const AlgoInput_IargsEntry_DoNotUse& other);
  static const AlgoInput_IargsEntry_DoNotUse* internal_default_instance() { return reinterpret_cast<const AlgoInput_IargsEntry_DoNotUse*>(&_AlgoInput_IargsEntry_DoNotUse_default_instance_); }
  static bool ValidateKey(std::string* s) {
    return ::PROTOBUF_NAMESPACE_ID::internal::WireFormatLite::VerifyUtf8String(s->data(), static_cast<int>(s->size()), ::PROTOBUF_NAMESPACE_ID::internal::WireFormatLite::PARSE, "AlgoInput.IargsEntry.key");
 }
  static bool ValidateValue(std::string* s) {
    return ::PROTOBUF_NAMESPACE_ID::internal::WireFormatLite::VerifyUtf8String(s->data(), static_cast<int>(s->size()), ::PROTOBUF_NAMESPACE_ID::internal::WireFormatLite::PARSE, "AlgoInput.IargsEntry.value");
 }
  using ::PROTOBUF_NAMESPACE_ID::Message::MergeFrom;
  ::PROTOBUF_NAMESPACE_ID::Metadata GetMetadata() const final;
  friend struct ::TableStruct_algo_5fargs_2eproto;
};

// -------------------------------------------------------------------

class AlgoInput final :
    public ::PROTOBUF_NAMESPACE_ID::Message /* @@protoc_insertion_point(class_definition:AlgoInput) */ {
 public:
  inline AlgoInput() : AlgoInput(nullptr) {}
  ~AlgoInput() override;
  explicit PROTOBUF_CONSTEXPR AlgoInput(::PROTOBUF_NAMESPACE_ID::internal::ConstantInitialized);

  AlgoInput(const AlgoInput& from);
  AlgoInput(AlgoInput&& from) noexcept
    : AlgoInput() {
    *this = ::std::move(from);
  }

  inline AlgoInput& operator=(const AlgoInput& from) {
    CopyFrom(from);
    return *this;
  }
  inline AlgoInput& operator=(AlgoInput&& from) noexcept {
    if (this == &from) return *this;
    if (GetOwningArena() == from.GetOwningArena()
  #ifdef PROTOBUF_FORCE_COPY_IN_MOVE
        && GetOwningArena() != nullptr
  #endif  // !PROTOBUF_FORCE_COPY_IN_MOVE
    ) {
      InternalSwap(&from);
    } else {
      CopyFrom(from);
    }
    return *this;
  }

  static const ::PROTOBUF_NAMESPACE_ID::Descriptor* descriptor() {
    return GetDescriptor();
  }
  static const ::PROTOBUF_NAMESPACE_ID::Descriptor* GetDescriptor() {
    return default_instance().GetMetadata().descriptor;
  }
  static const ::PROTOBUF_NAMESPACE_ID::Reflection* GetReflection() {
    return default_instance().GetMetadata().reflection;
  }
  static const AlgoInput& default_instance() {
    return *internal_default_instance();
  }
  static inline const AlgoInput* internal_default_instance() {
    return reinterpret_cast<const AlgoInput*>(
               &_AlgoInput_default_instance_);
  }
  static constexpr int kIndexInFileMessages =
    1;

  friend void swap(AlgoInput& a, AlgoInput& b) {
    a.Swap(&b);
  }
  inline void Swap(AlgoInput* other) {
    if (other == this) return;
  #ifdef PROTOBUF_FORCE_COPY_IN_SWAP
    if (GetOwningArena() != nullptr &&
        GetOwningArena() == other->GetOwningArena()) {
   #else  // PROTOBUF_FORCE_COPY_IN_SWAP
    if (GetOwningArena() == other->GetOwningArena()) {
  #endif  // !PROTOBUF_FORCE_COPY_IN_SWAP
      InternalSwap(other);
    } else {
      ::PROTOBUF_NAMESPACE_ID::internal::GenericSwap(this, other);
    }
  }
  void UnsafeArenaSwap(AlgoInput* other) {
    if (other == this) return;
    GOOGLE_DCHECK(GetOwningArena() == other->GetOwningArena());
    InternalSwap(other);
  }

  // implements Message ----------------------------------------------

  AlgoInput* New(::PROTOBUF_NAMESPACE_ID::Arena* arena = nullptr) const final {
    return CreateMaybeMessage<AlgoInput>(arena);
  }
  using ::PROTOBUF_NAMESPACE_ID::Message::CopyFrom;
  void CopyFrom(const AlgoInput& from);
  using ::PROTOBUF_NAMESPACE_ID::Message::MergeFrom;
  void MergeFrom( const AlgoInput& from) {
    AlgoInput::MergeImpl(*this, from);
  }
  private:
  static void MergeImpl(::PROTOBUF_NAMESPACE_ID::Message& to_msg, const ::PROTOBUF_NAMESPACE_ID::Message& from_msg);
  public:
  PROTOBUF_ATTRIBUTE_REINITIALIZES void Clear() final;
  bool IsInitialized() const final;

  size_t ByteSizeLong() const final;
  const char* _InternalParse(const char* ptr, ::PROTOBUF_NAMESPACE_ID::internal::ParseContext* ctx) final;
  uint8_t* _InternalSerialize(
      uint8_t* target, ::PROTOBUF_NAMESPACE_ID::io::EpsCopyOutputStream* stream) const final;
  int GetCachedSize() const final { return _impl_._cached_size_.Get(); }

  private:
  void SharedCtor(::PROTOBUF_NAMESPACE_ID::Arena* arena, bool is_message_owned);
  void SharedDtor();
  void SetCachedSize(int size) const final;
  void InternalSwap(AlgoInput* other);

  private:
  friend class ::PROTOBUF_NAMESPACE_ID::internal::AnyMetadata;
  static ::PROTOBUF_NAMESPACE_ID::StringPiece FullMessageName() {
    return "AlgoInput";
  }
  protected:
  explicit AlgoInput(::PROTOBUF_NAMESPACE_ID::Arena* arena,
                       bool is_message_owned = false);
  private:
  static void ArenaDtor(void* object);
  public:

  static const ClassData _class_data_;
  const ::PROTOBUF_NAMESPACE_ID::Message::ClassData*GetClassData() const final;

  ::PROTOBUF_NAMESPACE_ID::Metadata GetMetadata() const final;

  // nested types ----------------------------------------------------


  // accessors -------------------------------------------------------

  enum : int {
    kIargsFieldNumber = 1,
  };
  // map<string, string> iargs = 1;
  int iargs_size() const;
  private:
  int _internal_iargs_size() const;
  public:
  void clear_iargs();
  private:
  const ::PROTOBUF_NAMESPACE_ID::Map< std::string, std::string >&
      _internal_iargs() const;
  ::PROTOBUF_NAMESPACE_ID::Map< std::string, std::string >*
      _internal_mutable_iargs();
  public:
  const ::PROTOBUF_NAMESPACE_ID::Map< std::string, std::string >&
      iargs() const;
  ::PROTOBUF_NAMESPACE_ID::Map< std::string, std::string >*
      mutable_iargs();

  // @@protoc_insertion_point(class_scope:AlgoInput)
 private:
  class _Internal;

  template <typename T> friend class ::PROTOBUF_NAMESPACE_ID::Arena::InternalHelper;
  typedef void InternalArenaConstructable_;
  typedef void DestructorSkippable_;
  struct Impl_ {
    ::PROTOBUF_NAMESPACE_ID::internal::MapField<
        AlgoInput_IargsEntry_DoNotUse,
        std::string, std::string,
        ::PROTOBUF_NAMESPACE_ID::internal::WireFormatLite::TYPE_STRING,
        ::PROTOBUF_NAMESPACE_ID::internal::WireFormatLite::TYPE_STRING> iargs_;
    mutable ::PROTOBUF_NAMESPACE_ID::internal::CachedSize _cached_size_;
  };
  union { Impl_ _impl_; };
  friend struct ::TableStruct_algo_5fargs_2eproto;
};
// -------------------------------------------------------------------

class AlgoOutput_OargsEntry_DoNotUse : public ::PROTOBUF_NAMESPACE_ID::internal::MapEntry<AlgoOutput_OargsEntry_DoNotUse, 
    std::string, std::string,
    ::PROTOBUF_NAMESPACE_ID::internal::WireFormatLite::TYPE_STRING,
    ::PROTOBUF_NAMESPACE_ID::internal::WireFormatLite::TYPE_STRING> {
public:
  typedef ::PROTOBUF_NAMESPACE_ID::internal::MapEntry<AlgoOutput_OargsEntry_DoNotUse, 
    std::string, std::string,
    ::PROTOBUF_NAMESPACE_ID::internal::WireFormatLite::TYPE_STRING,
    ::PROTOBUF_NAMESPACE_ID::internal::WireFormatLite::TYPE_STRING> SuperType;
  AlgoOutput_OargsEntry_DoNotUse();
  explicit PROTOBUF_CONSTEXPR AlgoOutput_OargsEntry_DoNotUse(
      ::PROTOBUF_NAMESPACE_ID::internal::ConstantInitialized);
  explicit AlgoOutput_OargsEntry_DoNotUse(::PROTOBUF_NAMESPACE_ID::Arena* arena);
  void MergeFrom(const AlgoOutput_OargsEntry_DoNotUse& other);
  static const AlgoOutput_OargsEntry_DoNotUse* internal_default_instance() { return reinterpret_cast<const AlgoOutput_OargsEntry_DoNotUse*>(&_AlgoOutput_OargsEntry_DoNotUse_default_instance_); }
  static bool ValidateKey(std::string* s) {
    return ::PROTOBUF_NAMESPACE_ID::internal::WireFormatLite::VerifyUtf8String(s->data(), static_cast<int>(s->size()), ::PROTOBUF_NAMESPACE_ID::internal::WireFormatLite::PARSE, "AlgoOutput.OargsEntry.key");
 }
  static bool ValidateValue(std::string* s) {
    return ::PROTOBUF_NAMESPACE_ID::internal::WireFormatLite::VerifyUtf8String(s->data(), static_cast<int>(s->size()), ::PROTOBUF_NAMESPACE_ID::internal::WireFormatLite::PARSE, "AlgoOutput.OargsEntry.value");
 }
  using ::PROTOBUF_NAMESPACE_ID::Message::MergeFrom;
  ::PROTOBUF_NAMESPACE_ID::Metadata GetMetadata() const final;
  friend struct ::TableStruct_algo_5fargs_2eproto;
};

// -------------------------------------------------------------------

class AlgoOutput final :
    public ::PROTOBUF_NAMESPACE_ID::Message /* @@protoc_insertion_point(class_definition:AlgoOutput) */ {
 public:
  inline AlgoOutput() : AlgoOutput(nullptr) {}
  ~AlgoOutput() override;
  explicit PROTOBUF_CONSTEXPR AlgoOutput(::PROTOBUF_NAMESPACE_ID::internal::ConstantInitialized);

  AlgoOutput(const AlgoOutput& from);
  AlgoOutput(AlgoOutput&& from) noexcept
    : AlgoOutput() {
    *this = ::std::move(from);
  }

  inline AlgoOutput& operator=(const AlgoOutput& from) {
    CopyFrom(from);
    return *this;
  }
  inline AlgoOutput& operator=(AlgoOutput&& from) noexcept {
    if (this == &from) return *this;
    if (GetOwningArena() == from.GetOwningArena()
  #ifdef PROTOBUF_FORCE_COPY_IN_MOVE
        && GetOwningArena() != nullptr
  #endif  // !PROTOBUF_FORCE_COPY_IN_MOVE
    ) {
      InternalSwap(&from);
    } else {
      CopyFrom(from);
    }
    return *this;
  }

  static const ::PROTOBUF_NAMESPACE_ID::Descriptor* descriptor() {
    return GetDescriptor();
  }
  static const ::PROTOBUF_NAMESPACE_ID::Descriptor* GetDescriptor() {
    return default_instance().GetMetadata().descriptor;
  }
  static const ::PROTOBUF_NAMESPACE_ID::Reflection* GetReflection() {
    return default_instance().GetMetadata().reflection;
  }
  static const AlgoOutput& default_instance() {
    return *internal_default_instance();
  }
  static inline const AlgoOutput* internal_default_instance() {
    return reinterpret_cast<const AlgoOutput*>(
               &_AlgoOutput_default_instance_);
  }
  static constexpr int kIndexInFileMessages =
    3;

  friend void swap(AlgoOutput& a, AlgoOutput& b) {
    a.Swap(&b);
  }
  inline void Swap(AlgoOutput* other) {
    if (other == this) return;
  #ifdef PROTOBUF_FORCE_COPY_IN_SWAP
    if (GetOwningArena() != nullptr &&
        GetOwningArena() == other->GetOwningArena()) {
   #else  // PROTOBUF_FORCE_COPY_IN_SWAP
    if (GetOwningArena() == other->GetOwningArena()) {
  #endif  // !PROTOBUF_FORCE_COPY_IN_SWAP
      InternalSwap(other);
    } else {
      ::PROTOBUF_NAMESPACE_ID::internal::GenericSwap(this, other);
    }
  }
  void UnsafeArenaSwap(AlgoOutput* other) {
    if (other == this) return;
    GOOGLE_DCHECK(GetOwningArena() == other->GetOwningArena());
    InternalSwap(other);
  }

  // implements Message ----------------------------------------------

  AlgoOutput* New(::PROTOBUF_NAMESPACE_ID::Arena* arena = nullptr) const final {
    return CreateMaybeMessage<AlgoOutput>(arena);
  }
  using ::PROTOBUF_NAMESPACE_ID::Message::CopyFrom;
  void CopyFrom(const AlgoOutput& from);
  using ::PROTOBUF_NAMESPACE_ID::Message::MergeFrom;
  void MergeFrom( const AlgoOutput& from) {
    AlgoOutput::MergeImpl(*this, from);
  }
  private:
  static void MergeImpl(::PROTOBUF_NAMESPACE_ID::Message& to_msg, const ::PROTOBUF_NAMESPACE_ID::Message& from_msg);
  public:
  PROTOBUF_ATTRIBUTE_REINITIALIZES void Clear() final;
  bool IsInitialized() const final;

  size_t ByteSizeLong() const final;
  const char* _InternalParse(const char* ptr, ::PROTOBUF_NAMESPACE_ID::internal::ParseContext* ctx) final;
  uint8_t* _InternalSerialize(
      uint8_t* target, ::PROTOBUF_NAMESPACE_ID::io::EpsCopyOutputStream* stream) const final;
  int GetCachedSize() const final { return _impl_._cached_size_.Get(); }

  private:
  void SharedCtor(::PROTOBUF_NAMESPACE_ID::Arena* arena, bool is_message_owned);
  void SharedDtor();
  void SetCachedSize(int size) const final;
  void InternalSwap(AlgoOutput* other);

  private:
  friend class ::PROTOBUF_NAMESPACE_ID::internal::AnyMetadata;
  static ::PROTOBUF_NAMESPACE_ID::StringPiece FullMessageName() {
    return "AlgoOutput";
  }
  protected:
  explicit AlgoOutput(::PROTOBUF_NAMESPACE_ID::Arena* arena,
                       bool is_message_owned = false);
  private:
  static void ArenaDtor(void* object);
  public:

  static const ClassData _class_data_;
  const ::PROTOBUF_NAMESPACE_ID::Message::ClassData*GetClassData() const final;

  ::PROTOBUF_NAMESPACE_ID::Metadata GetMetadata() const final;

  // nested types ----------------------------------------------------


  // accessors -------------------------------------------------------

  enum : int {
    kOargsFieldNumber = 1,
  };
  // map<string, string> oargs = 1;
  int oargs_size() const;
  private:
  int _internal_oargs_size() const;
  public:
  void clear_oargs();
  private:
  const ::PROTOBUF_NAMESPACE_ID::Map< std::string, std::string >&
      _internal_oargs() const;
  ::PROTOBUF_NAMESPACE_ID::Map< std::string, std::string >*
      _internal_mutable_oargs();
  public:
  const ::PROTOBUF_NAMESPACE_ID::Map< std::string, std::string >&
      oargs() const;
  ::PROTOBUF_NAMESPACE_ID::Map< std::string, std::string >*
      mutable_oargs();

  // @@protoc_insertion_point(class_scope:AlgoOutput)
 private:
  class _Internal;

  template <typename T> friend class ::PROTOBUF_NAMESPACE_ID::Arena::InternalHelper;
  typedef void InternalArenaConstructable_;
  typedef void DestructorSkippable_;
  struct Impl_ {
    ::PROTOBUF_NAMESPACE_ID::internal::MapField<
        AlgoOutput_OargsEntry_DoNotUse,
        std::string, std::string,
        ::PROTOBUF_NAMESPACE_ID::internal::WireFormatLite::TYPE_STRING,
        ::PROTOBUF_NAMESPACE_ID::internal::WireFormatLite::TYPE_STRING> oargs_;
    mutable ::PROTOBUF_NAMESPACE_ID::internal::CachedSize _cached_size_;
  };
  union { Impl_ _impl_; };
  friend struct ::TableStruct_algo_5fargs_2eproto;
};
// ===================================================================


// ===================================================================

#ifdef __GNUC__
  #pragma GCC diagnostic push
  #pragma GCC diagnostic ignored "-Wstrict-aliasing"
#endif  // __GNUC__
// -------------------------------------------------------------------

// AlgoInput

// map<string, string> iargs = 1;
inline int AlgoInput::_internal_iargs_size() const {
  return _impl_.iargs_.size();
}
inline int AlgoInput::iargs_size() const {
  return _internal_iargs_size();
}
inline void AlgoInput::clear_iargs() {
  _impl_.iargs_.Clear();
}
inline const ::PROTOBUF_NAMESPACE_ID::Map< std::string, std::string >&
AlgoInput::_internal_iargs() const {
  return _impl_.iargs_.GetMap();
}
inline const ::PROTOBUF_NAMESPACE_ID::Map< std::string, std::string >&
AlgoInput::iargs() const {
  // @@protoc_insertion_point(field_map:AlgoInput.iargs)
  return _internal_iargs();
}
inline ::PROTOBUF_NAMESPACE_ID::Map< std::string, std::string >*
AlgoInput::_internal_mutable_iargs() {
  return _impl_.iargs_.MutableMap();
}
inline ::PROTOBUF_NAMESPACE_ID::Map< std::string, std::string >*
AlgoInput::mutable_iargs() {
  // @@protoc_insertion_point(field_mutable_map:AlgoInput.iargs)
  return _internal_mutable_iargs();
}

// -------------------------------------------------------------------

// -------------------------------------------------------------------

// AlgoOutput

// map<string, string> oargs = 1;
inline int AlgoOutput::_internal_oargs_size() const {
  return _impl_.oargs_.size();
}
inline int AlgoOutput::oargs_size() const {
  return _internal_oargs_size();
}
inline void AlgoOutput::clear_oargs() {
  _impl_.oargs_.Clear();
}
inline const ::PROTOBUF_NAMESPACE_ID::Map< std::string, std::string >&
AlgoOutput::_internal_oargs() const {
  return _impl_.oargs_.GetMap();
}
inline const ::PROTOBUF_NAMESPACE_ID::Map< std::string, std::string >&
AlgoOutput::oargs() const {
  // @@protoc_insertion_point(field_map:AlgoOutput.oargs)
  return _internal_oargs();
}
inline ::PROTOBUF_NAMESPACE_ID::Map< std::string, std::string >*
AlgoOutput::_internal_mutable_oargs() {
  return _impl_.oargs_.MutableMap();
}
inline ::PROTOBUF_NAMESPACE_ID::Map< std::string, std::string >*
AlgoOutput::mutable_oargs() {
  // @@protoc_insertion_point(field_mutable_map:AlgoOutput.oargs)
  return _internal_mutable_oargs();
}

#ifdef __GNUC__
  #pragma GCC diagnostic pop
#endif  // __GNUC__
// -------------------------------------------------------------------

// -------------------------------------------------------------------

// -------------------------------------------------------------------


// @@protoc_insertion_point(namespace_scope)


// @@protoc_insertion_point(global_scope)

#include <google/protobuf/port_undef.inc>
#endif  // GOOGLE_PROTOBUF_INCLUDED_GOOGLE_PROTOBUF_INCLUDED_algo_5fargs_2eproto
