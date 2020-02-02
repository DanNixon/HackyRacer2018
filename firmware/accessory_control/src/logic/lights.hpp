#pragma once

namespace logic {
namespace lights {
enum class role {
  brake,
  reverse,
  headlights_full,
  headlights,
};

void init();

void set_role(role const r, bool const active);
bool role_is_enabled(role const r);

void output();
} // namespace lights
} // namespace logic
